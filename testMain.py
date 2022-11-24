import unittest
import main

class TestProcessInput(unittest.TestCase):

    def test_Input1(self):
        inputStr = "Breakfast 1,2,3"
        result = main.orderSystem(inputStr)
        # print(result)
        self.assertEqual(result,'Eggs, Toast, Coffee',"Should be true")
    
    def test_Input2(self):
        inputStr = "Breakfast 2,3,1"
        result = main.orderSystem(inputStr)
        # print(result)
        self.assertEqual(result,'Eggs, Toast, Coffee',"Should be true")

    def test_Input3(self):
        inputStr = "Breakfast 1,2,3,3,3"
        result = main.orderSystem(inputStr)
        # print(result)
        self.assertEqual(result,'Eggs, Toast, Coffee(3)',"Should be true")
    
    def test_Input4(self):
        inputStr = "Breakfast 1"
        result = main.orderSystem(inputStr)
        # print(result)
        self.assertEqual(result,'Unable to process: Side is missing',"Should be true")
    
    def test_Input5(self):
        inputStr = "Lunch 1,2,3"
        result = main.orderSystem(inputStr)
        # print(result)
        self.assertEqual(result,'Sandwich, Chips, Soda',"Should be true")
    
    def test_Input6(self):
        inputStr = "Lunch 1,2"
        result = main.orderSystem(inputStr)
        # print(result)
        self.assertEqual(result,'Sandwich, Chips, Water',"Should be true")
    
    def test_Input7(self):
        inputStr = "Lunch 1,1,2,3"
        result = main.orderSystem(inputStr)
        # print(result)
        self.assertEqual(result,'Unable to process: Sandwich cannot be ordered more than once',"Should be true")
    
    def test_Input8(self):
        inputStr = "Lunch 1,2,2"
        result = main.orderSystem(inputStr)
        # print(result)
        self.assertEqual(result,'Sandwich, Chips(2), Water',"Should be true")

    def test_Input8(self):
        inputStr = "Lunch"
        result = main.orderSystem(inputStr)
        # print(result)
        self.assertEqual(result,'Unable to process: Main is missing, side is missing',"Should be true")
    def test_Input9(self):
        inputStr = "Dinner 1,2,3,4"
        result = main.orderSystem(inputStr)
        # print(result)
        self.assertEqual(result,'Steak, Potatoes, Wine, Cake, Water',"Should be true")
    
    def test_Input10(self):
        inputStr = "Dinner 1,2,3"
        result = main.orderSystem(inputStr)
        # print(result)
        self.assertEqual(result,'Unable to process: Dessert is missing',"Should be true")
    
    
    def test_ProcessInputForInValidInput(self):
        inputStr = ''
        result = main.processInput(inputStr)
        print(result)
        self.assertEqual(result,[],"Should be true")
    
    def test_ProcessInputForValidInput(self):
        inputStr = "Breakfast 1,2,3"
        result = main.processInput(inputStr)
        # print(result)
        self.assertEqual(result,['Breakfast', [1,2,3]],"Should be true")
    
    

if __name__ == '__main__':
    unittest.main()
