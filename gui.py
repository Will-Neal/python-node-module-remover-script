import tkinter as tk

HEIGHT = 700
WIDTH = 800

root = tk.Tk()

canvas = tk.Canvas(root, bg='#d9d9d9', height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#e6ffff')
frame.place(relx=0.1,rely=0.1, relwidth=0.8, relheight=0.8)

button = tk.Button(frame, bg='#d9d9d9', text="See Node_Modules")
button.pack()

button = tk.Button(frame, bg='#d9d9d9', text="Delete Node_Modules")
button.pack()

root.mainloop()