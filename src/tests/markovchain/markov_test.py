import unittest
from markovchain import markov
from data_analyzation import data_analysis
from trie import trie
import io
import sys

class TestMarkovChain(unittest.TestCase):
    def setUp(self):
        pass

    def test_create_graph_with_ngram(self):
        original = "he is, he was not, not him him was he is"
        s = original.split()

        
        txt = data_analysis.clean_text_file(s)
        final_graph = markov.create_graph_with_ngram(txt,2)
        self.assertEqual(5,len(final_graph.root.children.values()))
    
    def test_generate_text(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput


        trie_tree = trie.Trie()
        words = ["hello","how"]
        trie_tree.insert(words)
        markov.generate_text(trie_tree,limit=1)
        
        sys.stdout = sys.__stdout__ 

        self.assertEqual(211,len(capturedOutput.getvalue()))
