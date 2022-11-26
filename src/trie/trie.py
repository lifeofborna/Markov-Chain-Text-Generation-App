class TrieNode:
    """A node in the trie structure"""

    def __init__(self, char):
        # the character stored in this node
        self.char = char
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode("")
    
    def insert(self, curr_state, next_state):
        node = self.root

        #Make a new node, add to children of root, add successor
        if curr_state not in node.children.keys():
            new_node = TrieNode(curr_state)
            node.children[curr_state] = {}
            node.children[curr_state][next_state] = 1
            new_node.children[next_state] = 1
        else:
            node = node.children[curr_state]
            if next_state not in node.keys():
                new_node = TrieNode(next_state)
                node[next_state] = 1
            else:
                node[next_state] += 1
    
    def search(self):
        return self.root.children
        