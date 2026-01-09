students = {
    "name" : "kalpana",  #Key -name, age, country
    "age" : 20,        #Value -Kalpana, 20, Nepal
    "country" : "Nepal"

}

print(students["name"])
print(students["age"])
print(students["country"]) #If the key does not exist -> error

print(students.get("age"))
print(students.get("grade")) #No crash if key is missing
print(students.get("grade", "N/A" )) #You acn give a default value

# Get all the keys
print(students.keys())
for key in students.keys():
    print(key)


# Get all the values
print(students.values())
for value in students.values():
    print(value)

#Get keys and values together
print(students.items())
for keys, values in students.items():
    print(key, ":", values)

#Loop through dictionary
for keys in students:
    print(keys, students[keys])

#Add or updates values
students["GPA"] = "A"
students["age"] = 21
del students["country"]
print(students)

