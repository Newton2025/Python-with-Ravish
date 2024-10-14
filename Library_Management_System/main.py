from tkinter import *
import subprocess
from tkinter import ttk
import sqlite3

#Creating DataBase Object of Class "Connect" Which is Inside Library "sqlite"
con=sqlite3.connect('library.db')
cur=con.cursor()

#____________________________Function To Call Other Programs____________________
def addBook():
    print("Add Book Called")
    subprocess.Popen(['python', 'addbook.py'])

def addmember():
    print("Add memeber Called")
    subprocess.Popen(['python', 'addmember.py'])
def givebook():
     print("Give Book Called")
     subprocess.Popen(['python', 'givebook.py'])
#____________________________Function To Call Other Programs End Here____________________

#__________________Display All Books/Memeber in Libraray Status Function__________________
def displayStatistics():
        count_books=cur.execute("SELECT count(book_id) FROM books").fetchall()
        count_members = cur.execute("SELECT count(member_id) FROM members").fetchall()
        taken_books = cur.execute("SELECT count(book_status) FROM books WHERE book_status=1").fetchall()
        print(count_books)
        lbl_book_count.config(text='Total :'+ str(count_books[0][0])+' books in library')
        lbl_member_count.config(text="Total member : "+str(count_members[0][0]))
        lbl_taken_count.config(text="Taken books :"+str(taken_books[0][0]))
        displayBooks()
#____________Display All Books/Memeber in Libraray Status Function End____________

#__________________________Display Books Name Function___________________________
def displayBooks():
        books=cur.execute("SELECT * FROM books").fetchall()
        count=0
        list_books.delete(0,END)
        for book in books:
            print(book)
            list_books.insert(count,str(book[0])+ "-" +book[1])
            count +=1
#__________________________Display Books Name Function End___________________________

#__________________________Display Books Detail Showing Function_____________________
def bookInfo(event=None):
    selection = list_books.curselection()
    if selection:
        id = list_books.get(selection[0]).split('-')[0]
        book = cur.execute("SELECT * FROM books WHERE book_id=?", (id,))
        book_info = book.fetchall()
        list_details.delete(0, 'end')
        list_details.insert(0, "Book Name : " + book_info[0][1])
        list_details.insert(1, "Author : " + book_info[0][2])
        list_details.insert(2, "Page : " + book_info[0][3])
        list_details.insert(3, "Language : " + book_info[0][4])
        status = "Available" if book_info[0][5] == 0 else "Not Available"
        list_details.insert(4, "Status : " + status)
#__________________________Display Books Detail Showing Function End____________________

#__________________________Display Search Book Function___________________________
def searchBook():
    search_text = ent_search.get()
    books = cur.execute("SELECT * FROM books WHERE book_name LIKE ?", ('%' + search_text + '%',)).fetchall()
    count = 0
    list_books.delete(0, END)
    for book in books:
        list_books.insert(count, str(book[0]) + "-" + book[1])
        count += 1
#__________________________Display Search Book Function End___________________________

#__________________________From Here GUI Program Starts_______________________________
win = Tk()
win.title("Library Management System")
win.geometry("1164x1160")
win.iconbitmap('icons/icon.ico')

#Created a Frame Inside win
mainFrame=Frame(win)
mainFrame.pack()

#Divided frame into 2 parts
# 1) TopFrame
topFrame= Frame(mainFrame,width=1099,height=64,bg='white',padx=34,relief=SUNKEN,borderwidth=2)
topFrame.pack(side=TOP,fill=X)

# 2) Center or middle frame
centerFrame = Frame(mainFrame,width=720,relief=RIDGE,bg='white',height=860)
centerFrame.pack(side=TOP)

#again #Divided main frame part2 into two part
# 1)centerleftframe
centerLeftFrame= Frame(centerFrame,width=720,height=860,bg='red',borderwidth=2,relief='sunken')
centerLeftFrame.pack(side=LEFT)

# 2) centerRightframe
centerRightFrame= Frame(centerFrame,width=720,height=860,bg='green',borderwidth=2,relief='sunken')
centerRightFrame.pack()

