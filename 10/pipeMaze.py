import sys, re, os
import math

def partOne(inpu) :
    with open(inpu,'r') as inp :
        mat=[]
        x=0
        for i in inp :
            mat.append([j for j in i[:-1]])
            if "S" in i : 
                s=(x,i.index("S"))
            x+=1
#    for k in mat :
#        print(" ".join(k))
#    print()
    size=0
    maxx=x-1
    maxy=len(mat[0])-1
    xs=s[0]
    ys=s[1]
    top=[xs-1,ys]
    right=[xs,ys+1]
    bottom=[xs+1,ys]
    left=[xs,ys-1]
    n=[mat[top[0]][top[1]],mat[right[0]][right[1]],mat[bottom[0]][bottom[1]],mat[left[0]][left[1]]]
    if xs==0 :
        n=["",mat[right[0]][right[1]],mat[bottom[0]][bottom[1]],mat[left[0]][left[1]]]
    if xs==maxx:
        n=[mat[top[0]][top[1]],mat[right[0]][right[1]],"",mat[left[0]][left[1]]]
    if ys==0 :
        n=[mat[top[0]][top[1]],mat[right[0]][right[1]],mat[bottom[0]][bottom[1]],""]
    if ys==maxy :
        n=[mat[top[0]][top[1]],"",mat[bottom[0]][bottom[1]],mat[left[0]][left[1]]]

    co=0
    nex=""
    while co<4 :
        if co==0:
            if n[co] in ["|","F","7"] :
                nex=top
                break
        elif co==1 :
            if n[co] in ["-","J","7"] :
                nex=right
                break
        elif co==2 :
            if n[co] in ["J","|","L"] :
                nex=bottom
                break
        elif co==3 :
            if n[co] in ["-","F","L"] :
                nex=left
                break
        co+=1
    cur=""
    cc=[xs,ys]
    step=0

    while cur!="S" :

        if cc[0]<nex[0] :
            sens=2
        elif cc[0]>nex[0] :
            sens=0
        elif cc[1]<nex[1] :
            sens=1
        elif cc[1]>nex[1] :
            sens=3
        cc=nex
        if cur=="-" :
            if sens==1 :
                nex=[nex[0],nex[1]+1]
            elif sens==3 :
                nex=[nex[0],nex[1]-1]
        if cur=="F":
            if sens==0 :
                nex=[nex[0],nex[1]+1]
            elif sens==3 :
                nex=[nex[0]+1,nex[1]]
        if cur=="|" :
            if sens==0 :
                nex=[nex[0]-1,nex[1]]
            elif sens==2 :
                nex=[nex[0]+1,nex[1]]
        if cur=="J" :
            if sens==1 :
                nex=[nex[0]-1,nex[1]]
            elif sens==2 :
                nex=[nex[0],nex[1]-1]
        if cur=="7" :
            if sens==1 :
                nex=[nex[0]+1,nex[1]]
            elif sens==0 :
                nex=[nex[0],nex[1]-1]
        if cur=="L" :
            if sens==3 :
                nex=[nex[0]-1,nex[1]]
            elif sens==2 :
                nex=[nex[0],nex[1]+1]
        cur=mat[nex[0]][nex[1]]
        step+=1
    return int(step/2)


print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

def partTwo(inpu) :
    with open(inpu,'r') as inp :
        mat=[]
        x=0
        for i in inp :
            mat.append([j for j in i[:-1]])
            if "S" in i : 
                s=(x,i.index("S"))
            x+=1
