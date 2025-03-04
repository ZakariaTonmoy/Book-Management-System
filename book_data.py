import json
import os

File_Name = "books.json"

def load_books():
    if os.path.exists(File_Name):
        with open(File_Name, "r") as file:
            return json.load(file)
    return []

def save_books(books):
    with open(File_Name, "w") as file:
        json.dump(books, file, indent = 4)
