import tkinter as tk
from tkinter import messagebox, ttk


import sqlite3
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        password TEXT,
        gender TEXT,
        address TEXT,
        age INTEGER
    )
""")


window = tk.Tk()
window.title("widget nang cao")
window.geometry("400x300")

def dang_ky():
    if entry1 == "":
        messagebox.showwarning("cui lòng nhaập đủ thông tin")
    elif entry2 == "":
        messagebox.showwarning("vui lòng nhập d8ủ thông tin")
    else:
        name = entry1.get()
        password = entry2.get()
        gender1 = gender.get()
        address = combobox.get()
        age = age_box.get()
        cursor.execute("""
            INSERT INTO users(name,password,gender,address,age) VALUES
            (?,?,?,?,?)
        """,(name,password,gender1,address,int(age)))
        conn.commit()
        messagebox.showinfo("Info","Đăng ký thành công")

lb1 = tk.Label(window,text="tên:")
lb1.pack()

entry1 = tk.Entry(window)
entry1.pack()

lb2 = tk.Label(window,text="mật khẩu:")
lb2.pack()

entry2 = tk.Entry(window)
entry2.pack()

lb3 = tk.Label(window,text="giới tính:")
lb3.pack()

gender = tk.StringVar()
nam_button = tk.Radiobutton(window,text="Nam",variable=gender,value="Male")
nam_button.pack()
nu_button = tk.Radiobutton(window,text="Nữ",variable=gender,value="Female")
nu_button.pack()

lb4 = tk.Label(window,text="địa chỉ:")
lb4.pack()

combobox = ttk.Combobox(window,value=["Hà Nội","HCM","Đà Nẵng","Vũng Tàu","Đà Lạt"])
combobox.pack()
lb5 = tk.Label(window,text="Tuổi:")
lb5.pack()
age_box = tk.Spinbox(window, from_=1, to=200)
age_box.pack()

button = tk.Button(window,text="đăng ký",command=dang_ky)
button.pack()

window.mainloop()
conn.close()