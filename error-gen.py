#import os
import csv

sourceFile = open("errors.csv~", "r")
sourceLines = csv.reader(sourceFile, delimiter=",")

for code in sourceLines:
    def nameGet(name):
        if name == "code":
            return code[0].strip()
        elif name == "title":
            return code[1].strip()
        elif name == "body":
            return code[2].strip()
        else:
            print("ERROR: Invalid template")
            return "ERROR"

    templateFile = open("template.shtml", "r")
    template = templateFile.readlines()
    out = open("output/" + code[0] + ".shtml", "w")
    for line in template:
        while "{{" in line:
            start = line.find("{{")
            end = line.find("}}")
            name = line[start + 2:end].lower().strip()
            line = line[:start] + nameGet(name) + line[end+2:]
        
        out.write(line)

    templateFile.close()
    out.close()
    
