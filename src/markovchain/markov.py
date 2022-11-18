from trie import trie

#TODO add gen random text function

def construct_markov_model(txt,ngram=3,limit=10):
    get_graph = create_graph_with_ngram(txt,ngram)
    model = get_graph_transition_probabilites(get_graph)
    # gen_text = generate_text(model, limit, )
    #for state,succ in model.items():
     #   print(f'------------------------{state}---------------------------------------')
     #   print(model[state])



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

      #  tree.add_to_trie(current_state[:-1],succ_state[:-1])
        trie_tree.insert(current_state, succ_state)
    
    final = trie_tree.search()
    return final
    
def get_graph_transition_probabilites(graph):
    for state, succ_state in graph.items():
        #Get total prob of transition to next 
        total_prob = sum(succ_state.values())
        #update the prob
        for key,value in succ_state.items():
          #s  print(f'{value} / {total_prob}')
            graph[state][key] = value/total_prob
        
    return graph


#def generate_text(model, limit, )
