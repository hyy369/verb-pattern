This is a project for TribeHacks 2016 Logapps Challenge. The original prompt is posted at: https://github.com/ACMWM/Logapps-TribeHacks-Challenge-2016

### Part I FileToSentList.py
This source file reads trough a text file, identify complete sentences within the file, and initialize each sentence as a Sentence object. The object will have the following fields:
* str: the string representation of the sentence's content
* sbj: the subject part of the sentence
* obj: the list of the object parts of the sentence
* paraID: the number of paragraph where the sentence appears
* sentID: the index of the sentence within the paragraph
This file returns a list of Sentence objects that represents all complete sentences in the text file.

### Part II npl.py
This source file iterates through each Sentence object, and
* parses the sentence using Stanford Dependency Parser to look for subjects and objects
* tokenizes and tags each word to identify real verbs within the sentence
* creates a csv file with information of subjects, objects and verbs of each sentence

### Part III ExtendTable.py
This source file extends the csv file created in Part II and count verbs of different categories provided by table1.csv.

### Future directions
We are looking forward to apply our program to various texts across time and create a database of the occurrance of verbs of different categories. We want to look for a pattern in change of the using of verbs over time, and give each verb an index regarding the occurance in a certain time period. We want to use this extended version of our table1.csv to determine the creation time of a given text.
