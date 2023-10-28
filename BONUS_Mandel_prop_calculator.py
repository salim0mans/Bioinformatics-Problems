
def pheno(pat,mat,out):
    a = {"AA" : 1}
    b = {"BB": 1}
    h = {"AA":0.25, "AB": 0.5, "BB": 0.25}
    ab = {"AB":1}
    ah = {"AA": 0.5, "AB": 0.5}
    bh = {"BB": 0.5, "AB":0.5}

    geno = []
    dom = []
    rec = []
    if pat == 1 and mat == 1:
        geno = [a]
    elif pat == 0 and mat == 0:
        geno = [b]
    elif (pat == 2 and mat == 2):
        geno = [h]
    elif (pat == 1 and mat == 0) or (pat == 0 and mat == 1):
        geno = [ab]
    elif (pat == 1 and mat == 2) or (pat == 2 and mat == 1):
        geno = [ah]
    elif (pat == 0 and mat == 2) or (pat == 2 and mat == 0):
        geno = [bh]
    else:
        return "There is mistake in pat and mat, please choose (0,1,2) only"

    for poss in geno:
        for gt in poss:
            if "A" in gt:
                dom.append(poss[gt])
            elif "BB" in gt:
                rec.append(poss[gt])

    if out == 1:
        return sum(dom)
    elif out == 0:
        return sum(rec)
    else:
        return "Please, choose only 1 or 0"

##pheno(pat,mat,out)
#please choose value for each of paternal (pat) and maternal (mat) as:
### 0 if  homozygous recessive
### 1 if  homozygous dominant
### 2 if heterozygous
#please choose out as: 1 for dom, 0 for rec

print(pheno(2,2,1))
