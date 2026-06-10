
# 1. Display all products
def display_products(products):
    for pid in products:
        print(pid, products[pid])


# 2. Add new product
def add_product(pid, products):

    if pid in products:
        print("Product ID already exists")

    else:
        name = input("Enter product name: ")
        price = float(input("Enter price: "))
        stock = int(input("Enter stock: "))
        sold = int(input("Enter sold quantity: "))

        products[pid] = {
            "name": name,
            "price": price,
            "stock": stock,
            "sold": sold
        }

        print("Product added successfully")


# 3. Update stock after sales
def update_stock(pid, products):

    if pid in products:

        sold_qty = int(input("Enter sold quantity: "))

        if sold_qty <= products[pid]["stock"]:
            products[pid]["stock"] -= sold_qty
            products[pid]["sold"] += sold_qty
            print("Stock updated")

        else:
            print("Not enough stock")

    else:
        print("Product not found")


# 4. Out of stock products
def out_of_stock(products):

    for pid in products:
        if products[pid]["stock"] == 0:
            print(pid, products[pid]["name"])


# 5. Low stock (<5)
def low_stock(products):

    for pid in products:
        if products[pid]["stock"] < 5:
            print(pid, products[pid]["name"], products[pid]["stock"])


# 6. Total inventory value
def inventory_value(products):

    total = 0

    for pid in products:
        total += products[pid]["price"] * products[pid]["stock"]

    print("Total Inventory Value =", total)


# 7. Best selling product
def best_selling(products):

    best_id = None

    for pid in products:

        if best_id is None or products[pid]["sold"] > products[best_id]["sold"]:
            best_id = pid

    print("Best Seller:", best_id, products[best_id]["name"], products[best_id]["sold"])


# 8. Least selling product
def least_selling(products):

    least_id = None

    for pid in products:

        if least_id is None or products[pid]["sold"] < products[least_id]["sold"]:
            least_id = pid

    print("Least Seller:", least_id, products[least_id]["name"], products[least_id]["sold"])


# 9. Total revenue
def total_revenue(products):

    revenue = 0

    for pid in products:
        revenue += products[pid]["price"] * products[pid]["sold"]

    print("Total Revenue =", revenue)


# 10. Low stock report
def low_stock_report(products):

    report = {}

    for pid in products:
        if products[pid]["stock"] < 5:
            report[pid] = products[pid]

    print("Low Stock Report")
    for pid in report:
        print(pid, report[pid])


# 11. Above average sales
def above_avg_sales(products):

    total = 0

    for pid in products:
        total += products[pid]["sold"]

    avg = total / len(products)

    print("Average Sales =", avg)

    for pid in products:
        if products[pid]["sold"] > avg:
            print(pid, products[pid]["name"], products[pid]["sold"])


# 12. Promotion products (sales < 10)
def promotion_products(products):

    promo = {}

    for pid in products:
        if products[pid]["sold"] < 10:
            promo[pid] = products[pid]

    print("Promotion Products")

    for pid in promo:
        print(pid, promo[pid])