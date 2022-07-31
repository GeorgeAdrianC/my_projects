import random
"""Store program with data in dictionaries."""
products = [
    {"name":"AK-47",
    "unit":"pcs.",
    "price":500,
    "stock":20},
    {"name":"Grenades",
    "unit":"pcs.",
    "price":40,
    "stock":75},
    {"name":"AKM",
    "unit":"pcs.",
    "price":600,
    "stock":100},
    {"name":"Nukes",
    "unit":"pcs.",
    "price":9999998,
    "stock":3},
    {"name":"Glock",
    "unit":"pcs.",
    "price":600,
    "stock":120},
    {"name":"Uzi",
    "unit":"pcs.",
    "price":200,
    "stock":330},
    {"name":"Vodka",
    "unit":"pcs.",
    "price":12,
    "stock":66},
    {"name":"Borscht",
    "unit":"pcs.",
    "price":1,
    "stock":2000},
    {"name":"Matryoshka doll",
    "unit":"pcs.",
    "price":15,
    "stock":122},
    {"name":"Supreme Leader Painting",
    "unit":"pcs.",
    "price":99,
    "stock":"unlimited"},
    {"name":"Adidas Tracksuit",
    "unit":"pcs.",
    "price":150,
    "stock":152}
]
store = {
    "name": "Beryozka",
    "address":{
        "line_1":"Stalingrad",
        "line_2":"St. Volgograd, No.6"
    },
    "owner":{
        "name":"Boris Minkovski",
        "age":47
    },
    "phone_number":"+0369-521-125",
    "products": products
    } 
unavailable_product = products.pop(random.randint(0,len(products)-1))
print(f"\nGreetings comrad!!\nWelcome to {store['name']} store!\n")
print(f"We're really sorry dear confedarate but '{unavailable_product['name']}' is no longer available.\n")
# print(f"What you can choose from: \n\n {products[0]['name']}: {products[0]['price']}$ \n {products[1]['name']}: {products[1]['price']}$ \n {products[2]['name']}: {products[2]['price']}$\n {products[3]['name']}: {products[3]['price']}$\n {products[4]['name']}: {products[4]['price']}$\n {products[5]['name']}: {products[5]['price']}$\n {products[6]['name']}: {products[6]['price']}$\n {products[7]['name']}: {products[7]['price']}$\n {products[8]['name']}: {products[8]['price']}$\n {products[9]['name']}: {products[9]['price']}$\n ")
print("What you can choose from:\n")
for product in products:
    print(f"{product['name']}: {product['price']}$")
products[0]["name"] = "NEW AK-47/ SILENCER"
products[0]["price"] = 800
products[0]["stock"] = 300
print(f"\nGreat news comrade!\n We have updated our old stock of AK-47 with the {products[0]['name']}! \n You can have yours today for only {products[0]['price']}$! \n Have a great commie day!" )
print(f"\n\nFor product warranty and complaints you can always find us at:\n{store['address']['line_2']}\nCity {store['address']['line_1']}\nOwner: {store['owner']['name']}\nPhone no.: {store['phone_number']}")
print("\n         *DISCLAIMER* \n*WE DON'T SERVE CAPITALISTS*")


