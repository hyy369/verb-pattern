#!/usr/bin/env python3
#
#  ==========================================================================
#  expand.py - A project for TribaHacks 2016 - LOGAPPS Challenge
#
#  Created on: Apr 1, 2016
#  Author: Yangyang He, Liang Wu, Martin Liu
#
#  ==========================================================================

import nltk

# transform table1 into a dictionary
def table2dic(table_filename):
  table = open(table_filename, "r")
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


filename = input("Source text file (w/o extension name): ")
table_dict = table2dic("table1.csv") #provided by the challenfe


input_file = open(filename + "_decomposed.csv", "r")
result_file = open(filename + "_expanded.csv", "w")
input_row = input_file.readline().strip()
result_file.write(input_row + ",Ctg. #1,Ctg. #2,Ctg. #3,Ctg. #4,Ctg. #5,Ctg. #6,Ctg. #7\n")
input_row = input_file.readline().strip()
counted_verb = []


while input_row != "":
  new_info = []
  input_columns = input_row.split(",")
  key_words = input_columns[4].split(" ") #list of verbs

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
  new_info_str = ",".join(new_info)
  print(input_row + "," + new_info_str)
  result_file.write(input_row + "," + new_info_str + "\n")
  for word in key_words:
    if word not in counted_verb:
      counted_verb.append(word)
  input_row = input_file.readline().strip()

result_file.close()
input_file.close()
