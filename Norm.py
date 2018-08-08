import os
import subprocess
import sys

folderSRT = 'C:\\Users\\repos\\7910_Subliminal\\SRT\\'

lenS1 = 22 #  1 - 22
lenS2 = 22 #  23 - 44
lenS3 = 25 #  45 - 69
lenS4 = 26 #  70 - 95
lenS5 = 26 #  96 - 121
lenS6 = 25 # 122 - 146
lenS7 = 22 # 147 - 168
lenS8 = 26 # 169 - 194
lenS9 = 27 # 195 - 221  *double episode* 
lenS10= 25 # 222 - 247 * double episode*  25/26
lenS11= 25 # 248 - 275  *triple episode* 26/27/28

s1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
s2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
s3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
s4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
s5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
s6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
s7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
s8 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
s9 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
s10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
s11 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]

def numFormat( inNum ):
    if inNum < 10:
        out = "0"+str(inNum)
    else: 
        out = str(inNum)
    return out
	
def epFormat( inEp, inSea):
    ep = numFormat(inEp)
    se = numFormat(inSea)
    return("S"+se+"E"+ep)
	
listSs = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11]

listS1 = []
listS2 = []
listS3 = []
listS4 = []
listS5 = []
listS6 = []
listS7 = []
listS8 = []
listS9 = []
listS10 = []
listS11 = []
p1 = "subliminal download -l en Cheers."
p2 = "S02E03"
p3 = ".mp4"

def makeCall(inThing):
    p1 = "subliminal download -l en Cheers."
    p2 = "S02E03"
    p3 = ".mp4"
	

for i in s1:
    listS1.append(epFormat(i, 1))

listSeasons = []
for i in [1,2,3,4,5,6,7,8,9,10,11]:
    thisSeason = []
    for j in eval("s"+str(i)):
        print(p1+epFormat(j,i)+p3)
        pO = p1+epFormat(j,i)+p3
        print(pO)
        
        #subprocess.call(dictO)
    #listSeasons.append(
	
	



