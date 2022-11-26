from trie import trie
import random


def construct_markov_model(txt,ngram,start,limit):

    get_graph = create_graph_with_ngram(txt,ngram)
    model = get_graph_transition_probabilites(get_graph)
    
    for i in range(20):
        print(str(i)+ ". ", generate_text(model,start=start, limit=8))
 



def create_graph_with_ngram(txt, ngram = 1):
    trie_tree = trie.Trie()
    i = 0
    
    # Loop through words, create ngram size states, add to trie
    while i < (len(txt)-ngram-1):
        current_state = ""
        succ_state = ""
        for j in range(ngram):
            current_state += txt[i+j]+ " "
            succ_state += txt[i+j+ngram] + " "
        i+=1

        trie_tree.insert(current_state, succ_state)
    
    final = trie_tree.search()
    return final
    
def get_graph_transition_probabilites(graph):
    for state, succ_state in graph.items():
        #Get total prob of transition to next 
        total_prob = sum(succ_state.values())
        #update the prob
        for key,value in succ_state.items():
            graph[state][key] = value/total_prob
        
    return graph


def generate_text(model, limit=8, start="we shall " ):
    current_state = start
    succ_state = None
    text = ""
    text+=current_state+" "

    for x in range(limit):
        succ_state = random.choices(list(model[current_state].keys()),
                     list(model[current_state].values()))

        current_state = succ_state[0]
        text+=current_state+" "

    return text