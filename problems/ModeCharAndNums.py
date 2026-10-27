def ModeChar(string:str):#O(n)
    if not string:
        print("\nstring = ''")
        return None, 0
    freq ={} 
    for ch in string:
        freq[ch] = freq.get(ch , 0) + 1
    seen = set()
    mode_ch = string[0]
    ch_freq = freq[mode_ch]
    for ch in string:
        if ch not in seen:
            seen.add(ch)
            if freq[ch] > ch_freq:
                ch_freq = freq[ch]
                mode_ch = ch
  
    return mode_ch,ch_freq

def ModeNum(nums: list):#O(n)
    if not nums:
        print("\nnums = ''")
        return None, 0
    freq ={}
    for num in nums:
        freq[num] = freq.get(num , 0) + 1
    seen = set()
    mode_num = nums[0]
    num_freq = freq[mode_num]
    for num in nums:
        if num not in seen:
            seen.add(num)
            if freq[num] > num_freq:
                num_freq = freq[num]
                mode_num = num    
    return mode_num ,num_freq

if __name__ == "__main__":
    string ="aabbaaa"
    nums = [ 5 , 5 , 6 , 6 , 7 , 7 , 7 , 5 , 4 , 4 , 3]
    print("")
    print(string , ModeChar(string))
    print("")
    print(nums)
    print(ModeNum(nums))
    print("")