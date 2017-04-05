import csv

class sentence_class(object):
  def __init__(self):
    self.str = ""
    self.sbj = ""
    self.obj = []
    self.verb = []
    self.rem = []
    self.paraID = 0
    self.sentID = 0
    
    
  def print2file(self, file_name):
    sent_list = [str(self.id), self.sbj, " ".join(self.obj), " ".join(self.verb), " ".join(self.rem)]
	output_file = open(file_name, "w")
    rowwriter = csv.writer(output_file, delimiter=',', quoting = csv.QUOTE_MINIMAL)    
    rowwriter.writerow(sent_list)
    output_file.close()
    
  def __str__(self):
    return self.str