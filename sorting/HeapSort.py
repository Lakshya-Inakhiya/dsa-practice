import random
def heap_down(a,i , n):#O(logN)
    # n = len(a)
    while True:
        l = 2*i + 1
        r = 2*i + 2
        lar = i
        if l < n and a[l] > a[lar]:
            lar = l
        if r < n and a[r] > a[lar]:
            lar = r
        if lar == i:
            break
        a[lar] , a[i] = a[i] , a[lar]
        i = lar

def build_heap(a):#O(n)
    n = len(a)
    for i in range( n//2 - 1 , -1 , -1):
        heap_down(a,i,n)


def heap_sort(a):#O(NlogN)
    n = len(a)
    build_heap(a)

    for i in range(n-1 , 0 , -1):
        a[0] , a[i] = a[i] , a[0]
        heap_down(a,0,i)

    return a

if __name__ == "__main__":
    nums = [random.randint(1, 100) for _ in range(random.randint(5, 10))]
    print(nums[:] ,"->",heap_sort(nums))