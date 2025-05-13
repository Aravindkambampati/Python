import unittest
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
class UnitTesting(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3),5)
        self.assertEqual(add(-1,3),2)
        self.assertEqual(add(5,6),11)
    def test_subtract(self):
        self.assertEqual(subtract(4,2),2)
        self.assertEqual(subtract(-1,-3),2)
        self.assertEqual(subtract(3,6),-3)
