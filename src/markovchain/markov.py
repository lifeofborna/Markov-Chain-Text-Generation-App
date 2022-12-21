from trie import trie
import random
import time

def construct_markov_model(txt,ngram,limit,word):
    '''
    This function constructs the markov model by creating a graph 
    and calculating its probabilities then printing the results. 
    '''

    graph = create_graph_with_ngram(txt,ngram)

    if word == None:
        generate_text(graph,limit)
    else:
        generate_text(graph,limit,word.lower())




def generate_text(graph: trie, limit, word=""):
    """
    This function generates text when given a trie datastructure
    """
    # Generate all the sentences at once, store them in a list
    generated_texts = []

    for i in range(1, 21):
        if word != "":
            try:
                current_node = graph.root.children[word]
            except:
                print("The word you tried using is not a state! Please try again.")
                return
            
            generated_text = word+" "
        else:
            current_node = graph.root        
            generated_text = ""

        for y in range(0, limit):
            weights = [x.counter for x in current_node.children.values()]

            # If we have received to the end --> start from the last node.
            if current_node.is_end:
                current_node = graph.root.children[current_node.char]
                continue

            # Pick the next node randomly via random.choices
            next_node = random.choices(list(current_node.children.values()), weights, k=1)[0]

            generated_text += f"{next_node.char} "
            current_node = next_node

        generated_texts.append(generated_text)

    # Print the sentences
    for i in range(len(generated_texts)):
        generated_text = generated_texts[i]
        print(f"{i + 1}. {generated_text}")








def create_graph_with_ngram(txt, ngram):

    '''
     Initialized the trie datastructure when given the cleaned text.  
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


    