path = "datasets/rosalind_revc.txt"

def comp(path):
    seq = ""
    with open(path) as file:
        for line in file:
            for i in line.rstrip().upper():
                if i == "T":
                    seq += "A"
                elif i == "A":
                    seq += "T"
                elif i == "C":
                    seq += "G"
                elif i == "G":
                    seq += "C"
                elif i == "\n":
                    break
                else:
                    return "Error in sequence at position " + str(i)
    return seq[::-1]

print(comp(path))
