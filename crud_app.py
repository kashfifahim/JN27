import json

def create_items():
    item = {}
    item['name'] = input("Enter the item's name: ")
    item['description'] = input("Enter the item's description")

    with open('data.json', 'r+') as file:
        data = json.load(file)
        data.append(item)
        file.seeek(0)
        json.dump(data, file, indent=4)

def read_items():
    pass

def update_item():
    pass

def delete_item():
    pass