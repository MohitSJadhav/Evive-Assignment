import json

OrderMenu = json.load(open('menu.json'))

class Order(object):
    
    def __init__(self, mealType, orderItems):
        self.mealType = mealType    # Options are: Breakfast, Lunch, Dinner
        self.orderItems = orderItems    # List of orders

    def checkMenu(self)->str:
        # If orderedItems is empty 
        if self.orderItems == []:
            return "Unable to process: Main is missing, side is missing"
        
        # check if main and side are present
        if (1 not in self.orderItems or 2 not in self.orderItems):
            if(1 not in self.orderItems and 2 not in self.orderItems):
                return "Unable to process: Main is missing, side is missing"
            elif (1 not in self.orderItems):
                return "Unable to process: Main is missing"
            elif (2 not in self.orderItems):
                return "Unable to process: Side is missing"
        
        # Check the type of Meal
        if(self.mealType == "Breakfast"):
            print("OrderItems: ",self.orderItems)
            return self.processBreakfast()
        elif(self.mealType == "Lunch"):
            return self.processLunch()
        elif(self.mealType == "Dinner"):
            return self.processDinner()
        else:
            return "Incorrect Meal type selected"

    # Process Breakfast according to conditions stated in requirements.
    def processBreakfast(self)->str:
        outputString = list()
        menuItem = self.orderItems
        countGreater = 0
        if menuItem.count(3)>1:
            countGreater = menuItem.count(3)
        menuItem = list(set(menuItem))
        for i in menuItem:
            if i>3:
                return "Invalid menu item"
            if(i==3 and countGreater!=0):
                outputString.append((OrderMenu['Order'][str(self.mealType)][str(i)])+"("+str(countGreater)+")")
                continue
            outputString.append(OrderMenu['Order'][str(self.mealType)][str(i)])
        if 3 not in menuItem:
            outputString.append("Water")    
        return ', '.join(outputString)

    # Process Lunch according to conditions stated in requirements.
    def processLunch(self)->str:
        outputString = list()
        menuItem = self.orderItems
        countGreater = 0
        if menuItem.count(1)>1:
            return "Unable to process: Sandwich cannot be ordered more than once"
        if menuItem.count(2)>1:
            countGreater = menuItem.count(2)
        menuItem = list(set(menuItem))
        for i in menuItem:
            if i>3:
                return "Invalid menu item"
            if(i==2 and countGreater!=0):
                outputString.append((OrderMenu['Order'][str(self.mealType)][str(i)])+"("+str(countGreater)+")")
                continue
            outputString.append(OrderMenu['Order'][str(self.mealType)][str(i)])
        if 3 not in menuItem:
            outputString.append("Water")    
        return ', '.join(outputString)
    
    # Process Dinner according to conditions stated in requirements.
    def processDinner(self)->str:
        outputString = list()
        menuItem = self.orderItems
        countGreater = 0
        if menuItem.count(3)>1:
            countGreater = menuItem.count(3)
        menuItem = list(set(menuItem))
        if 4 not in menuItem:
            return "Unable to process: Dessert is missing"
        for i in menuItem:
            if i>4:
                return "Invalid menu item"
            outputString.append(OrderMenu['Order'][str(self.mealType)][str(i)]) 
        outputString.append('Water')
        return ', '.join(outputString)
