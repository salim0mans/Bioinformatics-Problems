path = "datasets/test.txt"
path = "datasets/rosalind_dna.txt"
def dna_cnt(path):
    count = {}
    for i in "ACTG":
        count[i] = 0
    with open(path) as file:
        for line in file:
            for base in line.rstrip():
                count[base] += 1
    return count
print(dna_cnt(path))
