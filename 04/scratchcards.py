import sys, re, os

def partOne(inpu) :
    with open(inpu,'r') as inp :
        total=0
        for i in inp :
            count=0
            i=i.split(":")[1]
            isp=i[:-1].split(" | ")
            win=re.findall("\d+",isp[0])
            num=re.findall("\d+",isp[1])
            for c in num :
                if c in win :
                    if count==0 :
                        count+=1
                    else :
                        count=count*2
            total+=count
    return total

print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

def partTwo(inpu) :
    hand={1:1}
    with open(inpu,'r') as inp :
        for i in inp :
            count=0
            ip=i.split(":")
            isp=ip[1][:-1].split(" | ")
            win=re.findall("\d+",isp[0])
            num=re.findall("\d+",isp[1])
            cur=int(ip[0].split(" ")[-1])
            for c in num :
                if c in win :
                    count+=1
            if cur not in hand :
                hand[cur]=1
            if count>0 :
                n=0
                while n<count :
                    if cur+n+1 not in hand :
                        hand[cur+n+1]=1+(1*hand[cur])
                    else :
                        hand[cur+n+1]+=1*hand[cur]
                    n+=1
    return sum(list(hand.values()))

print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
print()


