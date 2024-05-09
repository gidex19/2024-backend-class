f = open("myfile.txt", "a")

# x = f.readlines()
# x = f.read(5)
# for i in x:
#     print(i)
#     print("-----------")
# print(x)
f.write("This is the appended text")
f.close()

f = open("myfile.txt")
x = f.read()
print(x)
import os
os.remove("myfile.txt")