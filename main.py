#!/usr/bin/env python3
#
#  ==========================================================================
#  main.py - A project for TribaHacks 2016 - LOGAPPS Challenge
#
#  Created on: Apr 1, 2016
#  Author: Yangyang He, Liang Wu, Martin Liu
#
#  Reference:
#  Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language
#  Processing with Python. O’Reilly Media Inc.
#  Marie-Catherine de Marneffe, Bill MacCartney and Christopher D. Manning. 2006.
#  Generating Typed Dependency Parses from Phrase Structure Parses. In LREC 2006.
#  ==========================================================================

#Import NLTK module and Stanford Parser
import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.parse.stanford import StanfordParser
from nltk.parse.stanford import StanfordDependencyParser
import csv

#Import Sentence class from Sentence.py
from Sentence import Sentence
import Sentence

#Use Stanford Dependency Parser to parse each sentence
def Dep_parce_tree(sentList):

    verb_list = [] #All verbs in text

    for sent_obj in sentList:

        sent_str = sent_obj.str

        #Parse sentence with Stanford Dependency Parser
        dep_parser = StanfordDependencyParser(model_path="edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")
        dep_parses = dep_parser.raw_parse(sent_str)

        #Iterate through parsing results to find sbj and obj
        for parse in dep_parses:

            objList = [] #List of objects in the sentence
            dirObj = [] #List of direct objects in the sentence
            verbList = []


            #Find direct objects
            for p in parse.triples():
                #print (p)
                if "VB" in p[0][1]:
                    verbList.append(p[0][0])
                if "VB" in p[2][1]:
                    verbList.append(p[2][0])

                if p[1] == "dobj":

                    objList.append(p[2][0])
                    dirObj.append(p[2][0])

            #Find siblings of direct objects
            for p in parse.triples():
                if p[0][0] in dirObj and p[1] == "conj":
                    objList.append(p[2][0])
            objList = list(set(objList))

            sent_obj.obj = objList
            verbList = list(set(verbList))

            #Find subject in the sentence
            dep_tree = parse.tree()
            sbjTree = dep_tree[0]
            sbjList = []
            if isinstance(sbjTree,str):
                sbjList.append(sbjTree)
            else:
                sbjList.extend(sbjTree.leaves())
                sbjList.append(sbjTree.label())

            for s in sbjList:
                sent_obj.sbj += s
                sent_obj.sbj += " "

        #Tag the words in sentence and find verbs
        word_list = nltk.word_tokenize(sent_str) #A list of words in the sentence
        tag_list = nltk.pos_tag(word_list) #A list of tuples of word and tag

        for tag_tuple in tag_list:

            if "VB" in tag_tuple[1]:
                #Convert to base verb, append real verb to sent_obj.vb
                base_verb = WordNetLemmatizer().lemmatize(tag_tuple[0].lower(),'v')
                if base_verb not in ("be", "have", "can"):
                    sent_obj.verb.append(base_verb)

        #Another algorithm of finding verbs
        sent_obj.verb = []
        for v in verbList:
            base_verb = WordNetLemmatizer().lemmatize(v.lower(),'v')
            if base_verb not in ("be", "have", "can"):
                sent_obj.verb.append(base_verb)


        print("Paragraph: " + str(sent_obj.paraID))
        print("Setence: " + str(sent_obj.sentID))
        print("String: " + str(sent_obj))
        print("Subject: " + sent_obj.sbj)
        print("Verb: " + str(sent_obj.verb))
        print("Object: " + str(sent_obj.obj))
        print()
    return sentList

fileName = "appendix1"
sentList = Dep_parce_tree(Sentence.fileToSentList(fileName + ".txt"))


# create first result file
output_file = open(fileName + "result.csv", "w")
rowwriter = csv.writer(output_file, delimiter=',', quoting = csv.QUOTE_MINIMAL)
rowwriter.writerow(["Para. #", "Sent. #", "Subject", "Objects", "Verbs"])
for sent in sentList:
    sent.print2file(rowwriter)
output_file.close()
