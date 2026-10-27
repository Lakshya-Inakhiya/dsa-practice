def IsomorphicStrings(x: str, y: str) -> bool:#O(n)
    if len(x) != len(y):
        return False
    fwd, rev = {}, {}
    for (a, b) in zip(x, y):
        if a in fwd and fwd[a] != b:
            return False
        if b in rev and rev[b] != a:
            return False
        fwd[a] = b
        rev[b] = a
    return True

if __name__ == "__main__":
    print(IsomorphicStrings("add" ,"egg"))


