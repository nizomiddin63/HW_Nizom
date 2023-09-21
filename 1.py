class Book:
    def __init__(self, title, authors, price, publishing_house):
        self.title = title
        self.authors = authors
        self.price = price
        self.publishing_house = publishing_house

    def input_book_info(self):
    print("\n*****\n")
        self.title = input("Kitob nomi: ")
        self.authors = input("Kitob Mualliflari: ").split(",")
        self.price = float(input("Kitob narxi: "))
        self.publishing_house = input("Kitob nashriyoti: ")

    def print_book_info(self):
        print("Kitob nomi:", self.title)
        print("Kitob Mualliflari:", self.authors)
        print("Kitob narxi:", self.price)
        print("Kitob nashriyoti:", self.publishing_house)

    def is_published_by_a_h(self):
        return self.publishing_house.startswith("A") or self.publishing_house.startswith("B") or self.publishing_house.startswith("C") or self.publishing_house.startswith("D") or self.publishing_house.startswith("E") or self.publishing_house.startswith("F") or self.publishing_house.startswith("G") or self.publishing_house.startswith("H")

def main():
    books = []
    for i in range(5):
        book = Book("", [], 0, "")
        book.input_book_info()
        books.append(book)

    books_published_by_a_h = []
    for book in books:
        if book.is_published_by_a_h():
            books_published_by_a_h.append(book)

    for book in books_published_by_a_h:
        book.print_book_info()

if __name__ == "__main__":
    main()
