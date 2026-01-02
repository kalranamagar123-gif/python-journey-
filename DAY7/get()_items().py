student = {
    "name" : "kalpana",
    "age" : 20,
    "country" : "USA"
}

print(student.get("name"))
print(student.get("age"))
print(student.get("country"))

for key, value in student.items():
    print(key, ":", value)
