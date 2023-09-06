#!/usr/bin/env python
from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

@app.route('/')
def start():
    return render_template('index.html')


@app.route('/submission',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      t,o = fetch(result["Chapter"],result["Verse"])
      if(t!=1):
        return render_template("result.html",errdisplay="none", target=t, output=o)
      else:
        errorVerse = "1 Nephi " + str(o[0]) + ":" + str(o[1])
        return render_template("index.html", errdisplay="block",verse=errorVerse)

def fetch(chapter, verse):
    matrixFile = './data/output/matrix.txt'

    m = np.loadtxt(matrixFile)

    nephi_file = open("./data/text/nephi.txt", "r")
    nephi_data = nephi_file.read().replace("$","$ ").split("$")
    nephi_file.close()

    alma_file = open("./data/text/alma.txt", "r")
    alma_data= alma_file.read().split("$")
    alma_file.close()

    try:
        target = [i for i, s in enumerate(nephi_data) if ((" " + str(chapter) + ":" + str(verse)) + " " in s)][0]

        offset = len(nephi_data)
        nephiMat = m[target,offset:]
        position = np.unravel_index(np.argmax(nephiMat, axis=None), nephiMat.shape)[0]
        t = "1 Nephi " + nephi_data[target]
        o = "Alma " + alma_data[position]
        return t,o
    except:
        return 1,[chapter,verse]

if __name__ == '__main__':
    app.run()