from tkinter import *
from tkinter import messagebox
import sqlite3

con = sqlite3.connect('library.db')
cur = con.cursor()

def add_book(ent_search=None):
    name = ent_name.get()
    author = ent_author.get()
    page = ent_page.get()
    language = ent_language.get()

    print(name + author +page + language )

    if name and author and page and language:
        try:
            query = "INSERT INTO books (book_name, book_author, book_page, book_language) VALUES (?, ?, ?, ?)"
            cur.execute(query, (name, author, page, language))
            print("Query Executed")
            con.commit()
            messagebox.showinfo("Success", "Successfully added to database", icon='info')

        except:
            messagebox.showerror("Error", "Can't add to database", icon='warning')
    else:
        messagebox.showerror("Error", "Fields can't be empty", icon='warning')


def on_entry_click(entry_widget, default_text):
    if entry_widget.get() == default_text:
        entry_widget.delete(0, END)
        entry_widget.config(fg='black')

def on_entry_leave(entry_widget, default_text):
    if not entry_widget.get():
        entry_widget.insert(0, default_text)
        entry_widget.config(fg='grey')

root = Tk()
root.geometry("520x420")
root.title("Add Book")
root.resizable(False, False)

# Top Frame
topFrame = Frame(root, height=150, bg='white')
topFrame.pack(fill=X)

# Bottom Frame
bottomFrame = Frame(root, height=600, bg='#fcc324')
bottomFrame.pack(fill=X)

# Heading, image
top_image = PhotoImage(file='icons/addbook.png')
top_image_lbl = Label(topFrame, image=top_image, bg='white')
top_image_lbl.place(x=120, y=10)
heading = Label(topFrame, text='  Add Book ', font='arial 22 bold', fg='#003f8a', bg='white')
heading.place(x=290, y=60)

# Entries and Labels

# Name
lbl_name = Label(bottomFrame, text='Name :', font='arial 15 bold', fg='white', bg='#fcc324')
lbl_name.place(x=40, y=40)
ent_name_default_text = 'Please enter a book name'
ent_name = Entry(bottomFrame, width=30, bd=4, fg='grey')
ent_name.insert(0, ent_name_default_text)
ent_name.place(x=150, y=45)
ent_name.bind("<FocusIn>", lambda event: on_entry_click(ent_name, ent_name_default_text))
ent_name.bind("<FocusOut>", lambda event: on_entry_leave(ent_name, ent_name_default_text))

# Author
lbl_author = Label(bottomFrame, text='Author :', font='arial 15 bold', fg='white', bg='#fcc324')
lbl_author.place(x=40, y=80)
ent_author_default_text = 'Please enter an author name'
ent_author = Entry(bottomFrame, width=30, bd=4, fg='grey')
ent_author.insert(0, ent_author_default_text)
ent_author.place(x=150, y=85)
ent_author.bind("<FocusIn>", lambda event: on_entry_click(ent_author, ent_author_default_text))
ent_author.bind("<FocusOut>", lambda event: on_entry_leave(ent_author, ent_author_default_text))

# Page
lbl_page = Label(bottomFrame, text='Page :', font='arial 15 bold', fg='white', bg='#fcc324')
lbl_page.place(x=40, y=120)
ent_page_default_text = 'Please enter page size'
ent_page = Entry(bottomFrame, width=30, bd=4, fg='grey')
ent_page.insert(0, ent_page_default_text)
ent_page.place(x=150, y=125)
ent_page.bind("<FocusIn>", lambda event: on_entry_click(ent_page, ent_page_default_text))
ent_page.bind("<FocusOut>", lambda event: on_entry_leave(ent_page, ent_page_default_text))

# Language
lbl_language = Label(bottomFrame, text='Language :', font='arial 15 bold', fg='white', bg='#fcc324')
lbl_language.place(x=40, y=160)
ent_language_default_text = 'Please enter a Language'
ent_language = Entry(bottomFrame, width=30, bd=4, fg='grey')
ent_language.insert(0, ent_language_default_text)
ent_language.place(x=150, y=165)
ent_language.bind("<FocusIn>", lambda event: on_entry_click(ent_language, ent_language_default_text))
ent_language.bind("<FocusOut>", lambda event: on_entry_leave(ent_language, ent_language_default_text))

# Button
button = Button(bottomFrame, text='Add Book', command=add_book)
button.place(x=270, y=200)

root.mainloop()
