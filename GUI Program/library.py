import tkinter as tk
from tkinter import Label, Entry, Button

class Library:
    def __init__(self):
        self.book_name = ""
        self.bookid = 0
        self.price = 0

    def set_book_name(self, book_name):
        self.book_name = book_name

    def get_book_name(self):
        return self.book_name

    def set_bookid(self, book_id):
        self.bookid = book_id

    def get_bookid(self):
        return self.bookid

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def get_book_info(self):
        book_info = {}
        book_info["Name"] = self.book_name
        book_info["Book_ID"] = self.bookid
        book_info["Price"] = self.price
        return book_info

class LibraryGUI:
    def __init__(self, master):
        self.master = master
        master.title("Library GUI")

        self.library = Library()

        self.label_name = Label(master, text="Book Name:")
        self.label_id = Label(master, text="Book ID:")
        self.label_price = Label(master, text="Book Price:")

        self.entry_name = Entry(master)
        self.entry_id = Entry(master)
        self.entry_price = Entry(master)

        self.label_name.grid(row=0, column=0)
        self.label_id.grid(row=1, column=0)
        self.label_price.grid(row=2, column=0)

        self.entry_name.grid(row=0, column=1)
        self.entry_id.grid(row=1, column=1)
        self.entry_price.grid(row=2, column=1)

        self.button_get_info = Button(master, text="Get Book Info", command=self.display_book_info)
        self.button_get_info.grid(row=3, column=0, columnspan=2)

        # Label to display book info
        self.label_book_info = Label(master, text="")
        self.label_book_info.grid(row=4, column=0, columnspan=2)

    def display_book_info(self):
        book_name = self.entry_name.get()
        book_id = self.entry_id.get()
        book_price = self.entry_price.get()

        self.library.set_book_name(book_name)
        self.library.set_bookid(book_id)
        self.library.set_price(book_price)

        book_info = self.library.get_book_info()
        info_text = f"Book Info: {book_info}"
        self.label_book_info.config(text=info_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryGUI(root)
    root.mainloop()
