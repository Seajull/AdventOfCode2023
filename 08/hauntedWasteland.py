import sys, re, os
import math

def partOne(inpu) :
    with open(inpu,'r') as inp :
        f=0
        dM={}
        for i in inp :
            if f==0 :
                f=1
                ins=i[:-1]
            elif i=="\n" :
                continue
            else :
                node=i.split(" = ")[0]
                res=re.findall("\w+",i[:-1].split(" = ")[1])
                dM[node]=res
        cNode="AAA"
        b=0
        step=0
        while cNode!="ZZZ" :
            for l in ins :
                step+=1
                if l=="L" :
                    b=0
                else :
                    b=1
                cNode=dM[cNode][b]
    return step
    


print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

def partTwo(inpu) :
    with open(inpu,'r') as inp :
        f=0
        dM={}
        for i in inp :
            if f==0 :
                f=1
                ins=i[:-1]
            elif i=="\n" :
                continue
            else :
                node=i.split(" = ")[0]
                res=re.findall("\w+",i[:-1].split(" = ")[1])
                dM[node]=res
        b=0
        length=[]
        lStart=[]
        for i in dM :
            if i[-1]=="A" :
                lStart.append(i)
        for lc in lStart : 
            node=lc
            step=0
            while node[-1]!="Z" :
                for l in ins :
                    step+=1
                    if l=="L" :
                        b=0
                    else :
                        b=1
                    node=dM[node][b]
            length.append(step)
    return math.lcm(*length)


print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
print()


