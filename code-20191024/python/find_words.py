class Solution:
    def findWords(self, board: str, words: str) -> str:
        trie = Trie()
        node = trie.root
        ret = []
        for word in words:
            trie.insert(word) 
        def print_node_rec(node):
            for w in node.children:
                print(w,end =" ")
            print(node.is_word)
            for w in node.children:
                print_node_rec(node.children[w])
        print_node_rec(node)     
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board,node,i,j,"",ret)
        return ret
    def dfs(self,board,node,i,j,path,ret):
        if node.is_word:
            ret.append(path)
            node.is_word = False
        if i<0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        
        temp = board[i][j]
        if temp in node.children:
            node = node.children[temp]
        else:
            return
        board[i][j] = "#"
        self.dfs(board,node,i+1,j,path+temp,ret)
        self.dfs(board,node,i-1,j,path+temp,ret)
        self.dfs(board,node,i,j-1,path+temp,ret)
        self.dfs(board,node,i,j+1,path+temp,ret)
        board[i][j] = temp



class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = Node()
    def insert(self,word):
        node = self.root
        for w in word:
            if w in node.children:
                node = node.children[w]
            else:
                node.children[w] = Node()
                node = node.children[w]
            
        node.is_word = True


a = Solution()
board = [["a","b"],["c","d"]]
words =["ab","cb","ad","bd","ac","ca","da","bc","db","adcb","dabc","abb","acb"]




print(a.findWords(board,words))

