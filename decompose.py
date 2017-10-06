#!/usr/bin/env python3
#
#  ==========================================================================
#  decompose.py - A project for TribaHacks 2016 - LOGAPPS Challenge
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
from sentence import Sentence
import sentence

#Use Stanford Dependency Parser to parse each sentence
def dep_parce_tree(sentence_list):

    verb_list = [] #All verbs in text

    for sentence_obj in sentence_list:

        sentence_str = sentence_obj.str

        #Parse sentence with Stanford Dependency Parser
        dep_parser = StanfordDependencyParser(model_path="edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")
        dep_parses = dep_parser.raw_parse(sentence_str)

        #Iterate through parsing results to find sbj and obj
        for parse in dep_parses:

            object_list = [] #List of objects in the sentence
            direct_object_list = [] #List of direct objects in the sentence
            verb_list = []


            #Find direct objects
            for p in parse.triples():
                #print (p)
                if "VB" in p[0][1]:
                    verb_list.append(p[0][0])
                if "VB" in p[2][1]:
                    verb_list.append(p[2][0])

                if p[1] == "dobj":

                    object_list.append(p[2][0])
                    direct_object_list.append(p[2][0])

            #Find siblings of direct objects
            for p in parse.triples():
                if p[0][0] in direct_object_list and p[1] == "conj":
                    object_list.append(p[2][0])
            object_list = list(set(object_list))

            sentence_obj.obj = object_list
            verb_list = list(set(verb_list))

            #Find subject in the sentence
            dep_tree = parse.tree()
            subject_tree = dep_tree[0]
            subject_list = []
            if isinstance(subject_tree,str):
                subject_list.append(subject_tree)
            else:
                subject_list.extend(subject_tree.leaves())
                subject_list.append(subject_tree.label())

            for s in subject_list:
                sentence_obj.sbj += s
                sentence_obj.sbj += " "

        #Tag the words in sentence and find verbs
        word_list = nltk.word_tokenize(sentence_str) #A list of words in the sentence
        tag_list = nltk.pos_tag(word_list) #A list of tuples of word and tag

        for tag_tuple in tag_list:

            if "VB" in tag_tuple[1]:
                #Convert to base verb, append real verb to sentence_obj.vb
                base_verb = WordNetLemmatizer().lemmatize(tag_tuple[0].lower(),'v')
                if base_verb not in ("be", "have", "can"):
                    sentence_obj.verb.append(base_verb)

        #Another algorithm of finding verbs
        sentence_obj.verb = []
        for v in verb_list:
            base_verb = WordNetLemmatizer().lemmatize(v.lower(),'v')
            if base_verb not in ("be", "have", "can"):
                sentence_obj.verb.append(base_verb)


        print("Paragraph: " + str(sentence_obj.paraID))
        print("Setence: " + str(sentence_obj.sentID))
        print("String: " + str(sentence_obj))
        print("Subject: " + sentence_obj.sbj)
        print("Verb: " + str(sentence_obj.verb))
        print("Object: " + str(sentence_obj.obj))
        print()
    return sentence_list

filename = input("Source text file (w/o extension name): ")
sentence_list = dep_parce_tree(Sentence.make_sentence_list("texts/" + filename + ".txt"))


# create first result file
outputfile = open("result/" + filename + "_decomposed.csv", "w")
rowwriter = csv.writer(outputfile, delimiter=',', quoting = csv.QUOTE_MINIMAL)
rowwriter.writerow(["Para. #", "Sent. #", "Subject", "Objects", "Verbs"])
for sentence in sentence_list:
    sentence.print2file(rowwriter)
outputfile.close()
