inventory = {
    "pen" : 20,
    "notebook" : 15,
    "eraser" : 30
}

inventory["pen"] = 15
inventory["pencil"] = 25

for key, value in inventory.items():
    print(key, ":", value)
