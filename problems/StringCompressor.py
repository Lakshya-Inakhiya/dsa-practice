def StringCompressor(string:str)-> str:
    def RecHelper(string:str , cmpstr:str , c:int , lseen:str) ->str:
        if not string:
            return cmpstr if lseen == "" else cmpstr + lseen + str(c)
        if lseen == "":
            return RecHelper(string[1:] ,cmpstr, 1 , string[0])
        if string[0] == lseen:
            return RecHelper(string[1:] , cmpstr , c+1 , lseen)
        else:
            return RecHelper(string[1:] , cmpstr+lseen+ str(c), 1 , string[0] )
    return RecHelper(string , "" , 0 , "")
    


if __name__ =="__main__":
    string = ""
    print(StringCompressor(string))