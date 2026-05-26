import json
with open("products.json", encoding="utf-8") as file:
    data = json.load(file)
print("Добавление нового продукта:")
name = input("Название: ")
price = int(input("Цена: "))
weight = int(input("Вес: "))
available = input("В наличии? (да/нет): ")
data["products"].append({
    "name": name,
    "price": price,
    "weight": weight,
    "available": available
})
with open("products.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("\nПродукт добавлен!\n")
print("Обновленный список:")
for product in data["products"]:
    status = "В наличии" if product["available"] else "Нет в наличии"
    print(f"{product['name']} - {product['price']} руб. ({status})")
