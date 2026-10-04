#tkinter

import tkinter as tk 
from tkinter import messagebox
window = tk.Tk()
window.title("Bai 1")
window.geometry("400x300")
def ham():
    messagebox.showinfo("title thong bao", "You got virus")
#widget (label, button, entry)
btn1 = tk.Button(window, text="Press", command= ham)
btn1.pack()
window.mainloop()