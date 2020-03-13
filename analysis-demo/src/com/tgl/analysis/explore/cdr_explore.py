import requests

import os
import re


with open("C:/Users/Administrator/Downloads/20200304001038-log-2020-03-04.00-10-37.log") as file_obj:
    for line in file_obj:
        if line.find("sessionid: \"127aaaa0b00049e394beaa9c0ed991b6\"uploadFlowsizeReq")>=0 :
            nlist = line.split(" ")

            print(nlist[nlist.index("ufId:")+1]+","+nlist[nlist.index("flowSizeup:")+1]+","+nlist[nlist.index("flowSizedown:")+1])





#list=[i.start() for i in re.finditer('\\\\', 'C:\\Users\\aaa\\computer\\flicker\\01213.jpg')]
#print(list)