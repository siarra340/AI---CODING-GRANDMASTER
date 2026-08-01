snack_name = "Chips"
price = 1.50
quantity = 10
is_available = True
discount = 0.25

print("Snack: ", snack_name)
print("Price: $", price)
print("Quantity in stock: ", quantity)
print("Available? ", is_available)

print(type(snack_name))
print(type(price))
print(type(quantity))
print(type(is_available))

total = price * quantity
print("Total Value: $", total)
print("Sales price: $", price - discount)
print("Double stock: ", quantity * 2)

print("Is price under $2? ", price < 2)
print("More than 5 in stock? ", quantity>5)
print("Is price exactly $1.50? ", price == 1.50)

shop_name = "Quick" + " " + "Bites"
print("Shop name: ", shop_name)
print("Letters in snack name: ", len(snack_name))
print("First letter of of shop name: ", shop_name[0])

price_1 = 2
price_2 = 4

print('Value of price_1 and price_2 before Swapping', price_1)
print(price_2)

temp = price_1
price_1= price_2
price_2 = temp

print('Value of price_1 and price_2 after Swapping', price_1)
print(price_2)


