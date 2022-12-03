import unittest
from markovchain import markov
from data_analyzation import data_analysis
from trie import trie

class TestTrieTree(unittest.TestCase):
    def setUp(self):
        self.trie = trie.Trie()

    def test_create_correct_trie(self):
        words = ["hello","how"]
        words2 = ["this","hello","is"]
        self.trie.insert(words)
        self.trie.insert(words2)
        
        
        next_states = self.trie.root.children.values()
        stack = []

        for x in next_states:
            stack.append(x)
        
        self.assertEqual(2,len(stack))

        self.assertEqual("hello",self.trie.root.children['hello'].char)


    def test_see_if_counter_is_correct(self):
        words = ["hello","how"]
        words2 = ["this","hello","is"]
        self.trie.insert(words)
        self.trie.insert(words2)


        self.assertEqual(1,self.trie.root.children['hello'].counter)

    def test_check_if_correct_probabilities(self):
        words = ["hello","how","are"]
        words2 = ["this","hello","is"]
        words3 = ['hello']
        self.trie.insert(words)
        self.trie.insert(words2)
        self.trie.insert(words3)

        self.trie.calculate_probabilities()
        self.assertEqual(0.6666666666666666,self.trie.root.children['hello'].counter)

        self.trie.insert(words3)

        self.trie.calculate_probabilities()
        self.assertEqual(0.8333333333333334,self.trie.root.children['hello'].counter)

        self.trie.insert(["I"])

        self.trie.calculate_probabilities()
        self.assertEqual(0.4166666666666667,self.trie.root.children['hello'].counter)
