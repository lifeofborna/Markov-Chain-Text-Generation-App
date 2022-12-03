from trie import trie
import random
import time
from collections import deque 

def construct_markov_model(txt,ngram,limit=12):
    '''
    This function constructs the markov model by creating a graph 
    and calculating its probabilities then printing the results. 
    '''

    graph = create_graph_with_ngram(txt,ngram)

    alku = time.time()
    graph.calculate_probabilities()
    loppu = time.time()

    print("--------------------------------------------------------")
    print("Aikaa kului todenäkköisyyksien luomiseen ja päivittämiseen: ", loppu-alku,)
    print("---------------------------------------------------------")
    print("")
    generate_text(graph,limit)




def generate_text(graph:trie,limit):
    '''
    This function generates text when given a trie datastructure with probabilities for next node. 
    '''
    generated_text = ""
    for i in range(1,21):
        current_node = graph.root
        generated_text = ""
        
        for y in range(0,limit):
            weights = []

            for x in current_node.children.values():
                weights.append(x.counter)


             #Jos vika = set graph.root find vika node --> jatka
            if current_node.is_end:
                current_node = graph.root.children[current_node.char]
                continue
            
            next_node = random.choices(list(current_node.children.values()),weights)[0]

            generated_text+=f"{next_node.char} "
            current_node = next_node
        
        print(f'{i}. {generated_text}')





def create_graph_with_ngram(txt, ngram):

    '''
    Creates the graph from cleaned txt and initializes trie datastructure. 
    '''

    alku = time.time()
    trie_tree = trie.Trie()
    i = 0
    while i < (len(txt)-ngram-1):
        trie_tree.insert(txt[i:i+ngram+1])
        i+=1
    
    loppu = time.time()

    print("-----------------------------------------------------------")
    print("Aikaa kului trie-treen muodostamiseen: ", loppu-alku,)
    print("------------------------------------------------------------")
    print("")
    return trie_tree


    