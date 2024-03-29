import os
from roboter import robotReader as robRead
from roboter import robotWriter as robWrite


class FileCheck():

    def fileExist(self, path):
        return os.path.exists(path)

class HandleRobot():
    NAME_OR_COUNT = "Name,Count"

    def __init__(self, location):
        self.location = location
        self.read = robRead.RobotReader(location)
        self.write = robWrite.RobotWriter()
    
    def textChange(self):
        temp = []

        for line in self.read.fileReader():
            if self.NAME_OR_COUNT not in line:
                temp.append(line.split(','))

        return temp

    def saveFile(self, group):

        try:
            self.write.fileWriter(self.location, group)
        
        except:
            print("set empty list check out input value of list")

"""
m = HandleRobot("d:/Project/Python/codinglearn/fileSys/test.csv")
k = HandleRobot("d:/Project/Python/codinglearn/test.csv")

a = robData.Guest()
b = robData.Guest()

text = k.textChange()

for row in text:
    b.appendGroup(row[0], row[1])

for a, b in b.Group():
    print(a, b)

#print(b.Group()[0][0]) A print(b.Group()[0]) (A, 3)
"""