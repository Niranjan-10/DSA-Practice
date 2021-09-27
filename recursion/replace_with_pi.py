
def replaceWithPi(string,start):

    if len(string) <2:
        return string

    if start == len(string):
        return string

    if string[start] == "p" and string[start+1] == "i" :
        string[start:start+2] = ['3','.','1','4']

    return replaceWithPi(string,start+1)




string = "pippi"
string = list(string)
res = ' '.join(replaceWithPi(string,0))
print(res)
