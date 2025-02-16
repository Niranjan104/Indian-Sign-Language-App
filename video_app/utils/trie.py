class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.video_filename = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, filename):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.video_filename = filename

    def search(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node.video_filename if node.is_end_of_word else None