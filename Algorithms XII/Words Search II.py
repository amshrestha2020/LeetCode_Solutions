Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.





class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build a Trie out of the list of words
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word

        # List to store the words found on the board
        result = []

        # Function to perform DFS on the board
        def dfs(i, j, node):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] not in node.children:
                return
            char = board[i][j]
            node = node.children[char]
            if node.word:
                result.append(node.word)
                node.word = None  # Ensure the word is only added once
            board[i][j] = '#'  # Mark the cell as visited
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(i + dx, j + dy, node)
            board[i][j] = char  # Reset the cell

        # Perform DFS on each cell of the board
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, root)

        return result
