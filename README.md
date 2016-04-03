### Part I FileToSentList.py
This source file reads trough a text file, identify complete sentences within the file, and initialize each sentence as a Sentence object. The object will have the following fields:
*str: the string representation of the sentence's content
*sbj: the subject part of the sentence
*obj: the list of the object parts of the sentence
#paraID: the number of paragraph where the sentence appears
#sentID: the index of the sentence within the paragraph
This file returns a list of Sentence objects that represents all complete sentences in the text file.

### Part II npl.py
This source file iterates through each Sentence object, and
*parses the sentence using Stanford Dependency Parser to look for subjects and objects
*tokenizes and tags each word to identify real verbs within the sentence
*creates a csv file with information of subjects, objects and verbs of each sentence

### Part III ExtendTable.py
This source file extends the csv file created in Part II and count verbs of different categories provided by Table 1.