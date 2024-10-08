import sys, re, os
import math

def partOne(inpu) :
    with open(inpu,'r') as inp :
        lTime=[]
        for i in inp :
            res=re.findall("\d+",i) 
            if "Time" in i :
                lTime=res
            else :
                lDist=res
                lCat=[(x,y) for x,y in zip(lTime,lDist)]
        nOk=1
        for cat in lCat :
            maxT=int(cat[0])
            mid=math.ceil(maxT/2)
            record=int(cat[1])
            sMin=(maxT-math.sqrt((maxT**2)-(4*record)))/2
            sMax=(maxT+math.sqrt((maxT**2)-(4*record)))/2
            sMin=math.ceil(sMin)
            sMax=int(sMax)
            if (maxT-sMin)*sMin==record:
                sMin+=1
            if (maxT-sMax)*sMax==record:
                sMax-=1
            nOk=nOk*(sMax-sMin+1)
    return nOk

print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

def partTwo(inpu) :
    with open(inpu,'r') as inp :
        lTime=[]
        for i in inp :
            res=re.findall("\d+",i) 
            if "Time" in i :
                lTime=res
                lTime="".join(lTime)
            else :
                lDist=res
                lDist="".join(lDist)
        nOk=1
        cat=[int(lTime),int(lDist)]
        maxT=int(cat[0])
        mid=math.ceil(maxT/2)
        record=int(cat[1])
        sMin=(maxT-math.sqrt((maxT**2)-(4*record)))/2
        sMax=(maxT+math.sqrt((maxT**2)-(4*record)))/2
        sMin=math.ceil(sMin)
        sMax=int(sMax)
        if (maxT-sMin)*sMin==record:
            sMin+=1
        if (maxT-sMax)*sMax==record:
            sMax-=1
        nOk=nOk*(sMax-sMin+1)
    return nOk

print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
print()


