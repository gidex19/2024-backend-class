# x = {
#   "name": "Larry"
# }
# try:
#   print(x["age"])
# except NameError:
#   print("An exception occurred")
# except KeyError:
#   print("this key does not exist in this dictionary")
# except:
#   print("unknown error")  
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")