import unittest
import HW03_Kheevar_Choudhary_ui as ui
import HW03_Kheevar_Choudhary_wordle as wordle
import HW03_Kheevar_Choudhary_dictionary as dictionary
import HW03_Kheevar_Choudhary_letterlikelyhood as ll
from unittest.mock import patch

class WordleTest(unittest.TestCase):
    @patch('builtins.input', side_effect = ["slave"])
    def test_user_input_length_correct(self, mock_inputs) -> None :
        """Test when the input length is correct"""
        self.assertEqual(len(ui.userinput(1)),5)
    
    @patch('builtins.input', side_effect = ["houses"])
    def test_user_input_length_incorrect(self, mock_inputs) -> None :
        """Test when the input length is not correct"""
        self.assertNotEquals(len(ui.userinput(1)),5)
    
    @patch('builtins.input', side_effect = ["books"])
    def test_user_input_valid_dictionary_word_true(self, mock_inputs) -> None :
        """Test when the input word is a valid dictionary word"""
        self.assertTrue(dictionary.checkWord(ui.userinput(1)))

    @patch('builtins.input', side_effect = ["slave"])
    def test_user_input_valid_dictionary_word_false(self, mock_inputs) -> None :
        """Test when the input word is not a valid dictionary word"""
        self.assertFalse(dictionary.checkWord(ui.userinput(1)))

    @patch('builtins.input', side_effect = ["ghost"])
    def test_user_input_no_special_characters(self, mock_inputs) -> None :
        """Test when the input does not contain any special characters"""
        self.assertTrue(ui.userinput(1))

    @patch('builtins.input', side_effect = ["@had$"])
    def test_user_input_special_characters(self, mock_inputs) -> None :
        """Test when the input does contain special characters"""
        self.assertEqual(ui.userinput(1),"incorrect input")

    def test_compare_word_function_true(self) -> None :
        """Testing the compare function with correct inputs"""
        self.assertTrue(wordle.compareWord("Hello","Hello"))
    
    def test_compare_word_function_false(self) -> None :
        """Testing the compare function with incorrect inputs"""
        self.assertFalse(wordle.compareWord("Hello","Books"))

    def test_quit_function_true(self) -> None :
        """Testing the quit function with empty string"""
        self.assertTrue(ui.quitfunction(""))
    
    def test_quit_function_false(self) -> None :
        """Testing the quit function with a valid word"""
        self.assertFalse(ui.quitfunction("Books"))
    def test_file_size_function(self) -> None :
        """Testing file size function"""
        self.assertFalse(dictionary.fileSize())
    
    def test_check_temp_function_true(self) -> None :
        """Testing checkTemp function with temp as not 0"""
        self.assertTrue(ll.checkTemp(["A",(3,5,7,2,3)]))
    def test_check_temp_function_false(self) -> None :
        """Testing checkTemp function with temp as 0"""
        self.assertFalse(ll.checkTemp([""]))

if __name__ == "__main__":
    unittest.main()
