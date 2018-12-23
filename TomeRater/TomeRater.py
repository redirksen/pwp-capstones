# This is create a user. Name and email are both strings
class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        # address needs to be a string
        if self.email != address:
            self.email = address
            print('Email has been changed to ' + address)

    def __repr__(self):
        return('User:' + str(self.name) + ' Email:' + str(self.email) + ' Books Read:' + str(len(self.books)))

    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.email

    def read_book(self, book, rating = None):
        self.books[book] = rating

    def get_average_rating(self):
        rating = 0
        count = 0
        for value in self.books.values():
            if value is not None:
                rating += value
                count += 1
        average = rating / count
        return average

# This is to create a Book
class Book:
    # title will be a string
    # isbn will be a int
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def __repr__ (self):
        return str(self.title)

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        if self.isbn != new_isbn:
            self.isbn = new_isbn

    def add_rating(self, rating):
        if rating >= 0 and rating <=4:
            self.ratings.append(rating)
        else:
            print('Invalid Rating')

    def __eq__(self, other):
        return self.title == other.title and self.isbn == other.isbn

    def get_average_rating(self):
        rating = 0
        if self.ratings == []:
            return 0
        for value in self.ratings:
                rating += value
        average = rating / len(self.ratings)
        return average

    def __hash__(self):
        return hash((self.title, self.isbn))

# This creates a fiction class of Book. author and title should be str
class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__ (self):
        return str(self.title) + ' by ' + str(self.author)

# This crates a Non-Fiction type book. Subject and level are strings
class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return str(self.title) + ', a ' + str(self.level) + ' manual on ' + str(self.subject)

class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        return Book(title,isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating = None):
        temp_user = self.users.get(email)
        if temp_user is None:
            print('no user with email ' + str(email) + '.')
        else:
            temp_user.read_book(book, rating)
            if rating is not None:
                book.add_rating(rating)
            if book in self.books.keys():
                self.books[book] = self.books[book] + 1
            else:
                self.books[book] = 1

    def add_user(self, name, email, user_books = None):
        if email in self.users.keys():
            print("An account with the email " + str(email) + " already exists.")
            return
        self.users[email] = User(name, email)
        if user_books is not None:
            for item in user_books:
                self.add_book_to_user(item, email)

    def print_catalog(self):
        for book in self.books.keys():
            print(book)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def most_read_book(self):
        most_read = None
        read_count = 0
        for book, count in self.books.items():
            if count > read_count:
                most_read = book
                read_count = count
        return most_read

    def highest_rated_book(self):
        highest_rated = None
        rating = 0
        for book in self.books.keys():
            if book.get_average_rating() > rating:
                highest_rated = book
                rating = book.get_average_rating()
        return highest_rated

    def most_positive_user(self):
        highest_rater = None
        rating = 0
        for user in self.users.values():
            if user.get_average_rating() > rating:
                highest_rater = user
                rating = user.get_average_rating()
        return highest_rater


