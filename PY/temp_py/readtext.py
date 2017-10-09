#!/usr/bin/env python
# coding: utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')

file = open("raw.txt")
import pyttsx
engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',180)

print rate
stopwords = {}.fromkeys([ line.rstrip() for line in open('stopword_all.txt') ])
import jieba

while 1:
    lines = file.readlines(100000)
    if not lines:
        break
    for line in lines:

        seg_list =jieba.cut(line, cut_all=False)
        result=seg_list
        s=''
        for g in result:
            if g.encode("utf-8")==" ":
                pass
            elif g.encode("utf-8")=="\n":
                pass
            elif g.encode("utf-8")=="。":
                print s+"。"
                engine.say(s)
                engine.runAndWait()
                s=""
            else:
                s+=g+""

