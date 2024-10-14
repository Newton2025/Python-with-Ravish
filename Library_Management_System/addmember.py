from tkinter import *
from tkinter import messagebox
import sqlite3

con = sqlite3.connect('library.db')
cur = con.cursor()

def add_member():
    name = ent_name.get()
    phone = ent_phone.get()

    if name and phone:
        try:
            query = "INSERT INTO members (member_name, member_phone) VALUES (?, ?)"
            cur.execute(query, (name, phone))
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
root.title("Add Member")
root.resizable(False, False)

topFrame = Frame(root, height=150, bg='white')
topFrame.pack(fill=X)

bottomFrame = Frame(root, height=600, bg='#fcc324')
bottomFrame.pack(fill=X)

top_image = PhotoImage(file='icons/addperson.png')
top_image_lbl = Label(topFrame, image=top_image, bg='white')
top_image_lbl.place(x=120, y=10)

heading = Label(topFrame, text='  Add Person ', font='arial 22 bold', fg='#003f8a', bg='white')
heading.place(x=290, y=60)

lbl_name = Label(bottomFrame, text='Name :', font='arial 15 bold', fg='white', bg='#fcc324')
lbl_name.place(x=40, y=40)
ent_name_default_text = 'Please enter a name'
ent_name = Entry(bottomFrame, width=30, bd=4, fg='grey')
ent_name.insert(0, ent_name_default_text)
ent_name.place(x=150, y=45)
ent_name.bind("<FocusIn>", lambda event: on_entry_click(ent_name, ent_name_default_text))
ent_name.bind("<FocusOut>", lambda event: on_entry_leave(ent_name, ent_name_default_text))

lbl_phone = Label(bottomFrame, text='Phone :', font='arial 15 bold', fg='white', bg='#fcc324')
lbl_phone.place(x=40, y=80)
ent_phone_default_text = 'Please enter phone number'
ent_phone = Entry(bottomFrame, width=30, bd=4, fg='grey')
ent_phone.insert(0, ent_phone_default_text)
ent_phone.place(x=150, y=85)
ent_phone.bind("<FocusIn>", lambda event: on_entry_click(ent_phone, ent_phone_default_text))
ent_phone.bind("<FocusOut>", lambda event: on_entry_leave(ent_phone, ent_phone_default_text))

button = Button(bottomFrame, text='Add Member', command=add_member)
button.place(x=270, y=120)

root.mainloop()
