import json

class BookCollection:

    def __init__(self):
        self.book_list =[]
        self.storage_file ="books_data.json"
        self.read_form_file()

    def read_form_file(self):
        try:
            with open(self.storage_file , "r")as file:
                self.book_list = json.load(file)
        except(FileNotFoundError , json.JSONDecodeError):
            self.book_list = []

    def save_to_file(self):
        with open(self.storage_file , "w") as file:
            json.dump(self.book_list, file , indent=4)

    def create_new_book(self):
        book_title = input("Enter your book name: ")
        book_author = input("Enter Author name: ")
        publication_year = input("Enter publication year: ")
        book_genre = input("Enter genre: ")
        is_book_read = (input("Have you read this book?(yes/no):").strip().lower() == "yes")

        new_book ={
            "title" : book_title,
            "author" : book_author,
            "year" :  publication_year,
            "genre" : book_genre,
            "read" : is_book_read,
        }

        self.book_list.append(new_book)
        self.save_to_file()
        print("Book added Successfully")

    def delete_book(self):
        book_title = input("Enter the title of book to remove")
        for book in self.book_list:
            if book ["title"].lower() == book_title.lower():
                self.book_list.remove(book)
                self.save_to_file()
                print("Book remove Successfully\n")
                return
            print("Book not found")

    def find_book(self):

        search_type = input("search by \n1: Title\n2. Author\n Enter your chooice: ")
        search_text = input("Enter search term ").lower()
        founds_books =[
            book 
            for book in self.book_list
            if search_type in book["title"].lower()
            or search_text in book["author"].lower()
        ]

        if founds_books:
            print("Matching Books: ")
            for index , book in enumerate(founds_books , 1):
                reading_status = "Read" if book["read"] else "unread"
                print(
                    f"{index}. ===== {book['title']} by {book['author']}({book['year']}) - {book['genre']} - {reading_status}"
                )
        else:
            print("============No matching books found\n==================")

    def update_book(self):
        book_title = input("Enter the title of the book you want to edit: ")
        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                print("leave blank to keep existing value")
                book['title'] = input(f"New title ({book['title']}):") or book['title']
                book['author'] =(
                    input(f"New book author ({book['author']}): ") or book['author']
                )
                book['year'] = input(f"New year ({book['year']}):") or book['year']
                book['genre'] = input(f"New genre ({book['genre']}):") or book['genre']
                book['read'] =(
                    input("Have you read this book? (yes/no):").strip().lower() == 'yes'
                )
                self.save_to_file()
                print("Book updated successfuly")
                return
            print("Book not Found!\n")

    def start_application(self):
        while True:
            print("Welcome to your Book Collection Manager")
            print("1. Add a new Book")
            print("2. remove a Book")
            print("3. search for Book")
            print("4. Updated Book Details")
            print("5. Exist")
            user_choice = input("Please choose an option(1 - 7): ")

            if user_choice == "1":
                self.create_new_book()
            elif user_choice == "2":
                self.delete_book()
            elif user_choice == "3":
                self.find_book()
            elif user_choice == "4":
                self.update_book()
            elif user_choice == "5":
                self.save_to_file()
                print("Thank you for using Book Collection Maanager Good Bye!")
                break 
            else:
                print("Invalid choice please try again\n")


if __name__ : "__main__"
book_manager = BookCollection()
book_manager.start_application()
  
            
            

