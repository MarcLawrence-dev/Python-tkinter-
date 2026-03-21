import tkinter as tk

root = tk.Tk()

tk.Label(root, text="Username").grid(row=0, column=0)
tk.Entry(root).grid(row=0, column=1)

tk.Label(root, text="Password").grid(row=1, column=0)
tk.Entry(root).grid(row=1, column=1)

root.mainloop()