import tkinter as tk
import os
from tkinter import messagebox
from second import *

window = tk.Tk() #Creating window
window.geometry('690x420')
window.title("PMS")
window.configure(bg="#a7cbf2")

f = "saved_data.pkl"
if os.path.exists(f): #If file exists then it will read the file
    lst = list(readList(f))
else:
    lst = []

window.counter = 0 #counter is initialzed to 0

def clear():
    #===This function is used to clear all the entry fields===

    prod_id_Entry.config(state='normal')
    prod_id_Entry.delete(0,"end")
    name_Entry.delete(0,"end")
    price_Entry.delete(0,"end")
    quantity_Entry.delete(0,"end")
    company_Entry.delete(0,'end')


def display():
    #===display the complete list===

    print("<====List of products====>")
    for i in lst:
        print(i.pid, i.name, i.price, i.stock, i.company)

def addnew2():
    if (prod_id_Entry.get()!=" " and name_Entry.get()!=" " and price_Entry.get()!=" " and quantity_Entry.get()!=" " and
            company_Entry.get()):#checks if user has left any field empty
        res = addnew(lst,prod_id_Entry.get(),name_Entry.get(),price_Entry.get(),quantity_Entry.get(),
               company_Entry.get())
        if res: #This condition is when there is no same product id present
            messagebox.showinfo("Note","Added")
        else: #When there is an existing product id
            messagebox.showwarning("Note","Product Id already present")
    else:#if user has left any field blank
        messagebox.showwarning("Note","Please fill all the boxes")
    clear()

def upd():
    flag=0
    if window.counter==0:#If it is the first click
        for i in lst:
            if i.pid==prod_id_Entry.get():
                x = prod_id_Entry.get()
                clear() #so that anything entered by user is first cleared
                prod_id_Entry.insert(1,x)
                prod_id_Entry.config(state='disable') #So that user cannot change the Id
                name_Entry.insert(1,i.name)
                price_Entry.insert(1,i.price)
                quantity_Entry.insert(1,i.stock)
                company_Entry.insert(1,i.company)
                window.counter+=1
                flag = 1
                break
        if flag!=1:#If pid not present
            messagebox.showwarning("Note","Product Id not present")
            clear()
        else:
            pass
    elif window.counter==1:#When there is a second click
        update(lst,prod_id_Entry.get(),name_Entry.get(),price_Entry.get(),
               quantity_Entry.get(),company_Entry.get())
        window.counter-=1 #counter is made to 0 so that the next click again becomes the first click
        messagebox.showinfo("Note","Updated")
        clear()


def delete1():
    msg = messagebox.askyesno("Note","Are you sure you want to delete".format(prod_id_Entry.get()))
    if msg:#if user clicks yes
        res = delete(lst,prod_id_Entry.get())
        if res:#if Id is present
            messagebox.showinfo("Note","Deleted product with Id {}".format(prod_id_Entry.get()))
            clear()
        else: #if Id is not present
            messagebox.showwarning("Note","Product Id not present")
            clear()
    else:
        clear()


def save1():
    saveList(f,lst)
    messagebox.showinfo("Note","Data has been saved")


tk.Label(window,text="PRODUCT MANAGEMENT SYSTEM",font="bold 25",bg="#a7cbf2").grid(row = 0,column=2,pady=(0,15))

prod_id_Label = tk.Label(window,text="Product Id",font="10",bg="#a7cbf2")
name_Label = tk.Label(window,text="Name",bg="#a7cbf2")
price_Label = tk.Label(window,text="Price",bg="#a7cbf2")
quantity_Label = tk.Label(window,text="Quantity",bg="#a7cbf2")
company_Label = tk.Label(window,text = "Company",bg="#a7cbf2")

prod_id_Entry = tk.Entry(window,borderwidth=3,highlightbackground='#58bbed')
name_Entry = tk.Entry(window,borderwidth=3,highlightbackground='#58bbed')
price_Entry = tk.Entry(window,borderwidth=3,highlightbackground='#58bbed')
quantity_Entry = tk.Entry(window,borderwidth=3,highlightbackground='#58bbed')
company_Entry = tk.Entry(window,borderwidth=3,highlightbackground='#58bbed')

prod_id_Label.grid(row=2,column=1)
name_Label.grid(row = 3,column = 1)
price_Label.grid(row = 4,column = 1)
quantity_Label.grid(row=5,column=1)
company_Label.grid(row=6,column=1)

prod_id_Entry.grid(row=2,column=2)
name_Entry.grid(row=3,column=2)
price_Entry.grid(row=4,column=2)
quantity_Entry.grid(row=5,column=2)
company_Entry.grid(row=6,column=2)


btn_add = tk.Button(window,text="Add",background="blue",command=addnew2,highlightbackground='#58bbed')
btn_update = tk.Button(window,text="Update",command=upd,highlightbackground='#58bbed')
btn_del = tk.Button(window,text="Delete",command=delete1,highlightbackground='#58bbed')
btn_save = tk.Button(window,text="Save",command=save1,highlightbackground='#58bbed')
btn_display = tk.Button(window,text="Display",command=display,highlightbackground='#58bbed')


btn_add.place(x=75,y=250)
btn_update.place(x=135,y=250)
btn_del.place(x=215,y=250)
btn_save.place(x=285,y=250)
btn_display.place(x=345,y=250)

window.mainloop()
