#!/usr/bin/env python3
#
#  ==========================================================================
#  sentence.py - A project for TribaHacks 2016 - LOGAPPS Challenge
#
#  Created on: Apr 1, 2016
#  Author: Yangyang He, Liang Wu, Martin Liu
#
#  ==========================================================================

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
        sentence_list = [str(self.paraID), str(self.sentID), self.sbj, " ".join(self.obj), " ".join(self.verb)]
        rowwriter.writerow(sentence_list)

    def __str__(self):
        return self.str

# identify if a line is a title (all capitalized)
def is_title(line):
    line_words = nltk.word_tokenize(line)
    is_title = False
    for w in line_words:
        if not w.isupper():
            return False
        if is_title:
            return True

# delete everything within "()"
def delete_in_bracket(string):
    str_copy = ""
    count = 0
    for char in string:
        if char != "(" and char != ")" and count == 0:
            str_copy += char
        if char == "(":
            count += 1
        if char == ")":
            count -= 1
    return str_copy

# open the original file and change the capitalized titles to a line break
def tidy_file(filename):
    with open(filename,"r",encoding="UTF-8") as input:
        with open("temp/temp.txt","w") as output:
            for line in input:
                if is_title(line) is False:
                    if not line.endswith(" \n") and not line.endswith(".\n"):
                        line = line[:-1]
                        line = line + ".\n"
                    output.write(line)
                else:
                    output.write('\n')
    output.close()
    return "temp.txt"


# Initialization. Decompose article to several paragraphs, using double line change as separator
def separate_paragraph(string):
    f = open("temp/temp.txt","r",encoding="UTF-8")
    data = f.read()
    data = delete_in_bracket(data)
    paragraphs = []
    paragraphs = data.split("\n\n")
    return paragraphs


# Delete all sentence fragments (i.e. sentences with no verb). Moreover, delete all paragraphs with no sentences.
def delete_fragments(paragraphs):
    new_paragraph = []
    for paragraph_index in range(0,len(paragraphs)):
        new_sentence = []
        p = paragraphs[paragraph_index]
        sentence_detector = nltk.data.load('tokenizers/punkt/english.pickle')
        sentences = sentence_detector.tokenize(p.strip())
        for sentence_index in range(0,len(sentences)):
            sentence = sentences[sentence_index]
            words = nltk.word_tokenize(sentence)
            tag_words = nltk.pos_tag(words)
            verb_count = 0
            for value in tag_words:
                if "VB" in value[1]:
                    verb_count += 1

            if verb_count != 0:
                new_sentence.append(sentences[sentence_index])
        if new_sentence:
            new_paragraph.append(new_sentence)
    return new_paragraph

# Print all the lines with count
def to_sentences(paragraph):
    sentence_list = []
    count = 0
    for paragraph_index in range(0,len(paragraph)):
        p = paragraph[paragraph_index]
        for sentence_index in range(0,len(p)):
            new_str = p[sentence_index].replace("\n", "")
            count += 1
            new_sentence = Sentence()
            new_sentence.str = new_str
            new_sentence.paraID = paragraph_index + 1
            new_sentence.sentID = sentence_index + 1
            sentence_list.append(new_sentence)
    return sentence_list

# The complete method convert a file to a list of sentence object
def make_sentence_list(filename):
    filename = tidy_file(filename)
    paragraph_list = separate_paragraph(filename)
    paragraph_list = delete_fragments(paragraph_list)
    sentence_list = to_sentences(paragraph_list)
    return sentence_list
