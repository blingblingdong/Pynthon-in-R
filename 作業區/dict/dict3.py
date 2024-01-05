def add_product(dict_product, product_id, product_info):
    if product_id not in dict_product:
        dict_product[product_id] = product_info
        print("Product added successfully.")
    else:
        print("Product ID already exists.")

def modify_product(dict_product, product_id, product_info):
    if product_id in dict_product:
        dict_product[product_id] = product_info
        print("Product modified successfully.")
    else:
        print("Product ID does not exist.")

def delete_product(dict_product, product_id):
    if product_id in dict_product:
        del dict_product[product_id]
        print("Product deleted successfully.")
    else:
        print("Product ID does not exist.")

def query_product(dict_product, product_id):
    if product_id in dict_product:
        print(f"Product ID: {product_id}, Info: {dict_product[product_id]}")
    else:
        print("Product ID does not exist.")

def list_products(dict_product):
    for product_id, product_info in dict_product.items():
        print(f"Product ID: {product_id}, Info: {product_info}")

# Main function to handle the product system operations
def product_system():
    dict_product = {}  # Dictionary to store product records

    while True:
        # Display the menu
        print("\nProduct Management System")
        print("1: Add Product")
        print("2: Modify Product")
        print("3: Delete Product")
        print("4: Query Product")
        print("5: List All Products")
        print("Others: Exit")

        # Get user choice
        choice = input("Enter your choice (1-5): ")

        # Perform the chosen action
        if choice == '1':
            product_id = input("Enter product ID to add: ")
            product_name = input("Enter product name: ")
            product_price = float(input("Enter product price: "))
            add_product(dict_product, product_id, [product_name, product_price])
        elif choice == '2':
            product_id = input("Enter product ID to modify: ")
            product_name = input("Enter new product name: ")
            product_price = float(input("Enter new product price: "))
            modify_product(dict_product, product_id, [product_name, product_price])
        elif choice == '3':
            product_id = input("Enter product ID to delete: ")
            delete_product(dict_product, product_id)
        elif choice == '4':
            product_id = input("Enter product ID to query: ")
            query_product(dict_product, product_id)
        elif choice == '5':
            list_products(dict_product)
        else:
            print("Exiting the system.")
            break

# Run the product system
# product_system() # Uncomment this line to run the system in a local environment
