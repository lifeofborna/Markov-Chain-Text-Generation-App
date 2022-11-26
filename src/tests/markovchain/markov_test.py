import unittest
from markovchain import markov
from data_analyzation import data_analysis

class TestMarkovChain(unittest.TestCase):
    def setUp(self):
        pass

    def test_create_graph_with_ngram(self):
        original = "he is, he was not, not him him was he is"
        ans = {'he is ': {'he was ': 1}, 'is he ': {'was not ': 1}, 'he was ': {'not not ': 1}, 'was not ': {'not him ': 1}, 'not not ': {'him him ': 1}, 'not him ': {'him was ': 1}, 'him him ': {'was he ': 1}, 'him was ': {'he is ': 1}}
        s = original.split()

        
        txt = data_analysis.clean_text_file(s)
        final_graph = markov.create_graph_with_ngram(txt,2)
      
        self.assertEqual(final_graph,ans)


    def test_graph_correct_probabilities(self):
        original = "he is, he was not, not him not him him him was not him was he is"
        ans = {'he is ': {'he was ': 1.0}, 'is he ': {'was not ': 1.0}, 'he was ': {'not not ': 1.0}, 'was not ': {'not him ': 0.5, 'him was ': 0.5}, 'not not ': {'him not ': 1.0}, 'not him ': {'not him ': 0.3333333333333333, 'him him ': 0.3333333333333333, 'was he ': 0.3333333333333333}, 'him not ': {'him him ': 1.0}, 'him him ': {'him was ': 0.5, 'was not ': 0.5}, 'him was ': {'not him ': 0.5, 'he is ': 0.5}}
        s = original.split()

        
        txt = data_analysis.clean_text_file(s)
        final_graph = markov.create_graph_with_ngram(txt,2)
        get_probability_graph = markov.get_graph_transition_probabilites(final_graph)

        self.assertEqual(get_probability_graph,ans)
    

    def test_generates_text_with_correct_start(self):
        original = "he is, he was not, not him not him him him was not him was he is"
        s = original.split()

        txt = data_analysis.clean_text_file(s)
        final_graph = markov.create_graph_with_ngram(txt,2)
        get_probability_graph = markov.get_graph_transition_probabilites(final_graph)
        s = markov.generate_text(get_probability_graph, limit=3, start="he is ")
        
        ans = s.split()
        
        self.assertEqual(ans[0],'he')