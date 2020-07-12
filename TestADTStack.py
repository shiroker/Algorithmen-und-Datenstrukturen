import unittest
from ADTStack import ADTStack

class TestADTStack(unittest.TestCase):

    def setUp(self):
        self.adtStack = ADTStack()

    def test_push(self):
        self.assertTrue(None == self.adtStack.top())
        self.adtStack.push(34)
        self.adtStack.push(45)
        self.assertIsNotNone(self.adtStack.top())
        self.assertTrue(45 == self.adtStack.top())

    def test_pop(self):
        self.adtStack.push(34)
        self.adtStack.push(45)
        self.adtStack.pop()
        self.assertTrue(34 == self.adtStack.top())
    
    def test_laenge(self):
        self.adtStack.push(34)
        self.adtStack.push(45)
        self.adtStack.pop()
        self.assertTrue(1==self.adtStack.laenge())

    def test_equals(self):
        self.adtStack.push(34)
        self.adtStack.push(45)
        self.adtStack.pop()

        other = ADTStack()
        other.push(34)
        self.assertTrue(self.adtStack.equals(other))








if __name__ == "__main__":
        unittest.main()
