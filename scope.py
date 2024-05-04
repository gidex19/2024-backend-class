x = 20
fruits = ["orange", "banana", "water melon" ]
def greeting():
    print("Hi there")

def my_func():
    # global y
    global x
    y = ''
    x = 60
    def area():
        nonlocal y
        y = 10
        print(x)
    area()
    print(y)    
# my_func()
# print(x) 
