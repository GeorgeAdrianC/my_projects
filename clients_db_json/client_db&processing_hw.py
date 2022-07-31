import json
from os import name
import re
from pathlib import Path

"""A .json database generator for clients name, age, phone and email. """

def client_interogation():
    client = {
        "name" : "",
        "age" : 0,
        "phone" : "",
        "email" : ""

    }

    while True:
        name_input = str(input("Hello! Please write your full name: "))
        name_regex = re.compile(r"[A-Z][a-z]+\s([A-Z][a-z]+\s)*([A-Z][a-z]+\s)*[A-Z][a-z]+")
        match = name_regex.search(name_input)
        if match:
            client["name"] = name_input
            break
        else:
            print("Name format doesn't match.")
    
    with open('clients_db.json', 'r') as file:
        data = json.load(file)
    if name_input in data["clients"].__str__():
        for item in data["clients"]:
            if item["name"] == name_input:
                print(f"Name: {item['name']}\nAge: {item['age']}\nPhone: {item['phone']}\nEmail: {item['email']}")
        quit()
    else:
        pass


    while True:        
        age_input = int(input("Please write your age: "))
        if 0 < age_input < 100:    
            client["age"] = age_input
            break
        else:
            print("Please enter a valid age number.")

    while True:

        phone_input = input("Please write your phone number: ")
        phone_regex = re.compile(r"0\d{3}\s\d{3}\s\d{3}|0\d{3}\s\d{2}\s\d{2}\s\d{2}|0\d{9}")
        match = phone_regex.search(phone_input)
        if match:
            client["phone"] = phone_input
            break
        else:
            print("Please enter a valid phone number.")
    while True:
        email_input = input("Please write your email: ")
        email_regex = re.compile(r"^[a-zA-z0-9-\.]+@([\w-]+\.)+[\w-]{2,4}$")
        match = email_regex.search(email_input)
        if match:
            client["email"] = email_input
            break
        else:
            print("Please enter a valid email address.")
    return client

client = client_interogation()
def write_json(data, filename="clients_db.json"):
    with open (filename, "w") as f:
        json.dump(data, f, indent=4)

with open ("clients_db.json") as json_file:
    data = json.load(json_file)
    temp = data["clients"]

    temp.append(client)

write_json(data)


