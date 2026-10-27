# Bruteforce counting
def bcount(a,t): #O(N)
    c = 0
    for i in a:
        if i == t:
            c += 1
    return c

a = [1,2,1,3,2]
print(bcount(a , 2))

# Hashing : pre storing/fetching

# Not feasible for greater N like 10^9
# assuming max value in the array can be 12
hash = [ 0 for _ in range(13)]
for i in a:
    hash[i] += 1

def hcount(t):
    try:
        if t>=0:
            return hash[t]
        else:
            return 0
    except(IndexError):
        return 0

print(hcount(2))

#HashMap

hmap = dict()
# for i in a:
#     hmap[i] = hmap.get(i,0) + 1

def hmcount(t):
    return hmap.get(t , 0)

print(hmcount(2))

def hmapmax(hmap):
    if not hmap:
        return None
    bi , bc = -1, -1

    for i , v in hmap.items():
        if v > bc:
            bi = i
            bc = v

    return bi , bc

print(hmapmax(hmap))