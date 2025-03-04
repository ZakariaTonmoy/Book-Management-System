from utils import validate_input

def add_book(books):
    print("\n--- Add a New Book ---")
    title = validate_input("Enter the book title:", str)
    author = validate_input("Enter the author: ", str)
    isbn = validate_input("Enter the ISBN: ", str)
    genre = validate_input("Enter the genre: ", str )
    price = validate_input("Enter the price: ", float, lambda x: x > 0)
    quantity = validate_input("Enter the quantity: ", int, lambda x: x>=0)

    # Check for duplicate ISBN
    if any(book["isbn"] == isbn for book in books):
        print("Error: A book with this ISBN exists.")
        return books
    
    # Adding new book
    new_book = {
        "title": title,
        "author": author,
        "isbn" : isbn,
        "genre": genre,
        "price": price,
        "quantity" : quantity
    }
    books.append(new_book)
    print("Book added successfully.")
