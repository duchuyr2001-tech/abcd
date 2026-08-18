import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Bai 1 - Lam quen voi tkinter")
window.geometry("500x300")

def insert():
    ten = entry1.get()
    if ten != "":
        listbox.insert(tk.END,ten)
        entry1.delete(0,tk.END)
    else:
        messagebox.showwarning("Error","Vui long nhap du lieu")
    
def delete():
    vitri = listbox.curselection()
    if vitri:
        listbox.delete(vitri)
    else:
        messagebox.showwarning("Error","Vui long chon de xoa")
listbox = tk.Listbox(window)
listbox.pack()
listbox.insert(tk.END,"Duc Huy")

entry1 = tk.Entry(window)
entry1.pack()

btn1 = tk.Button(window, text="Insert", command=insert)
btn1.pack()

btn2 = tk.Button(window, text="Delete", command=delete)
btn2.pack()

window.mainloop()