def ParenthesisBalancing(s: str) -> bool:#O(n)
    # KeepOnlyBracketsThenEarlyParityCheck.
    b = [c for c in s if c in '()[]{}']
    if len(b) % 2: return False

    # MapOpenToExpectedClose.
    dic = {'(': ')', '[': ']', '{': '}'}
    stack = []
    for c in b:
        if c in dic:                      # OpeningBracket.
            stack.append(dic[c])          # PushExpectedCloser.
        elif c in (')', ']', '}'):        # OnlyCareAboutBracketClosers.
            if not stack or stack.pop() != c:
                return False
        # IgnoreNonBracketChars.
    return not stack


if __name__ == "__main__":
    print(ParenthesisBalancing("(())"))