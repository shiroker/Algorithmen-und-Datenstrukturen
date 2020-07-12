
import unittest
from ADTQueue import ADTQueue

class TestADTQueue(unittest.TestCase):
    def setUp(self):
        self.adtQueue = ADTQueue()

    def test_enqueue(self):
        self.adtQueue.enqueue(34)
        self.adtQueue.enqueue(35)
        self.adtQueue.enqueue(36)
        self.assertFalse(self.adtQueue.isEmpty())

    def test_dequeue(self):
        self.adtQueue.enqueue(34)
        self.adtQueue.enqueue(35)
        self.adtQueue.enqueue(36)
        self.adtQueue.dequeue()
        self.assertFalse(self.adtQueue.laenge() == 3)
        self.assertTrue(self.adtQueue.laenge() == 2)

    def test_front(self):
        self.adtQueue.enqueue(34)
        self.adtQueue.enqueue(35)
        self.adtQueue.enqueue(36)
        self.assertTrue(self.adtQueue.front() == 34)

    def test_laenge(self):
        self.adtQueue.enqueue(34)
        self.adtQueue.enqueue(35)
        self.adtQueue.enqueue(36)
        self.adtQueue.enqueue(34)
        self.adtQueue.enqueue(35)
        self.adtQueue.enqueue(36)
        self.assertTrue(self.adtQueue.laenge()== 6)
        self.adtQueue.dequeue()
        self.adtQueue.dequeue()
        self.adtQueue.dequeue()
        self.assertTrue(self.adtQueue.laenge()==3)
        
    def test_equals(self):
        self.adtQueue.enqueue(34)
        self.adtQueue.enqueue(35)
        self.adtQueue.enqueue(36)
        self.adtQueue.enqueue(34)
        self.adtQueue.enqueue(35)
        self.adtQueue.enqueue(36)

        other = ADTQueue()
        other.enqueue(34)
        other.enqueue(35)
        other.enqueue(36)
        other.enqueue(34)
        other.enqueue(35)
        other.enqueue(36)
        self.assertTrue(self.adtQueue.equals(other))

        other.dequeue()
               
        self.assertFalse(self.adtQueue.equals(other))
        self.assertTrue(self.adtQueue.laenge() == 6)
        self.assertTrue(other.laenge() == 5)
                
    def test_reverse(self):
        self.adtQueue.enqueue('eins')
        self.adtQueue.enqueue('zwei')
        self.adtQueue.enqueue('drei')
        self.adtQueue.enqueue('vier')
        self.assertTrue(self.adtQueue.front() == 'eins')
        self.adtQueue.reverse()
        self.assertTrue(self.adtQueue.front() == 'vier')
        




if __name__ == "__main__":
        unittest.main()