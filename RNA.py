path = "datasets/rosalind_rna.txt"

def rna_transc(path):
    seq = ""

    with open(path) as file:
        for line in file:
            for base in line.rstrip().upper():
                if base == "T":
                    seq += "U"
                else:
                    seq += base
    return seq

print(rna_transc(path))
