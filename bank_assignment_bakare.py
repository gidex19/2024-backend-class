import random

accounts = {
    
        "0909098878": {
            "name": "Musa Adam",
            "balance": 20000.0,
            "pin": '2466'
        },
      
        "0887878878": {
            "name": "Baks Yemi",
            "balance": 1000.0,
            "pin": '3425'
        }
    }

accounts_list = []
for i in accounts.keys():
    accounts_list.append(i)
print(accounts_list)    



action = input("Press 1 for Transfer\nPress 2 for withdrawals\nPress 3 for Create an Account\n What do you want to do? ")
if action == '1':
    act_no = input("Please enter the account number of the beneficiary: ")
    amount = float(input("How much would you like to transfer? "))
    accounts[act_no]["balance"] += amount
    print("TRANSFER SUCCESSFUL")
    print("--------------account----------")
    print(accounts)
    
elif action == '2':
    act_no = input("Please enter your account number: ")
    amount = float(input("How much would you like to withdraw? "))
    pin = input("Enter your PIN? ")
    if pin == accounts[act_no]["pin"]:
        if accounts[act_no]["balance"] >= amount:
            accounts[act_no]["balance"] -= amount
            print("Withdrawal successful")
            bal = accounts[act_no]["balance"]
            print(f"Your balance is {bal}")
            print("--------------account----------")
            print(accounts)
            print("--------------account----------")
        else:
            print("INSUFFICIENT FUNDS")    
    else:
        print("invalid PIN")
elif action == '3':
    new_name = input("Enter your name: ")
    new_pin = str(random.randint(0000,9999))
    # new_account = ''
    
    new_account = str(random.randrange(0000000000,9999999999))
    while new_account in accounts_list:
        new_account = str(random.randrange(0000000000,9999999999))
        
    accounts.update({new_account: {
            "name": new_name,
            "balance": 0.0,
            "pin": new_pin
        }})

    print("Your account number is: " + str(new_account) + "Your default PIN is: " + str(new_pin))

else:
    print("Wrong Input")    

print(accounts)




