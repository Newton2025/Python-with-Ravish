class Library:
    def __init__(self):
        self.book_name=""
        self.bookid=0
        self.price=0

    def set_book_name(self,book_name):
        self.book_name=book_name

    def get_book_name(self):
        return self.book_name
           
    def set_bookid(self,book_id):
        self.bookid=book_id
        
    def get_bookid(self):
        return self.bookid

    def set_price(self,price):
        self.price=price
        
    def get_price(self):
        return self.price

    def get_book_info(self):
        book_info = {}
        book_info["Name"]=self.book_name
        book_info["Book_ID"]=self.bookid
        book_info["Price"]=self.price
        return book_info

    # def display_books(self):
    #     print(self.book_info)

book1= Library()

book1.set_book_name("spiderman")
book1.set_bookid("15266")
book1.set_price("250.99")

print(book1.get_book_info())



