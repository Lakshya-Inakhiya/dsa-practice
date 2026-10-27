def FlattenListTuple(lst):#O(n)
    ans = []
    for v in lst:
        if isinstance(v, (list, tuple)):      # flatten both
            ans.extend(FlattenListTuple(v))
        else:
            ans.append(v)
    return ans

if __name__ == "__main__":
    print(FlattenListTuple([1 , 2 ,[3 , 4 ,[5 , 6 , 7] ,8] ,9]))
