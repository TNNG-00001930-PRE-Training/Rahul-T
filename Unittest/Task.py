import unittest

class TestStringOperations(unittest.TestCase):
    
    def test_string_concatenation(self):
        # Test case for string concatenation
        self.assertEqual("Rahul" + " " + "Thangamani", "Rahul Thangamani")

    def test_string_slicing(self):
        # Test case for string slicing
        s = "Rahul Thangamani"
        self.assertEqual(s[:5], "Rahul")
        self.assertEqual(s[6:], "Thangamani")

    def test_string_formatting(self):
        # Test case for string formatting
        name = "Rahul"
        age = 22
        self.assertEqual("My name is {} and I am {} years old.".format(name, age), "My name is Rahul and I am 22 years old.")

    def test_string_manipulation_methods(self):
        # Test cases for string manipulation methods
        s = "  Rahul Thangamani  "
        self.assertEqual(s.upper(), "  RAHUL THANGAMANI  ")
        self.assertEqual(s.lower(), "  rahul thangamani  ")
        self.assertEqual(s.strip(), "Rahul Thangamani")
        self.assertEqual(s.replace("Rahul", "Hi"), "  Hi Thangamani  ")

if __name__ == '__main__':
    unittest.main()

