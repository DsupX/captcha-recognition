import cv2
import csv
import os
import random as rd

class LoadImage:
    def __init__(self, source):
        self.source = source
        print("Set Source File: ", self.source)
        self.info = "Read image from source and label from scv file"

    def setSource(self, new_source):
        self.source = new_source
        print("Set source file: ", self.source)

    def getImage(self, names, mode=None):
        pathFile = self.getPathImage(names)
        arr = []
        for p in pathFile:
            if mode is None:
                arr.append(cv2.imread(p))
            else:
                arr.append(cv2.imread(p, mode))
        return arr

    def getPathImage(self, names):
        files = names
        arr = []
        for i in range(len(files)):
            fullpath = os.path.join(self.source, files[i])
            if os.path.isdir(fullpath) == False:
                arr.append(fullpath)
        return arr

    def getLabel(self, source, columns):
        names = []
        label = []
        with open(source, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                names.append(row[columns[0]])
                label.append(row[columns[1]])

        return names, label



if __name__ == '__main__':
    img = LoadImage("data/tmp")


    names, label = img.getLabel('data/tmp.csv', ['ImageId', 'Text'])
    image = img.getImage(names, mode=0)
    r = rd.randint(0, 1000)
    print(r)
    cv2.imshow('f', image[r])
    print(label[r])
    cv2.waitKey(0)