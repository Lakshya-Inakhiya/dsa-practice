def wlen(num = 7456):#O(n)
    tnum = num
    count = 0
    while tnum >0:
        tnum //= 10
        count += 1
    return f"{num} is {count} digit Number"

if __name__ == "__main__":
    print(wlen(193456789))


