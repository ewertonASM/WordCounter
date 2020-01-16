import re
from collections import OrderedDict
import pandas as pd
import sys

notFoundWords = []
wordList = {}

with open(sys.argv[1]) as textFile, open('words.txt') as dictionaryFile:

    dictionary = {x[:-1].lower() for x in dictionaryFile}

    for line in textFile:
        for word in re.split(r'\W|\d', line):
            if word:
                if word in wordList:
                    wordList.update({word: wordList[word]+1})
                else:
                    wordList.update({word: 1})
                if not word.lower() in dictionary and word.lower() not in notFoundWords:
                    notFoundWords.append(word.lower())


wordListNumOrd = OrderedDict(
    sorted(wordList.items(), key=lambda t: t[1], reverse=True))

wordListAlphaOrd = OrderedDict(
    sorted(wordList.items()))

numberOrdFile_df = pd.DataFrame.from_dict(wordListNumOrd, orient="index")
numberOrdFile_df.to_csv("output/wordListNumOrd.csv")
alphaOrdFile_df = pd.DataFrame.from_dict(wordListAlphaOrd, orient="index")
alphaOrdFile_df.to_csv("output/wordListAlphaOrd.csv")

with open("output/NotFoundWords.txt", 'w+') as NotFoundFile:

    for i in notFoundWords:
        NotFoundFile.write(i+'\n')
