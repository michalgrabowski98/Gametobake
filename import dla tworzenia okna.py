
#tkinter dla tworzenia okna tekstów i guzików etc.
from tkinter import *

root = Tk()
#rozmiar okna
root.geometry("900x300")

#nazwa okna
root.title("TEST")

#tekst w oknie
text_label = Label(root, bg="red", text= "piwooooooo, kocham piwoooooooooo")

#guzior zamknięcia
buttonexit = Button(root, text = "Exit", command = root.destroy) 


#żeby się ładowało i działało
text_label.pack()
buttonexit.pack()
root.mainloop()