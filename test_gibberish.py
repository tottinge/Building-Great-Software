import unittest
import gibberish

class TestRandomGenerator(unittest.TestCase):
    def testNameIsSelected(self):
        talker = gibberish.Gibberish()
        self.assertTrue(talker.pickName() in talker.names)

unittest.main()
