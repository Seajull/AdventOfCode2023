import sys, re, os

def partOne(inpu) :
    with open(inpu,'r') as inp :
        di={"green":13,"red":12,"blue":14}
        count=0
        goo=True
        for i in inp : 
            res=re.search("Game (\d+):",i) 
            gamid=int(res.group(1))
            res=re.findall("(((\d+) blue|(\d+) red|(\d+) green))+",i)
            for j in res :
                isp=j[0].split(" ")
                if int(isp[0])>di[isp[1]] :
                    goo=False 
            if goo :
                count+=gamid
            else :
                goo=True
    return count

print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

def partTwo(inpu) :
    with open(inpu,'r') as inp :
        count=0
        for i in inp : 
            di={}
            res=re.search("Game (\d+):",i) 
            gamid=int(res.group(1))
            res=re.findall("(((\d+) blue|(\d+) red|(\d+) green))+",i)
            for j in res :
                isp=j[0].split(" ")
                if isp[1] not in di :
                    di[isp[1]]=[int(isp[0])]
                else :
                    di[isp[1]].append(int(isp[0]))
            l=[]
            for k in di.values() :
                l.append(max(k))
            count+=l[0]*l[1]*l[2]
    return count

print("==> PART TWO <==")
print(partTwo(sys.argv[1]))


