def exponent(n,m,res):

    if m == 0:
        return res
    
    res*= n 
    m-=1

    return exponent(n,m,res)


if __name__ == "__main__":
    n = 2
    m = 8
    res = 1

    print(exponent(n,m,res))