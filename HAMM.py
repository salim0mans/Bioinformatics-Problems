path = "datasets/rosalind_hamm.txt"
def input_qp(path):
    with open(path) as file:
        pq = []
        for line in file:
            pq.append(line.rstrip().upper())
    return pq

def hamm(path):
    p = input_qp(path)[0]
    q = input_qp(path)[1]
    n = len(p)
    count = 0
    for i in range(n):
        if p[i] != q[i]:
            count += 1
    return count

print(hamm(path))
