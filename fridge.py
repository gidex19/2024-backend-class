stock = {
    "banana": 5,
    "orange": 1,
    "kiwi": 12,
    "mango": 2
}
q = "yes"
while q == 'yes':
    newstock = input("What do you want to add to the fridge? ")
    quantity = int(input("how many do you want to add? "))
    if newstock in stock:
        stock[newstock] += quantity
    else:
        stock[newstock] = quantity
    q = input("Do you still want to add an iten to the fridge? ")

print(stock)