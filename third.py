class TrieNode:

    def __init__(self, ch: str):
        self.ch = ch
        self.nxt = {}
        self.is_end = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode('#')

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        WordDictionary.build_trie(word, 0, self.root)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return WordDictionary.recursion(word, 0, self.root)

    @staticmethod
    def recursion(word: str, i: int, node: TrieNode) -> bool:
        if i == len(word):
            return True if node.is_end else False
        if word[i] == '.':
            res = False
            for key in node.nxt.keys():
                res = res or WordDictionary.recursion(word, i + 1, node.nxt[key])
            return res
        else:
            return False if word[i] not in node.nxt else WordDictionary.recursion(word, i + 1, node.nxt[word[i]])

    @staticmethod
    def build_trie(word: str, i: int, node: TrieNode):
        if i == len(word):
            node.is_end = True
            return
        if word[i] not in node.nxt:
            node.nxt[word[i]] = TrieNode(word[i])
        WordDictionary.build_trie(word, i + 1, node.nxt[word[i]])



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)