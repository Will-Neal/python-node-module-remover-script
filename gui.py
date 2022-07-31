import tkinter as tk

HEIGHT = 450
WIDTH = 600

root = tk.Tk()

canvas = tk.Canvas(root, bg='#19194d', height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#232323')
frame.place(relx=0.1,rely=0.1, relwidth=0.8, relheight=0.8)

label = tk.Label(frame, bg='#bb86fc', text='No_Mo')
label.place(relx=0.4, rely=.05, relwidth=.2, relheight=.1)
 
seeButton = tk.Button(frame, bg='#03dac6', text="See Node_Modules")
seeButton.place(relx=0.2, rely=0.2, relwidth=.3, relheight=.09)

deleteButton = tk.Button(frame, bg='#cf6679', text="Delete Node_Modules")
deleteButton.place(relx=0.5, rely=0.2, relwidth=.3, relheight=.09)

seeJsonButton = tk.Button(frame, bg='#03dac6', text="See Package-Lock.jsons")
seeJsonButton.place(relx=0.2, rely=0.35, relwidth=.3, relheight=.09)

deleteJsonButton = tk.Button(frame, bg='#cf6679', text="Delete Node_Modules")
deleteJsonButton.place(relx=0.5, rely=0.35, relwidth=.3, relheight=.09)

root.mainloop()