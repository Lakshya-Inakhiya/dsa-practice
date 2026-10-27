def TimeConverter(oldtime): #O(1) # "HH:MM:SS" in 24h
    h, m, s = map(int, oldtime.split(":"))

    if h == 0:          # midnight hour
        suffix = "A.M."
        h = 12
    elif 1 <= h <= 11:  # morning
        suffix = "A.M."
    elif h == 12:       # noon hour
        suffix = "P.M."
    else:               # 13..23
        suffix = "P.M."
        h -= 12

    # choose padded or unpadded:
    # return f"{h}:{m}:{s} {suffix}"         # unpadded
    return f"{h:02d}:{m:02d}:{s:02d} {suffix}"  # padded

if __name__ == "__main__":
    print(TimeConverter("12:46:13"))