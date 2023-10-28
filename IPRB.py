path = "datasets/test.txt"
path = "datasets/rosalind_iprb.txt"
from math import *

with open(path) as file:
    x = file.read()
inp_list = x.rstrip().split(" ")

def model(inp_list,out):
    k = int(inp_list[0])
    m = int(inp_list[1])
    n = int(inp_list[2])
    tot = k + m + n
    tot_opt = comb(tot,2)
    a = {"AA" : 1}
    b = {"BB": 1}
    h = {"AA":0.25, "AB": 0.5, "BB": 0.25}
    ab = {"AB":1}
    ah = {"AA": 0.5, "AB": 0.5}
    bh = {"BB": 0.5, "AB":0.5}

    list = []
    dom = []
    rec = []

    for i in range(comb(k,2)):
        list.append(a)
    for i in range(comb(m,2)):
        list.append(h)
    for i in range(comb(n,2)):
        list.append(b)
    for i in range(k*m):
        list.append(ah)
    for i in range(k*n):
        list.append(ab)
    for i in range(m*n):
        list.append(bh)

    for poss in list:
        for gt in poss:
            if "A" in gt:
                dom.append(poss[gt]*(1/tot_opt))
            elif "BB" in gt:
                rec.append(poss[gt]*(1/tot_opt))

    if out == 1:
        return round(sum(dom), 5)
    elif out == 0:
        return round(sum(rec), 5)
    else:
        return "Please, choose only 1 or 0"


print(model(inp_list,1))
