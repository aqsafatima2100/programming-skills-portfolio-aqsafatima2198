# Define the price of each USB stick and the total amount of money the girl has
usb_price = 6
total_money = 50

# Calculate the maximum number of USB sticks the girl can buy
num_usb = total_money // usb_price

# Calculate the amount of money left after purchasing the USB sticks
money_left = total_money % usb_price

# Print the results
print("Number of USB sticks she can buy:", num_usb)
print("Pounds left after purchasing:", money_left)
