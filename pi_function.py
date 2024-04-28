def pi_func():
    print(f"the value of pi is: {22/7}")

def area_of_a_circle(r=5):
    # print(f"{(22/7) * (r)**2 }")
    return (22/7) * (r)**2 
    
def area_rectangle(l,b):
    return l*b
a = area_of_a_circle(6)

b = area_rectangle(4,5)
print(b)    