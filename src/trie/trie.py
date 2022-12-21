
class TrieNode:
    """A node in the trie structure"""

    def __init__(self, char):
        self.char = char
        self.children = {}
        self.counter = 0 
        self.is_end = False

class Trie:
    '''
    This function creates a Trie data structure which uses TrieNode as nodes.
    '''
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, words):
        '''
        Insert words to trie-datastructure.
        '''
        node = self.root

        for word in words:
            if word in node.children:
                node = node.children[word]
                node.counter+=1
            else:
                new_node = TrieNode(word)
                node.children[word] = new_node
                node = new_node
                node.counter+=1

        node.is_end = True