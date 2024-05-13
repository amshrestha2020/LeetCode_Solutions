Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
 

Constraints:

1 <= word.length <= 25
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 2 dots in word for search queries.
At most 104 calls will be made to addWord and search.




class TrieNode:
    def __init__(self):
        self.children = [None]*26  # For 26 lowercase English letters
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.is_word = True

    def search(self, word: str) -> bool:
        return self.searchFrom(self.root, word)

    def searchFrom(self, node: TrieNode, word: str) -> bool:
        for i in range(len(word)):
            ch = word[i]
            if ch == '.':
                for x in node.children:
                    if x and self.searchFrom(x, word[i+1:]):
                        return True
                return False
            else:
                index = ord(ch) - ord('a')
                node = node.children[index]
                if not node:
                    return False
        return node.is_word


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
