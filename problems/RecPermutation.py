def PermutationString(s: str):#O(n*n!)
    # Base case.
    if len(s) <= 1:
        return [s]

    ans = []
    seen = set()  # SkipSameCharChoiceAtThisDepth.
    for i in range(len(s)):
        start = s[i]
        if start in seen:
            continue
        seen.add(start)
        rest = s[:i] + s[i+1:]
        smaller_perms = PermutationString(rest)
        for p in smaller_perms:
            ans.append(start + p)
    return ans

if __name__ == "__main__":
    print(PermutationString("aab"))
