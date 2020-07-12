import unittest 
from ADTList import ADTList

class TestADTList(unittest.TestCase):

    def setUp(self):
        self.adtList = ADTList()
        


    def tet_addElem(self):
        self.adtList.addElem(2,45)
        self.adtList.addElem(3,768)
        self.adtList.addElem(9,456)
        self.assertFalse(self.adtList.isEmpty)
        self.assertEqual(45, self.adtList.getElem(2))
        self.assertFalse(self.adtList.isEmpty())
    
    def test_deleteElem(self):
        self.adtList.addElem(2,45)
        self.adtList.addElem(3,768)
        self.adtList.addElem(9,456)
        self.adtList.deleteElem(2)
        self.assertEqual(9, self.adtList.laenge())
        self.assertEqual([None,768,456], self.adtList.getAllElems())
        self.adtList.deleteElem(3)
        self.adtList.deleteElem(9)
        self.assertTrue(0 == self.adtList.laenge())

    def test_equals(self):
        self.adtList.addElem(1,"eins")
        self.adtList.addElem(3,567)
        other = ADTList()
        other.addElem(1,'eins')
        other.addElem(3,567)
        self.assertTrue(self.adtList.equals(other))
        other.addElem(5,567)
        self.assertFalse(self.adtList.equals(other))

    def test_retrieve(self):
        self.adtList.addElem(2,567)
        self.adtList.addElem(6,8765)
        self.adtList.retrieve(2)
        self.assertIsNone(self.adtList.getElem(2))
        
        


if __name__ == "__main__":
        unittest.main()
