

def strToInt(string,res):

    if len(string) ==0:
        return res
    
    prod = 10**(len(string)-1)
    # print(prod)
    res = res+int(string[0])*prod
    # print(res)
    string.pop(0)

    return strToInt(string,res)




string = "12678"
string = list(string)
res = strToInt(string,0)
print(type(res))

