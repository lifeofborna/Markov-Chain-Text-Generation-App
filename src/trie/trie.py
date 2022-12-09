
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


    def calculate_probabilities(self):
        
    # This function calculates the probabilities of each node in a trie
    # by using the TrieNode class counter attribute.

        def calculate_node_probabilities(node, total_prob):
            # Calculate the probabilities of each child node.
            for child in node.children.values():
                child.counter = child.counter / total_prob
                calculate_node_probabilities(child, total_prob)


        # Check if the trie is empty or has no children.
        if not self.root or not self.root.children:
            return

        # Calculate the total probability of the root node's children.
        total_prob = 0
        for child in self.root.children.values():
            total_prob += child.counter

        # Calculate the probabilities of each child node.
        for child in self.root.children.values():
            child.counter = child.counter / total_prob
            calculate_node_probabilities(child, total_prob)