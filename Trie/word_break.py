class Trie:

    def __init__(self):

        self.children = [None]*26
        self.isLeaf = False


class TrieNode:

    def __init__(self):
        self.root = self.getNode()

    
    def getNode(self):
        
        return Trie()

    
    def _charToIndex(self,ch):

        return ord(ch)-ord('a')

    
    def insert(self,key):
        pCrawl = self.root
        length = len(key)

        for i in range(length):

            index = self._charToIndex(key[i])

            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()

            
            pCrawl = pCrawl.children[index]

        
        pCrawl.isLeaf = True

    def search(self,root,key):
        pCrawl = self.root
        length = len(key)

        for i in range(length):
            index = self._charToIndex(key[i])

            if not pCrawl.children[index]:
                return False

            pCrawl = pCrawl.children[index]

        return pCrawl.isLeaf

def wordBreak(string,root):
    n = len(string)

    if n == 0:
        return True

    for i in range(1,n+1):
        if(root.search(root,string[:i]) and   wordBreak(string[i:],root)):
            return True
    return False


def utility(s,wordDict):
    root = TrieNode()

    for w in wordDict:
        root.insert(w)

    out = wordBreak(s, root)
    
    if(out):
        return "Yes"
    else:
        return "No"

if __name__ == "__main__":
    print(utility("thequickbrownfox", ["the", "quick", "fox"]))


    