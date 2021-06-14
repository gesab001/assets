import tkinter as tk
from tkinter import Text, ttk

root = tk.Tk()
container = ttk.Frame(root)
canvas = tk.Canvas(container)
scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

canvas.configure(yscrollcommand=scrollbar.set)

keys = ["Title", "Other Title", "Description", "Categories", "Book", "Chapter"]
keyspairs = {}


for i in range(0,5):
	key = keys[i]
	print(key)
	ttk.Label(scrollable_frame, text=key).pack()
	pair = ttk.Entry(scrollable_frame, width=50).pack()
	keyspairs[key] = pair
    
questionanswers = []    
for i in range(1,6):
    ttk.Label(scrollable_frame, text="Question"+str(i)).pack()
    question = Text(scrollable_frame, width=30, height=5).pack() 
    ttk.Label(scrollable_frame, text="Answer").pack()
    answer = ttk.Entry(scrollable_frame).pack() 
    ttk.Label(scrollable_frame, text="b").pack()
    b = ttk.Entry(scrollable_frame).pack() 
    ttk.Label(scrollable_frame, text="c").pack()
    c = ttk.Entry(scrollable_frame).pack() 
    ttk.Label(scrollable_frame, text="d").pack()
    d = ttk.Entry(scrollable_frame).pack()   
    data = {"question": question, "answer": answer, "b": b, "c": c, "d": d}
    questionanswers.append(data)          

def submit():
   #msg = messagebox.showinfo( "Hello Python", E1.get())
   title = pair.get()
   print(title)

B = ttk.Button(scrollable_frame, text = "Submit", command = submit)
B.pack()
    

container.pack()
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

root.mainloop()
