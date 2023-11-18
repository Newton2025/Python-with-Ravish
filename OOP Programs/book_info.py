class Books:
    def __init__(self):
        self.bookid=14552
        self.title="Codewithcoder"
        self.price=1299.99
        self.author="Gaurav"
    def book_detail(self):
        print(self.bookid)
        print(self.title)
        print(self.price)
        print(self.author)
book=Books()

book.book_detail()
