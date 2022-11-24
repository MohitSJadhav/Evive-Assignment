Code Implementation:
Implemented the above functionality of order system in Python language following the OOPS concept, a class named Order is created which has 2 attributes:
1. mealType- Breakfast or Lunch or Dinner
2. orderItems- List of order of items. i.e Main, Side, Drink and Desert
3. additional json is used to keep track of the orderType menu and dishes.

Methods of class are:
1. checkMenu() - checks for valid input for orderType and orderItems. Further calls other appropriate methods
2. processBreakfast() - This function checks for the breakfast order items and returns the result in form of string.
3. processLunch() - This function checks for the lunch order items and returns the result in form of string.
4. processDinner() - This function checks for the dinner order items and returns the result in form of string.

Code Execution:
To execute the python code follow steps below:
1. Command to run main file- python main.py
2. Command to run sample test file - python testMain.py
3. Command to test the class file - python testOrder.py
4. No Library dependencies are required other than unittest and json

Miscellaneous information:
1. Tests are written using unittest utility. All functions unit tests are covered including the negative positive test case.
2. All test cases given in requirement are covered in testOrder.py and can be executed at once using the command - python testMain.py.
3. Additional modification can be done such as creating child classes for every orderType and inheriting the Order class into the child classes.
