path = "datasets/rosalind_fibd.txt"
with open(path) as file:
    x = file.read()
print(x)

def fibo(n):
    li = [1,1]
    for i in range(2,n):
        li.append(li[i-1]+li[i-2])
    return li

def sub(li):
    subtr = [0]
    for i in range(1,len(li)):
        subtr.append(li[i]-li[i-1])
    return subtr

def mortrab(n,m):
    fib = fibo(m)
    x = sub(fib)
    for i in range(m,n):
        x.append(sum(x[i-m:i-1]))
        fib.append(fib[i-1] + x[i])
    return fib[n-1]

print(mortrab(86,18))


##YEEAAAAAAAH BABY!!! and I am freakin Cool

##Let's coin some concepts.. I will call the number of months the rabbit lives Survival Limit (m).. and the total of months Total Period (n)
##Subtraction list (SUB(li)) is the list of differences between elements of another list.. ex. SUB([1,1,2,7,15,20] is [0,1,5,8,5]
##I found that every mortal rabbit sequence with survival limit m:
# (1) it starts with m elements same as normal fibonacci, I will call them starter elements
# (2) after starter elements, if we see create a SUB of the sequence, we find that each element in the SUB equals sum of (m-1) elements before the previous one
##ex. the seq with m = 3 is [1,1,2,2,3,4,5,7,9,12..] so its SUB is [0,1,0,1,1,1,2,2,3,..]... notice that SUB[4] == SUB[1]+SUB[2] and SUB[7] == SUB[4]+SUB[5]
##So each element is the sum of 3-1 = 2 elements before previous one.. I don't understand why, but it appears to be a pattern..
# so for m = 5... each element starting from element 5 in the SUB of the seq equals sum of last 4 elements before the previous one..
#Of course we can deduce the rest of the sequence from the SUB.. as: Seq[i]==Seq[i-1]+SUB[i].. because in the first place, seq[i]-seq[i-1] is SUB[i]
#So... that's how I made the model for whatever survival limit for rabbits... It can be extended to k pairs born not just 1 pair as in normal fibonacci
