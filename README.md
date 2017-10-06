This project, originally named "verb-pattern-plus" is the 2016 Tribe Hackathon Winner in Natural Language Processing. The challenge prompt was created by LOGAPPS and is posted at: https://github.com/ACMWM/Logapps-TribeHacks-Challenge-2016
To successfully run this program, users are expected to have installed NLTK 3.0+ and corrsponding packages (http://www.nltk.org), Stanford Parsers (https://github.com/nltk/nltk/wiki/Installing-Third-Party-Software), Java 8, JDK 1.8+ and default encoding set to "UTF-8". Please feel free to report any compatibility issues.

### Part I sentence.py
The `Sentence class` is defined in this source file. A Sentence object will have the following fields:
* str: the string representation of the sentence's content
* sbj: the subject part of the sentence
* obj: the list of the object parts of the sentence
* paraID: the number of paragraph where the sentence appears
* sentID: the index of the sentence within the paragraph

The `make_sentence_list(filename)` method reads trough a text file, identify complete sentences within the file, and initialize each sentence as a Sentence object. This file returns a list of Sentence objects that represents all complete sentences in the text file.

This script will generate a temporary text file in `temp/`.

### Part II decompose.py
This source file iterates through each Sentence object, and
* parses the sentence using Stanford Dependency Parser to look for subjects and objects
* tokenizes and tags each word to identify real verbs within the sentence
* creates a csv file with information of subjects, objects and verbs of each sentence

User will have to input the source text file name (w/o directory or extension names).The result file is `result/xxx_decomposed.csv`.

### Part III expand.py
This source file extends the csv file created in Part II and count verbs of different categories provided by `table1.csv`. User will have to input the source text file name (w/o directory or extension names). The result file is `result/xxx_expanded.csv`.

### Directories
`./`: Root directory contains source codes, readme docs, the challenge prompt, the presentation, and `table1.csv`, which is provided by the challenge.

`en`: necessary local nltk libraries for English.

`result`: result tables in csv files.

`temp`: cache space for tidying texts.

`texts`: text files that need to be processed.

### Future applications
The score table of some key verbs provided by `table1.csv` is randomly generated. However, we can apply VerbPattern to plenty amount of text files and relate the pattern of output score table with the texts' author or other information. Each text file will have a unique matrix of score table which can be regarded as its fingerprint. We can use this database of text-fingerprints to maybe predict information of a given anonymous text or detect plagiarism, etc.
Our Sentence object include not only the verbs, but also information regarding subjects and objects of a sentence. By a simple extension of the project, we can create score tables for subjects and objects too, so that we can analyze the headlines people are mostly talking about on social network, etc.
