import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Tuong tac voi widget")
window.geometry("800x800")

def ham_1():
    ten = entry1.get()
    print("Ten cua ban la", ten)
    tuoi = entry2.get()
    print("Ban", tuoi,"tuoi")
    lop = entry3.get()
    print("Ban hoc lop", lop)
    messagebox.showinfo("Thong bao",
                    f"Ten cua ban la: {ten} \n Tuoi cua ban la: {tuoi} \n Ban hoc lop: {lop}")

lb1 = tk.Label(window,text="Ho va ten")
lb1.pack()

entry1 = tk.Entry(window,width=50)
entry1.pack()

lb2 = tk.Label(window,text="Nhap lop")
lb2.pack()

entry2 = tk.Entry(window,width=50)
entry2.pack()

lb3 = tk.Label(window,text="Nhap tuoi")
lb3.pack()

entry3 = tk.Entry(window,width=50)
entry3.pack()

btn = tk.Button(window,text="Print", command=ham_1)
btn.pack()
window.mainloop()