import unittest
from HW03_Kheevar_Choudhary_ui import Ui as ui
from HW03_Kheevar_Choudhary_wordle import Wordle as wordle
from HW03_Kheevar_Choudhary_dictionary import Dictionary as dictionary
from HW03_Kheevar_Choudhary_letterlikelyhood import ll as ll
from unittest.mock import patch

class WordleTest(unittest.TestCase):

    @patch('builtins.input', side_effect = ["slave"])
    def test_user_input_length_correct(self, mock_inputs) -> None :
        """Test when the input length is correct"""
        uitest = ui()
        self.assertEqual(len(uitest.userinput(1)),5)
    
    @patch('builtins.input', side_effect = ["houses"])
    def test_user_input_length_incorrect(self, mock_inputs) -> None :
        """Test when the input length is not correct"""
        uitest = ui()
        self.assertNotEquals(len(uitest.userinput(1)),5)
    
    @patch('builtins.input', side_effect = ["books"])
    def test_user_input_valid_dictionary_word_true(self, mock_inputs) -> None :
        """Test when the input word is a valid dictionary word"""
        dicttest = dictionary()
        uitest = ui()
        self.assertTrue(dicttest.checkWord(uitest.userinput(1)))


    @patch('builtins.input', side_effect = ["ghost"])
    def test_user_input_no_special_characters(self, mock_inputs) -> None :
        """Test when the input does not contain any special characters"""
        uitest = ui()
        self.assertTrue(uitest.userinput(1))


    def test_compare_word_function_true(self) -> None :
        """Testing the compare function with correct inputs"""
        wordletest = wordle()
        self.assertTrue(wordletest.compareWord("Hello","Hello"))
    
    def test_compare_word_function_false(self) -> None :
        """Testing the compare function with incorrect inputs"""
        wordletest = wordle()
        self.assertFalse(wordletest.compareWord("Hello","Books"))

    def test_quit_function_true(self) -> None :
        """Testing the quit function with empty string"""
        uitest = ui()
        self.assertTrue(uitest.quitfunction(""))
    
    def test_quit_function_false(self) -> None :
        """Testing the quit function with a valid word"""
        uitest = ui()
        self.assertFalse(uitest.quitfunction("Books"))
    def test_file_size_function(self) -> None :
        """Testing file size function"""
        dicttest = dictionary()
        self.assertFalse(dicttest.fileSize())
    
    def test_check_temp_function_true(self) -> None :
        """Testing checkTemp function with temp as not 0"""
        lltest = ll()
        self.assertTrue(lltest.checkTemp(["A",(3,5,7,2,3)]))
    def test_check_temp_function_false(self) -> None :
        """Testing checkTemp function with temp as 0"""
        lltest = ll()
        self.assertFalse(lltest.checkTemp([""]))

if __name__ == "__main__":
    unittest.main()
