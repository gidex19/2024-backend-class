mydict = {
    "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# print(mydict.get("month"))

for x, y in mydict.items():
    # print(x + "--" + str(y))
    print(f"{x}--{str(y)}")