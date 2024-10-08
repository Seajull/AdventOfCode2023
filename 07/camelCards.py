import sys, re, os
import math

def partOne(inpu) :
    order=["A","K","Q","J","T","9","8","7","6","5","4","3","2"]
    order.reverse()
    hand=["5","14","23","113","122","1112","11111"]
    hand.reverse()
    lHand=[]
    with open(inpu,'r') as inp :
        dSet={0:[],1:[],2:[],3:[],4:[],5:[],6:[]}
        for i in inp :
            dType={}
            isp=i[:-1].split(" ")
            for c in isp[0]:
                if c not in dType :
                    dType[c]=1
                else :
                    dType[c]+=1
            ht=sorted(list(dType.values()))
            ht="".join([str(x) for x in ht])
            cardValue=int("".join([str(order.index(x)+10) for x in isp[0]]))
            bid=int(isp[1])
            if ht in hand :
                dSet[hand.index(ht)].append((cardValue,bid))
        for i in dSet :
            if dSet[i]:
                dSet[i].sort()
                for h in dSet[i] :
                    lHand.append(h[1])
        c=0
        win=0
        while c<len(lHand) :
            win+=lHand[c]*(c+1)
            c+=1
    return win


print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

def partTwo(inpu) :
    order=["A","K","Q","T","9","8","7","6","5","4","3","2","J"]
    order.reverse()
    hand=["5","14","23","113","122","1112","11111"]
    hand.reverse()
    lHand=[]
    with open(inpu,'r') as inp :
        dSet={0:[],1:[],2:[],3:[],4:[],5:[],6:[]}
        for i in inp :
            dType={}
            isp=i[:-1].split(" ")
            if isp[0]=="JJJJJ":
                ht="5"
            else :
                nJ=0
                for c in isp[0]:
                    if c=="J" :
                        nJ+=1
                        continue
                    if c not in dType :
                        dType[c]=1
                    else :
                        dType[c]+=1
                mv=max(list(dType.values()))
                ht=list(dType.values())
                ht[ht.index(mv)]=mv+nJ
                ht.sort()
                ht="".join([str(x) for x in ht])
            cardValue=int("".join([str(order.index(x)+10) for x in isp[0]]))
            bid=int(isp[1])
            if ht in hand :
                dSet[hand.index(ht)].append((cardValue,bid))
        for i in dSet :
            if dSet[i]:
                dSet[i].sort()
                for h in dSet[i] :
                    lHand.append(h[1])
        c=0
        win=0
        while c<len(lHand) :
            win+=lHand[c]*(c+1)
            c+=1
    return win

print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
print()


