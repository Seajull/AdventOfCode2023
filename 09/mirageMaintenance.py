import sys, re, os
import math

def partOne(inpu) :
    with open(inpu,'r') as inp :
        al=[]
        for i in inp :
            isp=[int(x) for x in i[:-1].split(" ")]
            ori=list(isp)
            stH=[]
            while len(set(isp)) > 1 :
                c=0
                newL=[]
                while c<len(isp)-1 :
                    newL.append(isp[c+1]-isp[c])
                    c+=1
                stH.append(newL[-1])
                isp=newL
            al.append(sum(stH)+ori[-1])
    return sum(al)


print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

def partTwo(inpu) :
    with open(inpu,'r') as inp :
        al=[]
        for i in inp :
            isp=[int(x) for x in i[:-1].split(" ")]
            isp.reverse()
            ori=list(isp)
            stH=[]
            while len(set(isp)) > 1 :
                c=0
                newL=[]
                while c<len(isp)-1 :
                    newL.append(isp[c+1]-isp[c])
                    c+=1
                stH.append(newL[-1])
                isp=newL
            al.append(sum(stH)+ori[-1])
    return sum(al)

print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
print()


