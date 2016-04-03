#!/usr/bin/env python3
#
#  ==========================================================================
#  FileToSentList.py - A project for TribaHacks 2016 - LOGAPPS Challenge
#
#  Created on: Apr 1, 2016
#  Author: Yangyang He, Liang Wu, Martin Liu
#
#  ==========================================================================

import nltk


fileName = "appendix1"

# transform table1 into a dictionary
def table2dic(table_name):
  table = open("table1.csv", "r")
  table.readline()
  table_row = table.readline().strip()
  dictionary = {}
  while table_row != "":
    items = table_row.split(",")
    verb = items[0].strip()
    dictionary[verb] = []
    items.pop(0)
    for each in items:
      dictionary[verb].append(each)
    table_row = table.readline().strip()
  table.close()
  return dictionary



table_dict = table2dic("table1.csv")


file = open(fileName + "result.csv", "r")
new_file = open(fileName + "result2.csv", "w")
file_row = file.readline().strip()
new_file.write(file_row + ",Ctg. #1,Ctg. #2,Ctg. #3,Ctg. #4,Ctg. #5,Ctg. #6,Ctg. #7\n")
file_row = file.readline().strip()
counted_verb = []


while file_row != "":
  new_info = []
  columns = file_row.split(",")
  key_words = columns[4].split(" ") #list of verbs
  
  for category in range(7):
    sum = 0
    ctg_str = ""
    for verb in key_words:
      verb = verb.capitalize()#.strip("\n")
      if verb in table_dict:
        if verb not in counted_verb:
          sum += int(table_dict[verb][category])
          ctg_str += str(table_dict[verb][category]) + "+"
        else:
          ctg_str += "0+"          
      else:
        ctg_str += "0+"
      
    new_info.append(ctg_str[0:-1] + "=" + str(sum))
  new = ",".join(new_info)
  print(file_row + "," + new)
  new_file.write(file_row + "," + new + "\n")
  for word in key_words:
    if word not in counted_verb:
      counted_verb.append(word)
  file_row = file.readline().strip()
  
new_file.close()
file.close()

  
  