# In CenterRightframe we added -->>
# 1)Search -->> button,entry,labell,labelframe
search_bar =LabelFrame(centerRightFrame,width=352,height=60,text='Search Box',bg='#a0d2eb',pady=8)
search_bar.pack(fill=BOTH)

lbl_search=Label(search_bar,text='Search :', font='arial 10 bold',bg='#FFFFF0',fg='black')
lbl_search.grid(row=0,column=0,padx=16,pady=8)

ent_search=Entry(search_bar,width=24,bd=8)
ent_search.grid(row=0,column=1,columnspan=3,padx=8,pady=8)

btn_search=Button(search_bar,text='Search',font='arial 10',bg='#FFFFF0',fg='black')
btn_search.config(command=searchBook)
btn_search.grid(row=0,column=4,padx=16,pady=8)

# 1)Image -->> image,label
image_bar=Frame(centerRightFrame)
image_bar.pack(fill=BOTH)

title_right=Label(image_bar,text='Welcome to Digital Library',font='arial 18 bold')
title_right.grid(row=0)

img_library=PhotoImage(file='icons/library.png')
lblImg=Label(image_bar,image=img_library)
lblImg.grid(row=1)

# In Topframe we added -->>
# 3 image button addmember,addbook,givebook
iconbook=PhotoImage(file='icons/add_book.png')
btnbook= Button(topFrame,text='Add Book',image=iconbook,compound=LEFT,
                 font='arial 10 bold')
btnbook.config(command=addBook)
btnbook.pack(side=LEFT,padx=8)
iconmember= PhotoImage(file ='icons/users.png')
btnmember=Button(topFrame,text='Add Member',font='arial 10 bold',padx=8)
btnmember.config(command=addmember)
btnmember.configure(image=iconmember,compound=LEFT)
btnmember.pack(side=LEFT)
icongive=PhotoImage(file ='icons/givebook.png')
btngive=Button(topFrame,text='Give Book',font='arial 10 bold',padx=8,
                image=icongive,compound=LEFT)
btngive.config(command=givebook)
btngive.pack(side=LEFT)

# In CenterRightleft we added -->>
# 1) Notebook
tabs= ttk.Notebook(centerLeftFrame,width=720,height=528)
tabs.pack()
tab1_icon=PhotoImage(file='icons/books.png')
tab2_icon=PhotoImage(file='icons/members.png')
tab1=ttk.Frame(tabs)
tab2=ttk.Frame(tabs)
tabs.add(tab1,text='Library Management',image=tab1_icon,compound=LEFT)
tabs.add(tab2,text='Statistics',image=tab2_icon,compound=LEFT)

# 2) Creted a Listbox for viewing a books
list_books= Listbox(tab1,width=33,height=31,bd=4,font='times 10 bold')
sb=Scrollbar(tab1,orient=VERTICAL)
list_books.config(yscrollcommand=sb.set)
list_books.grid(row=0,column=0,padx=(8,0),pady=8,sticky=N)
sb.grid(row=0,column=0,sticky=N+S+E)

# 3) Creted a Listbox for viewing a books details
list_details=Listbox(tab1,width=64,height=31,bd=4,font='times 10 bold')
list_details.grid(row=0,column=1,padx=(8,0),pady=8,sticky=N)
list_books.bind("<<ListboxSelect>>", bookInfo)

# Exception Case when there is no book added or not connect to db it show
lbl_book_count= Label(tab2,text="Current Nothing Here",pady=16,font='verdana 11 bold')
lbl_book_count.grid(row=0)
lbl_member_count=Label(tab2,text="We Will Add Something",pady=16,font='verdana 11 bold')
lbl_member_count.grid(row=1,sticky=W)
lbl_taken_count=Label(tab2,text="Later Based Of Statistic",pady=16,font='verdana 11 bold')
lbl_taken_count.grid(row=2,sticky=W)

# calling this function
displayBooks()
displayStatistics()

win.mainloop()
