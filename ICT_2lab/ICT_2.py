# Функция для добавления продукта
def add_product(products, name, price):
    products[name] = price 
    print("Продукт добавлен.")

# Функция для удаления продукта
def remove_product(products, name):
    if name in products:
        del products[name]  
        print("Продукт удален.")
    else:
        print("Продукт не найден.")

# Функция для просмотра всех продуктов
def view_products(products):
    if products:  
        for name, price in products.items():
            print(f"{name}: {price}")
    else:
        print("Нет доступных продуктов.")


products = {} 


while True:
    action = input("Выберите действие: add, remove, view, quit\n> ").lower()
    if action == "add":
        name = input("Введите название продукта: ")
        price = float(input("Введите цену продукта: "))
        add_product(products, name, price)
    elif action == "remove":
        name = input("Введите название продукта: ")
        remove_product(products, name)
    elif action == "view":
        view_products(products)
    elif action == "quit":
        break
    else:
        print("Неверное действие.")
