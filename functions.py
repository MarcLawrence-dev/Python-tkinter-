def groceryComputation(item, quantity, price):
    totalComputation = quantity * price
    print("Your item is " + item + " quantity is " + str(quantity) + " and the total price is " + str(totalComputation)) 

shopper = input("Enter the item you are purchasing: ")
itemQuantity = int(input("Enter the quantity of your item: "))
itemPrice = float(input("Enter the price of your item: "))
groceryComputation(shopper, itemQuantity, itemPrice)
