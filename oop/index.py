class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return "This is the instance for object " + self.title

    def get_book_details(self):
        return 'The book ' + self.title + ' is written by ' + self.author

    def lend_count(self,number):
        return 'Book ' + self.title + ' has ' + str(number) + ' lends'