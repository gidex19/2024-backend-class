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


action = input("Press 1 for Transfer\nPress 2 for withdrawals\n What do you want to do? ")
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
else:
    print("Wrong Input")    

