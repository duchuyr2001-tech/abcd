import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Quan ly cong viec")
window.geometry("800x500")

def them_ten_lop_truong():
    ten = entry1.get()
    lop = entry2.get()
    truong = entry3.get()
    if ten != "":
        messagebox.showinfo("Thong bao",f"Da them {ten}")
    elif lop != "":
        messagebox.showinfo("Thong bao",f"Da them {lop}")
    elif truong != "":
        messagebox.showinfo("Thong bao",f"Da them {truong}")
    else:
        messagebox.showwarning("Loi","Vui long nhap day di thong tin cua ban")
        


label1 = tk.Label(window,text="Nhap ten cua ban")
label1.pack(side=tk.TOP, pady=10)

entry1 = tk.Entry(window,width=40)
entry1.pack(side=tk.TOP, padx= 20, pady= 10)

label2 = tk.Label(window,text="Nhap lop cua ban")
label2.pack(side=tk.TOP, pady=10)

entry2 = tk.Entry(window,width=40)
entry2.pack(side=tk.TOP, padx= 20, pady= 10)

label3 = tk.Label(window,text="Nhap truong cua ban")
label3.pack(side=tk.TOP, pady=10)

entry3 = tk.Entry(window,width=40)
entry3.pack(side=tk.TOP, padx= 20, pady= 10)

button = tk.Button(window,text="Press", command=them_ten_lop_truong)
button.pack(side=tk.TOP, fill=tk.X,pady=10)

window.mainloop()