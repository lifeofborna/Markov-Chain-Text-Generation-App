import unittest
import string 
from data_analyzation import data_analysis

class TestDataAnalyzis(unittest.TestCase):
    def setUp(self):
        pass

    def test_if_no_punctuation(self):
        text = "A?B!!!BBBB.,.....B)))=B<BB>C"
        clean_data = data_analysis.clean_text_file(text)

        self.assertAlmostEqual(string.punctuation in clean_data, False)
    
    def test_no_numbers(self):
        text = "1212122221A"
        clean_data = data_analysis.clean_text_file(text)
        nums = (1,2)
        self.assertAlmostEqual(nums in clean_data, False)

    def test_right_amout_of_words(self):
        correct_ans = 745535
        words = data_analysis.read_from_file()
        ans = len(words)

        self.assertAlmostEqual(ans, correct_ans)