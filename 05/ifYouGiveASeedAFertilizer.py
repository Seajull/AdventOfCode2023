import sys, re, os

def partOne(inpu) :
    with open(inpu,'r') as inp :
        for i in inp :
            if "seeds" in i :
                seed=re.findall("\d+",i)
                seed=[int(x) for x in seed]
    loc=[]
    with open(inpu,'r') as inp :
        for s in seed : 
            find=False
            for i in inp :
                if "seeds" in i or "seed-to-soil" in i:
                    continue
                elif "map" in i :
                    if find :
                        s=ns
                        find=False
                    continue
                elif i=="\n" :
                    continue
                ma=re.findall("\d+",i)
                ma=[int(x) for x in ma]
                if s in range(ma[1],ma[1]+ma[2]) :
                    find=True
                    ns=range(ma[0],ma[0]+ma[2])[range(ma[1],ma[1]+ma[2]).index(s)]
            loc.append(ns)
            inp.seek(0)
    return min(loc)

print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

def partTwo(inpu) :
    with open(inpu,'r') as inp :
        for i in inp :
            if "seeds" in i :
                seed=re.findall("\d+",i)
                seed=[int(x) for x in seed]
    loc=[]
    c=0
    rseed=[]
    while c<len(seed) :
        rseed.append(range(seed[c],seed[c]+seed[c+1]))
        c+=2

    l=0
    for seed in rseed :
        l+=len(seed)
    print(l)
    with open(inpu,'r') as inp :
        for seed in rseed :
            for s in seed : 
                find=False
                for i in inp :
                    if "seeds" in i or "seed-to-soil" in i:
                        continue
                    elif "map" in i :
                        if find :
                            s=ns
                            find=False
                        continue
                    elif i=="\n" :
                        continue
                    ma=re.findall("\d+",i)
                    ma=[int(x) for x in ma]
                    if s in range(ma[1],ma[1]+ma[2]) :
                        find=True
                        ns=range(ma[0],ma[0]+ma[2])[range(ma[1],ma[1]+ma[2]).index(s)]
                loc.append(ns)
                inp.seek(0)
    return min(loc)

print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
print()


