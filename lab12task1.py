import json
with open("products.json", encoding="utf-8") as file:
    data = json.load(file)
count = len(data["products"])
for i, product in enumerate(data["products"]):
    print("Название:", product["name"])
    print("Цена:", product["price"])
    print("Вес:", product["weight"])
    
    if product["available"]:
        print("В наличии")
    else:
        print("Нет в наличии!")