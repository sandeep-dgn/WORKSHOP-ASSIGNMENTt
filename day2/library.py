class Book:
    def __init__(self, title, author, price, stock):
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock

    def show_book_info(self):
        print(f"Name: {self.title}, Author: {self.author}, Price: {self.price}, Stock: {self.stock}")

class User:
    def __init__(self, name, email, user_id):
        self.name = name
        self.email = email
        self.user_id = user_id

    def show_my_info(self):
        print(f"Name: {self.name}, Email: {self.email}, ID: {self.user_id}")

class Librarian(User):
    def __init__(self, name, email, user_id):
        super().__init__(name, email, user_id)

    def add_book(self, books, title, author, price, stock):
        for book in books:
            if book.title == title and book.author == author:
                book.stock += stock
                print(f"Stock of '{title}' by {author} increased by {stock}. New stock: {book.stock}\n")
                return
        books.append(Book(title, author, price, stock))
        print(f"Book '{title}' by {author} added successfully.\n")

    def remove_book(self, books, title, author):
        for book in books:
            if book.title == title and book.author == author:
                books.remove(book)
                print(f"Book '{title}' by {author} removed from the library.\n")
                return
        print(f"Book '{title}' by {author} not found in the system.\n")

    def show_all_books(self, books):
        print("\nBooks in the system:")
        if books:
            for book in books:
                book.show_book_info()
        else:
            print("No books available in the system.\n")

class Student(User):
    def __init__(self, name, email, user_id):
        super().__init__(name, email, user_id)

    def request_book(self, books, requests, title):
        for book in books:
            if book.title == title:
                if book.stock > 0:
                    requests.append({"Requested_By": self.name, "Book": title})
                    print(f"Request for '{title}' submitted by {self.name}.")
                    return
                else:
                    print(f"Sorry, the book '{title}' is out of stock.")
                    return
        print(f"Book '{title}' not found in the system.")

if __name__ == "__main__":
    books = []
    requests = []

    lib = Librarian("Sasank", "sasank@lib.com", "L001")
    lib.add_book(books, "MUNA MADAN", "LAXMI PRASAD DEVKOTA", 200, 10)
    lib.add_book(books, "MANSAROVAR", "BP KOIRALA", 150, 5)
    lib.add_book(books, "JIVAN KADA KI PHOOL", "GHAMAK KUMARI GHIMIRA", 100, 3)

    students = [
        Student("Sandeep", "sandeep@student.com", "S001"),
        Student("Aakash", "aakash@student.com", "S002"),
        Student("Bishal", "bishal@student.com", "S003"),
        Student("Bibek", "bibek@student.com", "S004"),
        Student("Bipin", "bipin@student.com", "S005")
    ]

    print("Welcome to the Library Management System")
    role = input("Are you a Student or Librarian? (Enter 'S' for Student, 'L' for Librarian): ")

    if role == 'l':
        print("\nYou are logged in as Librarian.")
        lib.show_my_info()

        while True:
            print("\n1. Add Book\n2. Remove Book\n3. Increase Book Stock\n4. Show All Books\n5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                price = float(input("Enter book price: "))
                stock = int(input("Enter book stock: "))
                lib.add_book(books, title, author, price, stock)

            elif choice == '2':
                title = input("Enter book title to remove: ")
                author = input("Enter book author to remove: ")
                lib.remove_book(books, title, author)

            elif choice == '3':
                title = input("Enter book title to increase stock: ")
                author = input("Enter book author to increase stock: ")
                stock = int(input("Enter number of copies to add to stock: "))
                lib.add_book(books, title, author, 0, stock)  # Price is set to 0 for stock increase

            elif choice == '4':
                lib.show_all_books(books)

            elif choice == '5':
                print("Exiting Librarian's dashboard.")
                break
            else:
                print("Invalid choice! Please try again.")

    elif role == 's':
        print("\nYou are logged in as Student.")
        student_name = input("Enter your name: ")
        student_found = False
        for student in students:
            if student.name == student_name:
                student.show_my_info()
                student_found = True
                break

        if not student_found:
            print("Student not found. Please check your name and try again.")
        else:
            while True:
                print("\n1. Request a Book\n2. Exit")
                choice = input("Enter your choice: ")

                if choice == '1':
                    title = input("Enter book title to request: ")
                    student.request_book(books, requests, title)
                elif choice == '2':
                    break
                else:
                    print("Invalid choice! Please try again.")

    else:
        print("Invalid role! Please enter 'S' for Student or 'L' for Librarian.")
