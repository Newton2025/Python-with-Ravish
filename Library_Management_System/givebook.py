from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox

con = sqlite3.connect('library.db')
cur = con.cursor()

def give_book():
    book_name = book_var.get().split('-')[0]
    member_name = member_var.get().split('-')[0]

    if book_name and member_name:
        try:
            query = "INSERT INTO borrows (bbook_id, bmember_id) VALUES (?, ?)"
            cur.execute(query, (book_name, member_name))
            con.commit()
            messagebox.showinfo("Success", "Successfully added to database!", icon='info')
            cur.execute("UPDATE books SET book_status = ? WHERE book_id = ?", (1, book_name))
            con.commit()
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
root.title("Give Book")
root.resizable(False, False)

query_books = "SELECT * FROM books WHERE book_status = 0"
books = cur.execute(query_books).fetchall()
book_list = [f"{book[0]}-{book[1]}" for book in books]

query_members = "SELECT * FROM members"
members = cur.execute(query_members).fetchall()
member_list = [f"{member[0]}-{member[1]}" for member in members]

topFrame = Frame(root, height=150, bg='white')
topFrame.pack(fill=X)

bottomFrame = Frame(root, height=600, bg='#fcc324')
bottomFrame.pack(fill=X)

top_image = PhotoImage(file='icons/addbook.png')
top_image_lbl = Label(topFrame, image=top_image, bg='white')
top_image_lbl.place(x=120, y=10)

heading = Label(topFrame, text=' Give a Book ', font='arial 22 bold', fg='#003f8a', bg='white')
heading.place(x=290, y=60)

book_var = StringVar()
lbl_name = Label(bottomFrame, text='Book: ', font='arial 15 bold', fg='white', bg='#fcc324')
lbl_name.place(x=40, y=40)
combo_name = ttk.Combobox(bottomFrame, textvariable=book_var)
combo_name['values'] = book_list
combo_name.place(x=150, y=45)

member_var = StringVar()
lbl_phone = Label(bottomFrame, text='Member: ', font='arial 15 bold', fg='white', bg='#fcc324')
lbl_phone.place(x=40, y=80)
combo_member = ttk.Combobox(bottomFrame, textvariable=member_var)
combo_member['values'] = member_list
combo_member.place(x=150, y=85)

button = Button(bottomFrame, text='Give Book', command=give_book)
button.place(x=270, y=200)

root.mainloop()
