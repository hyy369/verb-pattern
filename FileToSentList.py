import nltk	
from nltk.corpus import words
import re
import csv
# a class of sentence to keep track of the content, differnt parts, and the unique ID of the sentences.
class Sentence(object):
    
    def __init__(self):
        self.str = ""
        self.sbj = ""
        self.obj = []
        self.verb = []
        self.paraID = 0
        self.sentID = 0
	
    def print2file(self, rowwriter):
        sent_list = [str(self.paraID), str(self.sentID), self.sbj, " ".join(self.obj), " ".join(self.verb)]   
        rowwriter.writerow(sent_list) 
		
    def __str__(self):
        return self.str

# identify if a line is a title (all capitalized)
def isTitle(line):
    lineWordList = nltk.word_tokenize(line)
    isTitle = False
    for w in lineWordList:
        if not w.isupper():
            return False
        if isTitle:
            return True
		
# delete everything within "()"
def delInBracket(string):
    strCopy = ""
    count = 0
    for char in string:
        if char != "(" and char != ")" and count == 0:
            strCopy += char
        if char == "(":
            count += 1
        if char == ")":
            count -= 1
    return strCopy

# open the original file and change the capitalized titles to a line break
def clearFile(string):
    with open(string,"r",encoding="UTF-8") as input:
        with open("newText.txt","w") as output:
            for line in input:
                if isTitle(line) is False:
                    if not line.endswith(" \n") and not line.endswith(".\n"):
                        line = line[:-1]
                        line = line + ".\n"
                    output.write(line)
                else:
                    output.write('\n')
    output.close()
    return "newText.txt"


# Initialization. Decompose article to several paragraphs, using double line change as separator
def separatePara(string):
    f = open("newText.txt","r",encoding="UTF-8")
    data = f.read()
    data = delInBracket(data)
    paragraphs = []
    paragraphs = data.split("\n\n")
    return paragraphs


# Delete all sentences with no verb. Moreover, delete all paragraphs with no sentences. 
def deleteNonSentence(paragraphs):
    newPara = []
    for paraIndex in range(0,len(paragraphs)):
        newSent = []
        p = paragraphs[paraIndex]
        sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
        sentences = sent_detector.tokenize(p.strip())
        for sentIndex in range(0,len(sentences)):	
            sent = sentences[sentIndex]
            words = nltk.word_tokenize(sent)
            tagWords = nltk.pos_tag(words)
            verbCount = 0
            for value in tagWords:
                if "VB" in value[1]:
                    verbCount += 1
		    
            if verbCount != 0:
                newSent.append(sentences[sentIndex])
        if newSent:
            newPara.append(newSent)
    return newPara

# Print all the lines with count 
def toSentences(newPara):
    sentList = []
    count = 0
    for paraIndex in range(0,len(newPara)):
        p = newPara[paraIndex]
        for sentIndex in range(0,len(p)):
            newStr = p[sentIndex].replace("\n", "")
            count += 1	
            newSent = Sentence()
            newSent.str = newStr
            newSent.paraID = paraIndex + 1
            newSent.sentID = sentIndex + 1
            sentList.append(newSent) 
    return sentList

# The complete method convert a file to a list of sentence object
def fileToSentList(fileName):
    fileName = clearFile(fileName)
    paraList = separatePara(fileName)
    paraList = deleteNonSentence(paraList)
    sentList = toSentences(paraList)
    return sentList