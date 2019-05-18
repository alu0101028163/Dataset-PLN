import sys
import os



path = "../outputs"
arff_file = open("./goodreads_nlp.arff","w+")
categories = open("categories.txt","r")


header = "@RELATION goodreads_nlp\n"
header += "\t@ATTRIBUTE text  string\n"
header += "\t@ATTRIBUTE class        {"

header += categories.readline().strip()

for category in categories:
    header += "," + category.strip()

header += "}\n"
header += "@DATA"
arff_file.write(header + "\n")



for filename in os.listdir(path):

    file_ = open(path + "/" + filename,"r+")
    for line in file_:
        arff_file.write(line)

arff_file.close()
