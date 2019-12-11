import unittest
from .__init__ import PyDictionary

dictionary = PyDictionary()


class PyDictionaryTest(unittest.TestCase):
    def testMeaning(self):
        self.assertIsInstance(dictionary.meaning('python'), dict)

    def testSynonym(self):
        self.assertIsInstance(dictionary.synonym('happy'), list)

    def testAntonym(self):
        self.assertIsInstance(dictionary.antonym('happy'), list)


if __name__ == '__main__':
    unittest.main()
