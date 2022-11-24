import unittest
import order as ord

class TestProcessInput(unittest.TestCase):
    def test_CheckInputForValidTest(self):
        order = ord.Order("Dinner",[1,2,3,4])
        result = order.checkMenu()
        self.assertEqual(result,"Steak, Potatoes, Wine, Cake, Water","Should be true")
    
    def test_CheckOrderForValidInput(self):
        order = ord.Order("Dinner",[1])
        result = order.checkMenu()
        self.assertEqual(result,"Unable to process: Side is missing","Should be true")
    
    def test_ProcessDinnerForValidTest(self):
        order = ord.Order("Dinner",[1,2,3,4])
        result = order.processDinner()
        self.assertEqual(result,"Steak, Potatoes, Wine, Cake, Water","Should be true")
    
    def test_ProcessDinnerForInValidTest(self):
        order = ord.Order("Dinner",[1,2])
        result = order.processDinner()
        self.assertEqual(result,"Unable to process: Dessert is missing","Should be true")
    
    def test_ProcessLunchForValidTest(self):
        order = ord.Order("Lunch",[1,2,3])
        result = order.processLunch()
        self.assertEqual(result,"Sandwich, Chips, Soda","Should be true")
    
    def test_ProcessLunchForInValidTest(self):
        order = ord.Order("Lunch",[1,1,2])
        result = order.processLunch()
        self.assertEqual(result,"Unable to process: Sandwich cannot be ordered more than once","Should be true")
    
    def test_ProcessBreakfastForValidTest(self):
        order = ord.Order("Breakfast",[1,2,3])
        result = order.processBreakfast()
        self.assertEqual(result,"Eggs, Toast, Coffee","Should be true")
    
    def test_ProcessBreakfastForInValidTest(self):
        order = ord.Order("Breakfast",[1,2])
        result = order.processBreakfast()
        self.assertEqual(result,"Eggs, Toast, Water","Should be true")
    
    
    

if __name__ == '__main__':
    unittest.main()
