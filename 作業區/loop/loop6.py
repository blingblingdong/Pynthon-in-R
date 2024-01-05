# A list to store the library's books
library = []

# Sub-function to add a book
def add_book(book_title):
    library.append(book_title)
    print(f"'{book_title}' has been added to the library.")

# Sub-function to remove a book
def remove_book(book_title):
    if book_title in library:
        library.remove(book_title)
        print(f"'{book_title}' has been removed from the library.")
    else:
        print("Book not found in the library.")

# Sub-function to list all books
def list_books():
    if library:
        print("Library Books:")
        for book in library:
            print(book)
    else:
        print("The library is empty.")

# Sub-function to search for a book
def search_book(book_title):
    if book_title in library:
        print(f"'{book_title}' is in the library.")
    else:
        print(f"'{book_title}' is not in the library.")

# Main function to handle user interaction
def library_system():
    while True:
        print("\nLibrary System")
        print("1: Add Book")
        print("2: Remove Book")
        print("3: List Books")
        print("4: Search Book")
        print("5: Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            book_title = input("Enter the title of the book to add: ")
            add_book(book_title)
        elif choice == '2':
            book_title = input("Enter the title of the book to remove: ")
            remove_book(book_title)
        elif choice == '3':
            list_books()
        elif choice == '4':
            book_title = input("Enter the title of the book to search: ")
            search_book(book_title)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

# Run the library system
library_system()
