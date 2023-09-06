#!/usr/bin/env python
import numpy as np

targetChapter = 5
targetVerse = 20

matrixFile = './data/output/matrix.txt'

m = np.loadtxt(matrixFile)

nephi_file = open("./data/text/nephi.txt", "r")
nephi_data = nephi_file.read().split("$")
nephi_file.close()

alma_file = open("./data/text/alma.txt", "r")
alma_data= alma_file.read().split("$")
alma_file.close()

target = [i for i, s in enumerate(nephi_data) if (str(targetChapter) + ":" + str(targetVerse)) in s][0]

offset = len(nephi_data)
nephiMat = m[target,offset:]
position = np.unravel_index(np.argmax(nephiMat, axis=None), nephiMat.shape)[0]

print("\nTarget:\n1 Nephi " + nephi_data[target])
print("Result:\nAlma " + alma_data[position])