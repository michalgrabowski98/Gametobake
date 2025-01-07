from tkinter import Tk, Button

root = Tk()
root.geometry("900x300")
root.title("TEST")

buttonexit = Button(root, text = "Exit", command = root.destroy) 


buttonexit.pack()
root.mainloop()