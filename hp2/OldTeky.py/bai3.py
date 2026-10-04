import tkinter as tk

window = tk.Tk()
window.title("Bai 3")
window.geometry("600x600")

label = tk.Label(window, text="Hello")
label.pack(side=tk.LEFT)

label1 = tk.Label(window, text="World")
label1.pack(side=tk.LEFT)

label2 = tk.Label(window, text="World")
label2.pack(side=tk.RIGHT)
#fill
entry1 = tk.Entry(window)
entry1.pack(fill=tk.BOTH)
button1 = tk.Button(window,text="Press")
button1.pack(pady=10)
#pad


window.mainloop()