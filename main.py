# main.py
from book_data import load_books, save_books
from add_book import add_book
from view_books import view_books
from remove_book import remove_book

def main_manu():
    books = load_books()  # Load existing books
    while True:
        print("\n--- Book Store Management System ---") 
        print("1. Add Book")
        print("2. View Books")
        print("3. Remove Book")
        print("4. Exits")
        choice = input("Enter your choice: ")

        if choice == "1":
            books = add_book(books)
        elif choice == "2":
            view_books(books)
        elif choice == "3":
            books = remove_book(books)
        elif choice == "4":
            save_books(books)  # save book before existing

        print("Existing the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again!")

if __name__== "__main__"   :
    main_manu()         


