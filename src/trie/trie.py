
class TrieNode:
    """A node in the trie structure"""

    def __init__(self, char):
        self.char = char
        self.children = {}
        self.counter = 0 
        self.is_end = False

class Trie:
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

        '''
        This function calculates the probabilities of each node by using TrieNode class counter attribute. 
        '''
        
        next_states_from_root = self.root.children.values()
        stack = []
        total_probability = 0

        for x in next_states_from_root:
            stack.append(x)
            total_probability += x.counter
                
        for y in next_states_from_root:
            y.counter = float(y.counter)/float(total_probability)

        
        #Stackissa nyt eka, katsotaan montako lasta > Update probs
        
        while len(stack):
            #Eka
            current = stack.pop(0)
            total_prob = 0
            
            for x in current.children.values():
                # käydään läpi ekan lapset lasketaan total prob
                total_prob += x.counter
                #lisätään stackkiin naapurit
                stack.insert(0,x)

            for y in current.children.values():
              #  print(total_prob)
                y.counter = y.counter/total_prob



