# Vending machine items and prices
items = {
    '1': {'name': 'bubble', 'price': 1},
    '2': {'name': 'coke', 'price': 1.50},
    '3': {'name': 'ice cream', 'price': 2.00},
    '4': {'name': 'nuts', 'price': 1.00},
    '5': {'name': 'chocolates','price':3.60},
    '6': {'name': 'almonds','price':4.20},
    '7':{'name':'water','price':1},
    '8':{'name':'pastries','price':6.90},
    '9':{'name':'chips','price':3.80},
    '10':{'name':'toffee','price':2.0}
    
}

# Display available items and prices
print("Welcome to the vending machine!")
print("Please select an item:")

for key,item in items.items():
    print(f"{key}.{item['name']} - ${item['price']}")
#prompt user for input 
selection= input("Enter the item number you wish to purchase:")

#check if the selected item is valid
if selection in items:
    selected_item = items[selection]
    print(f"you have selected {selected_item['name']}.")
    amount_due = selected_item['price']
    
    #prompt user to insert money
    while amount_due > 0:
        try:
            payment = float(input(f"PLEASE insert ${ amount_due:2f}:"))
            if payment >= amount_due:
                change= payment-amount_due
                print(f"Thankyou for your purchase! your change is ${change:2f}.")
                break
            else:
                print("Inufficient payment.Please insert more money.")
                amount_due = payment
        except:ValueError 
    
    print("invalid payment amount.PLEASE enter a valid number.")
else:
    print("invalid selection.PLEASE try again.")