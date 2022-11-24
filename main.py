import order as ord

def processInput(inpString)->list:
    
    inpString = inpString.split(" ")
    print("np: ",inpString)
    if inpString==['']:
        return []
    orderType = inpString[0]
    try:
        orderMenu = [int(item) for item in inpString[1].split(',') if item.isdigit()]
        orderMenu.sort()
    except:
        return []

    order = list()
    order.append(orderType)
    order.append(orderMenu)
    # print(order)
    return order
def orderSystem(inpOrder)->str:
    # processing the input to appropriate form
    # inpOrder = input()
    order = processInput(inpOrder)
    print("order####: ",order)
    if order != []:
        newOrder = ord.Order(order[0],order[1])
        outputString = newOrder.checkMenu()
        return (outputString)
    else:
        return ("Unable to process: Main is missing, side is missing")


def main():
    while(True):
        print("Place Order:")
        print("Breakfast:\n\t1. Main-Eggs\n\t2. Side-Toast\n\t3. Drink-Coffee")
        print("Lunch:\n\t1. Main-Sandwich\n\t2. Side-Chips\n\t3. Drink-Soda")
        print("Dinner:\n\t1. Main-Steak\n\t2. Side-Potatoes\n\t3. Drink-Wine\n4. Desert-Cake")
        print("\nPlease enter your choice: ")
        inpOrder = input()
        print(orderSystem(inpOrder))
        print("\nWant to Place another order. Please choose 1 or Select any other key to close the menu: ")
        if(input()!='1'):
            print("\nThank you for choosing us!")
            break

if __name__=="__main__":
    main()