#    for k in mat :
#        print(" ".join(k))
#    print()
    size=0
    maxx=x-1
    maxy=len(mat[0])-1
    xs=s[0]
    ys=s[1]
    top=[xs-1,ys]
    right=[xs,ys+1]
    bottom=[xs+1,ys]
    left=[xs,ys-1]
    n=[mat[top[0]][top[1]],mat[right[0]][right[1]],mat[bottom[0]][bottom[1]],mat[left[0]][left[1]]]
    if xs==0 :
        n=["",mat[right[0]][right[1]],mat[bottom[0]][bottom[1]],mat[left[0]][left[1]]]
    if xs==maxx:
        n=[mat[top[0]][top[1]],mat[right[0]][right[1]],"",mat[left[0]][left[1]]]
    if ys==0 :
        n=[mat[top[0]][top[1]],mat[right[0]][right[1]],mat[bottom[0]][bottom[1]],""]
    if ys==maxy :
        n=[mat[top[0]][top[1]],"",mat[bottom[0]][bottom[1]],mat[left[0]][left[1]]]
    truS=""
    if n[0] in ["7","|","F"] and n[1] in ["J","7","-"] :
        truS="L"
    elif n[0] in ["7","|","F"] and n[2] in ["J","|","L"] :
        truS="|"
    elif n[0] in ["7","|","F"] and n[3] in ["-","F","L"] :
        truS="J"
    elif n[1] in ["J","7","-"] and n[2] in ["J","|","L"] :
        truS="F"
    elif n[1] in ["J","7","-"] and n[3] in ["-","F","L"] :
        truS="-"
    elif n[2] in ["J","|","L"] and n[3] in ["-","F","L"] :
        truS="7"
    co=0
    nex=""
    while co<4 :
        if co==0:
            if n[co] in ["|","F","7"] :
                nex=top
                break
        elif co==1 :
            if n[co] in ["-","J","7"] :
                nex=right
                break
        elif co==2 :
            if n[co] in ["J","|","L"] :
                nex=bottom
                break
        elif co==3 :
            if n[co] in ["-","F","L"] :
                nex=left
                break
        co+=1
    cur=""
    cc=[xs,ys]
    step=0
    dicN={tuple(cc):mat[xs][ys]}
    while cur!="S" :

        if cc[0]<nex[0] :
            sens=2
        elif cc[0]>nex[0] :
            sens=0
        elif cc[1]<nex[1] :
            sens=1
        elif cc[1]>nex[1] :
            sens=3
        cc=nex
        if cur=="-" :
            if sens==1 :
                nex=[nex[0],nex[1]+1]
            elif sens==3 :
                nex=[nex[0],nex[1]-1]
        if cur=="F":
            if sens==0 :
                nex=[nex[0],nex[1]+1]
            elif sens==3 :
                nex=[nex[0]+1,nex[1]]
        if cur=="|" :
            if sens==0 :
                nex=[nex[0]-1,nex[1]]
            elif sens==2 :
                nex=[nex[0]+1,nex[1]]
        if cur=="J" :
            if sens==1 :
                nex=[nex[0]-1,nex[1]]
            elif sens==2 :
                nex=[nex[0],nex[1]-1]
        if cur=="7" :
            if sens==1 :
                nex=[nex[0]+1,nex[1]]
            elif sens==0 :
                nex=[nex[0],nex[1]-1]
        if cur=="L" :
            if sens==3 :
                nex=[nex[0]-1,nex[1]]
            elif sens==2 :
                nex=[nex[0],nex[1]+1]
        cur=mat[nex[0]][nex[1]]
        if tuple(nex) not in dicN :
            dicN[tuple(nex)]=cur
        step+=1
    toChek=[]
    minx=min([x[0] for x in dicN.keys()])
    maxx=max([x[0] for x in dicN.keys()])
    miny=min([x[1] for x in dicN.keys()])
    maxy=max([x[1] for x in dicN.keys()])
    x=minx
    while x <= maxx :
        y=miny
        if x==minx or x==maxx :
            x+=1 
            continue
        while y <= maxy :
            if y==miny or y==maxy :
                y+=1 
                continue
            if (x,y) not in dicN.keys(): 
                toChek.append([x,y])
            y+=1
        x+=1
    nin=0
    for i in toChek :
        nin+=nleft(i,dicN,miny,truS)
    return nin


def nleft(coord,dic,my,truS) :
    y=coord[1]
    ll=[]
    while y>my : 
        y-=1
        if (coord[0],y) not in dic :
            continue
        ll.append(dic[(coord[0],y)])
    if "S" in ll :
        ll[ll.index("S")]=truS
    nj=ll.count("J")
    nf=ll.count("F")
    n7=ll.count("7")
    nl=ll.count("L")
    np=ll.count("|")
    if nj>0 and nf>0 : 
        np+=min(nj,nf)
    if n7>0 and nl>0 :
        np+=min(n7,nl)
    return np%2

# need to determine what S is to add to count

print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
print()


