# example 1
def create_house(n):
    if n>0:
        print(n)
        print("house created")
        create_house(n-1)
        # n -= 1 
    else:
        print("n is zero")
        
create_house(4)       


# example 2
def factorial(x):
    if x ==1:
        return 1
    else:
        return (x * factorial(x-1))
n = factorial(4)
print(n)    