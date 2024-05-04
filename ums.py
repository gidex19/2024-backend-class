

import random
database = {
    '2024/1/1234': {
        'name': 'Aliyu Musa',
        'level': 100,
        'programme': "LAW",
        "fees_paid": False,
        "cgpa": 4.1

    },
        '2024/1/2234': {
        'name': 'Harlem Abel',
        'level': 100,
        'programme': "HISTORY",
        "fees_paid": False,
        "cgpa": 2.5

    }

}

"""1. university information management System
    FEATURES:
    A. admit student - name, level, programme, cgpa, fees_paid, matric_number 
    B. expel/remove student
    C. show result
    d. pay_fees

    
    2. quiz app


"""
selected_matric = ['2024/1/1234', ]
def generate_matric_no(start_point, end_point):
    rand = random.randint(start_point, end_point)
    mat_no = f"2024/1/{str(rand)}"
    if mat_no in selected_matric:
        generate_matric_no(start_point, end_point)
    else:
        selected_matric.append(mat_no)
        return mat_no    
print("What would you like to do?\n1. ADMIT NEW STUDENT\n2. EXPEL STUDENT\n3. SHOW RESULT\n4. PAY FEES\n5. QUIT")
option = int(input(("Enter Option: ")))
if option == 1:
    name = input("Enter full name of the student: ").strip().capitalize()
    progamme = input("What is your programme: ").strip().upper()
    matric = generate_matric_no(1000, 9999)
    database[matric] = {
        "name": name,
        "level": 100,
        "progamme": progamme,
        "fees_paid": False,
        "cgpa": 0.00
    }
    print("Student added successfully...")
elif option == 2:
    matric = input("Enter matric number of the student: ").strip()
    if database.get(matric) != None:
        database.pop(matric)
    else:
        print("This student does not exist")    
elif option ==3:
    matric = input("Enter matric number of the student: ").strip()
    if database.get(matric) != None:
        cgpa = database[matric]["cgpa"]
        print(f"Hello {database[matric]["name"]}\nYour CGPA is {cgpa}")
    else:
        print("This student does not exist") 
elif option == 4:
    matric = input("Enter matric number of the student: ").strip()
    if database.get(matric) != None:
        database[matric]["fees_paid"] = True
else: 
    pass
print(database)