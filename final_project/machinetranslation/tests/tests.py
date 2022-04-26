import unittest
from translator import french_to_english, english_to_french

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour") #test when input is Hello, output is Bonjour
        self.assertEqual(english_to_french(""),"") #test when input is null, output is null
        self.assertNotEqual(english_to_french("One"),"1") #test when input is One, output is not 1

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello") #test when input is Bonjour, output is Hello
        self.assertEqual(french_to_english(""),"") #test when input is null, output is null
        self.assertNotEqual(french_to_english("Un"),"1") #test when input is Un, output is not 1

unittest.main()