path = "datasets/test.txt"
path = "datasets/rosalind_subs.txt"

def motif(path):
    with open(path) as file:
        lines = [line.rstrip() for line in file]
    dna = lines[0]
    n = len(dna)
    pat = lines[1]
    k = len(pat)
    pos = []
    for i in range(n-k+1):
        if pat == dna[i:i+k]:
            pos.append(str(i+1))
    return " ".join(pos)
print(motif(path))
