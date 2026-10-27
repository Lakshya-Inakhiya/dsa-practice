def rem_dup(arr):
    if not arr:
        return arr, 0
    i = 0
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
    return arr, i + 1

if __name__ == "__main__":
    nums = [0, 1, 2 , 3 , 4 , 4 , 4 , 4 , 5 , 7 , 8 ,8 ,9]
    print(rem_dup(nums))


def min_heap_up(a,i):
    while i>0:
        p = (i-1)//2
        if a[i] >= a[p]:
            break
        a[i] , a[p] = a[p] , a[i]
        i = p

def min_heap_insert(a, x):
    i = len(a)
    a.append(x)
    min_heap_up(a,i)

def min_heap_down(a , i):
    n = len(a)
    
    while True:
        l = 2*i + 1
        r = 2*i + 2
        s = i
        if l<n and a[l] < a[s]:
            s = l
        if r<n and a[r] < a[s]:
            s = r
        if s == i:
            break
        a[i] , a[s] = a[s] , a[i]
        i = s

def extract_min(a):
    n = len(a)
    if n == 0:
        return "Empty Heap"
        
    a[0] , a[n-1] = a[n-1] , a[0]
    _min = a.pop()
    min_heap_down(a , 0)
    return _min
    
def build_min_heap(a):
    n = len(a)
    p = n//2 - 1
    for i in range( p , -1 , -1):
        min_heap_down(a , i)