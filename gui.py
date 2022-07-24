import tkinter as tk

HEIGHT = 700
WIDTH = 800

root = tk.Tk()

canvas = tk.Canvas(root, bg='#d9d9d9', height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#e6ffff')
frame.place(relx=0.1,rely=0.1, relwidth=0.8, relheight=0.8)

label = tk.Label(root, bg='#999999', text='No_Modules')
label.place(relx=0.4, rely=0, relwidth=.2, relheight=.1)
 
seeButton = tk.Button(frame, bg='#d9d9d9', text="See Node_Modules")
seeButton.place(relx=0.2, rely=0.25, relwidth=.2, relheight=.05)

deleteButton = tk.Button(frame, bg='#d9d9d9', text="Delete Node_Modules")
deleteButton.place(relx=0.6, rely=0.25, relwidth=.2, relheight=.05)

seeJsonButton = tk.Button(frame, bg='#d9d9d9', text="See Package-Lock.jsons")
seeJsonButton.place(relx=0.2, rely=0.35, relwidth=.2, relheight=.05)

deleteJsonButton = tk.Button(frame, bg='#d9d9d9', text="Delete Node_Modules")
deleteJsonButton.place(relx=0.6, rely=0.35, relwidth=.2, relheight=.05)

root.mainloop()