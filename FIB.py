path = "datasets/rosalind_fib.txt"
with open(path) as file:
    x = file.read()
print(x)

def rabbit(n,k):
    pairs = {0:1, 1:1}
    for i in range(2,n):
        pairs[i] = pairs[i-1] + pairs[i-2]*k
    return pairs.values()

print(rabbit(5,3))
