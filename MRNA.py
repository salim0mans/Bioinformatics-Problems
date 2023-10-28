path = "datasets/test.txt"
path = "datasets/rosalind_mrna.txt"

code = {"A": ["GCU", "GCC", "GCA", "GCG"], "V": ["GUU", "GUA", "GUC", "GUG"],
        "I": ["AUU", "AUC", "AUA"], "M": ["AUG"],
        "L": ["CUU", "CUC", "CUG", "CUA", "UUA", "UUG"], "F": ["UUU", "UUC"],
        "S": ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"], "P": ["CCU", "CCC", "CCA", "CCG"],
        "T": ["ACU", "ACA", "ACC", "ACG"], "E": ["GAA", "GAG"],
        "D": ["GAU", "GAC"], "N": ["AAU", "AAC"],
        "K": ["AAA", "AAG"], "Q": ["CAA", "CAG"],
        "H": ["CAU", "CAC"], "Y": ["UAU", "UAC"],
        "C": ["UGU", "UGC"], "W": ["UGG"],
        "R": ["CGA", "CGC", "CGU", "CGG", "AGA", "AGG"], "G": ["GGU", "GGC", "GGA", "GGG"],
        "STOP": ["UGA", "UAA", "UAG"]}
aa = "ACDEFGHIKLMNPQRSTVWY"


def mrna(path):
    count = {}
    total = []
    final = []
    for key in sorted(code):
        count[key] = len(code[key])

    with open(path) as file:
        for line in file:
            for i in line.rstrip():
                if i in count:
                    total.append(count[i])
                else:
                    return " ".join(["Error, a.a. not identified at position: ", str(line.index(i)+1),i])
    res = 1
    for i in total:
        res *= i
    return (res % 1000000)*3


print(mrna(path))
###For some strange reason, the answer is only last 6 digits
