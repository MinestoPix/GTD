import unittest

from tk_autocomplete import *


class MyTestCase(unittest.TestCase):
    # def test_set_string_var(self):
    # Creates two copies of one string_var and sets _from to "Test" while not changing _to
    # test_string_var_to = StringVar()
    # test_string_var_from = test_string_var_to
    # test_string_var_from.set("Test")
    # test_string_var = set_string_var(test_string_var_to, test_string_var_from)
    # self.assertEqual(test_string_var, test_string_var_to)
    # YOU DONT NEED TWO SEPERATE VARIABLES DUMMY
    # actually you do need two variables
    def test_complete_text_no_completion(self):
        test_text = "test"
        test_completed_text = complete_text(test_text)
        self.assertEqual(test_completed_text, test_text)

    def test_complete_text_completion(self):
        test_text = "Tom"
        test_completed_text = complete_text(test_text)
        self.assertEqual(test_completed_text, "Tomorrow")


if __name__ == '__main__':
    unittest.main()
