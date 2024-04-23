candidates = {
    "0123": {
        "name": "Aba John",
        "location": "Lagos",
        "age": 27,
        "kids": ["jnr", "ade", "barakat"]
    },
    "0124": {
        "name": "James Ogu",
        "location": "Benin",
        "age": 34,
        "kids": ["Shola"]
    }
}

for candidate in candidates:
    print(f"for candidate with the Application ID:{candidate}")
    candidates_name = candidates[candidate]["name"].split()
    last_name = candidates_name[0]

    for kid in candidates[candidate]["kids"]:
        print(f"My Name is {last_name} {kid}")
    print("\n")    

