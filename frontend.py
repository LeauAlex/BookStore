"""
A program that stores book information:
Title, Author,
Year, ISBN

The user can:
View all records
Search and entry
Update an entry
Delete
Close
"""

from tkinter import *
from tkinter import messagebox
import Backend



def get_selected_row(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
    except IndexError:
        lambda : messagebox.showinfo(title="Info!", message="No intem in list")


def view_command():
    list1.delete(0, END)  # this will make sure that when you press view you will see only 1 list.
    for row in Backend.view():
        list1.insert(END, row)


def search_command():  # it must have the same parameters as in backend script
    list1.delete(0, END)
    for row in Backend.search(input_text.get(), input_author.get(), input_year.get(), input_ISBN.get()):
        list1.insert(END, row)


def insert_command():
    Backend.insert(input_text.get(), input_author.get(), input_year.get(), input_ISBN.get())
    list1.delete(0, END)
    list1.insert(END, (input_text.get(), input_author.get(), input_year.get(), input_ISBN.get()))
    view_command()


def delete_command():
    Backend.delete(selected_tuple[0])
    view_command()


def update_command():
    Backend.update(selected_tuple[0], input_text.get(), input_author.get(), input_year.get(), input_ISBN.get())
    view_command()


window = Tk(screenName = "BookStore")

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Year")
l2.grid(row=1, column=0)

l3 = Label(window, text="Author")
l3.grid(row=0, column=2)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

input_text = StringVar()
e1 = Entry(window, textvariable = input_text, width= 10)
e1.grid(row=0, column=1,)

input_author = StringVar()
e2 = Entry(window, textvariable=input_author, width=10)
e2.grid(row=1, column=1)

input_year = StringVar()
e3 = Entry(window, textvariable=input_year, width = 10)
e3.grid(row=0, column = 3,)

input_ISBN = StringVar()
e4 = Entry(window, textvariable = input_ISBN, width = 10)
e4.grid(row = 1, column = 3,)

list1 = Listbox(window, height= 10, width = 35)
list1.grid(row =2, column = 0, rowspan =8, columnspan = 2)

sb1=Scrollbar(window)
sb1.grid(row=2, column=2, rowspan = 6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)


list1.bind("<<ListboxSelect>>", get_selected_row)


b1 = Button(window, text = "View all",width = 10,command = view_command)
b1.grid(row =2 , column = 3)

b2 = Button(window, text = "Search Entry", width = 10, command = search_command)
b2.grid(row =3 , column = 3)

b3 = Button(window, text = "Add entry", width = 10, command = insert_command )
b3.grid(row =4 , column = 3)

b4 = Button(window, text = "Update", width = 10, command = update_command)
b4.grid(row =5 , column = 3)

b5 = Button(window, text = "Delete", width = 10, command = delete_command)
b5.grid(row =6 , column = 3)

b6 = Button(window, text = "Close", width = 10, command = window.destroy)
b6.grid(row =7 , column = 3)



window.mainloop()



if __name__ == '__main__':
    Tk()