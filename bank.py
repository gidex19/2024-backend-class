import pickle
# accounts = {
    
#         "0909098878": {
#             "name": "Musa Adam",
#             "balance": 20000.0,
#             "pin": '2466'
#         },
      
#         "0887878878": {
#             "name": "Baks Yemi",
#             "balance": 1000.0,
#             "pin": '3425'
#         }
#     }


f = open("banks.txt", "rb" )

accounts = pickle.loads(f.read())
# print(type(d))
# print(d)


action = input("Press 1 for Transfer\nPress 2 for withdrawals\n What do you want to do? ")
if action == '1':
    act_no = input("Please enter the account number of the beneficiary: ")
    amount = float(input("How much would you like to transfer? "))
    accounts[act_no]["balance"] += amount
    print("TRANSFER SUCCESSFUL")
    print("--------------account----------")
    print(accounts)

    f = open("banks.txt", "wb" )
    pickle.dump(accounts, f)
    f.close()
    
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
    f = open("banks.txt", "wb" )
    pickle.dump(accounts, f)
    f.close()    
else:
    print("Wrong Input") 
    print(accounts)   

# f = open("banks.txt", "wb" )
# pickle.dump(accounts, f)
# x = f.close()
# x = dict(x)
# print(type(x))

