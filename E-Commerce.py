
LOW_STOCK_THRESHOLD =5

class Product:
    def __init__(self,product_id,name,price,stock,category):
        self.product_id=product_id
        self.name=name
        self.price=price
        self.stock=stock
        self.category=category

    def update_stock(self,quantity):
        if quantity < 0:
            if self.stock >= abs(quantity):
                self.stock -= abs(quantity)
                if self.stock < LOW_STOCK_THRESHOLD:
                    print(f"⚠️ Warning: {self.name} stock is low ({self.stock} left)")
                print(f"{self.name} Available stock {self.stock}")
                return True
            else:
                print(f"Not enough stock for {self.name}")
                return False
        else:
            self.stock += quantity
            if self.stock < LOW_STOCK_THRESHOLD:
                print(f"⚠️ Warning: {self.name} stock is low ({self.stock} left)")
            print(f"{self.name} Available stock {self.stock}")
            return True


class Cart:
    def __init__(self):
        self.items={}

    def add_to_cart(self, product, quantity):
        if product.update_stock(-quantity):
            if product.product_id in self.items:
                    existing_product,existing_quantity=self.items[product.product_id]
                    self.items[product.product_id] = (existing_product, existing_quantity+quantity)

            else:
                    self.items[product.product_id] = (product, quantity)
                    print(f"{product.name} is added to cart")
        else:
            print(f"Could not add {product.name} to cart due to insufficient stock.")


    def remove_item(self,product_id):
        if product_id in self.items:
            self.items.pop(product_id)
            print(f"{product_id} is removed from cart")
        else:
            print(f"product id {product_id} invalid")

    def view_items(self):
        for item,(products,quantity)in self.items.items():
            print(f"{products.name}: price {products.price} quantity {quantity}")

    def calculate_total(self):
        sum_amount=0
        for item,(products,quantities) in self.items.items():
            total =products.price * quantities
            sum_amount+=total
        return sum_amount


class Customer:
    def __init__(self,customer_id,name):
        self.customer_id = customer_id
        self.name = name
        self.cart = Cart()

    def add_to_cart(self,product,quantity):
        self.cart.add_to_cart(product,quantity)
        print(f"customer {self.name} added item to cart")

    def remove_item(self,product_id):
        self.cart.remove_item(product_id)

    def view_cart(self):
        self.cart.view_items()

    def checkout(self):
        total =self.cart.calculate_total()
        self.cart.items.clear()
        print(f"Total {total}")



products = {
    1: Product(1, "Bread", 20, 5, "Bakery"),
    2: Product(2, "Milk", 30, 4, "Dairy"),
    3: Product(3, "Eggs", 50, 6, "Poultry")
}

# ==== Customer Registry ====
customers = {
    1: Customer(1, "Mpho"),
    2: Customer(2, "Lebo")
}
def register(name):
    last_key = max(customers.keys())
    customer=customers[last_key]
    last_customer_key=customer.customer_id+1
    customers[last_customer_key]=Customer(last_customer_key,name)
    print(f"Registration successful! Your customer ID is {last_customer_key}")



def display_customer():
    print("\nAvailable Customers:")
    for p in customers.values():
        print(f"ID: {p.customer_id} | {p.name}")



def display_products():
    print("\nAvailable Product:")
    for p in products.values():
        print(f"ID: {p.product_id} | {p.name} | Price: {p.price} | Stock: {p.stock}")


def main():
    print("Welcome to MiniMart!\n")

    while True:
        try:
            while True:

                print("\n1. Login\n2. Register new customer\n3. Admin Restock\n4. Exit")
                choice = int(input("Enter selection : "))
                if choice == 1:
                    cid = int(input("Enter customer ID (1 for Mpho, 2 for Lebo, 0 to exit): "))
                    if cid == 0:
                        print("Goodbye!")
                        break
                    if cid not in customers:
                        print("Invalid customer ID.\n")
                        continue

                    customer = customers[cid]
                    print(f"\nWelcome, {customer.name}!\n")
                elif choice == 2:
                    customer_name = input("Enter Customer name: ")
                    register(customer_name)
                    display_customer()
                elif choice ==3:
                    display_products()
                    pid = int(input("Enter product ID: "))
                    positive_quantity = int(input("Enter product Quantity: "))
                    if positive_quantity > 0:
                        if pid in products[pid]:
                            product=products[pid]
                            product.update_stock(positive_quantity)
                            print(f"Restocked {positive_quantity} of {product.name}. new stock {product.stock}")
                        else:
                            print("Invalid Product ID")
                    else:
                        print("Enter a positive quantity")

                elif choice ==4:
                    break
                else:
                    print("Invalid selection")


                while True:
                    print("\n1. View Products\n2. Add to Cart\n3. Remove from Cart\n4. View Cart\n5. Checkout\n6. Switch Customer\n")
                    choice = input("Choose an option: ")

                    if choice == "1":
                        display_products()

                    elif choice == "2":
                        display_products()
                        pid = int(input("Enter Product ID to add: "))
                        qty = int(input("Enter quantity: "))
                        if pid in products:
                            customer.add_to_cart(products[pid], qty)
                        else:
                            print("Invalid product ID.")

                    elif choice == "3":
                        customer.view_cart()
                        pid = int(input("Enter Product ID to remove: "))
                        customer.remove_item(pid)

                    elif choice == "4":
                        customer.view_cart()

                    elif choice == "5":
                        customer.checkout()

                    elif choice == "6":
                        break



                    else:
                        print("Invalid choice.")
        except ValueError:
            print("Please enter valid numbers.")


main()





