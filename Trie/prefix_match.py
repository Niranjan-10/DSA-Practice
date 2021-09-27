class Node:
    def __init__(self):
        self.arr = [None]*26
        self.freq = 0


class Trie:
    def __init__(self):
        self.root = self.getNode()

    
    def getNode(self):
        return Node()

    
    def insert(self,s):
        _in = 0
        cur = self.root

        for i in range(len(s)):
            _in = ord(s[i]) - ord('a')

            if not cur.arr[_in]:
                cur.arr[_in] = self.getNode()

            cur.arr[_in].freq +=1

            cur = cur.arr[_in]


    def find(self,s,k):
        _in = 0
        count = 0
        cur = self.root

        for i in range(len(s)):
            _in = ord(s[i]) - ord('a')

            if cur.arr[_in] == None:
                return 0

            cur = cur.arr[_in]
            count+=1

            if count == k:
                return cur.freq

        
        return 0


# Driver code
def main():
     
    arr = [ "abba", "abbb", "abbc", "abbd", "abaa", "abca" ]
    n = len(arr)
 
    root = Trie();
 
    # Insert the strings in the trie
    for i in range(n):
        root.insert(arr[i])
 
    # Query 1
    print(root.find("abbg", 3))
 
    # Query 2
    print(root.find("abg", 2))
 
    # Query 3
    print(root.find("xyz", 2))
 
if __name__ == '__main__':
    main()


