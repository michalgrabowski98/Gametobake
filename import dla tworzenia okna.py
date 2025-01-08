
#tkinter dla tworzenia okna tekstów i guzików etc.
from tkinter import *

root = Tk()
#rozmiar okna
root.geometry("900x300")

#nazwa okna
root.title("TEST")

#tekst w oknie
text_label = Label(root,
                    
                    answer = input("You have reached doors to big crypt. It's kinda strange to see also some ring to it, they have eletricity down there?").lower().strip()
    #women path
                    if answer == "knock":
                    answer = input (f"The old woman, around here 30s, opened the door and looks at you with her dark brown eyes - What is your wish to find here {nameP}?(tea/coffe)")

)

#guzior zamknięcia
buttonexit = Button(root, text = "Exit", command = root.destroy) 


#żeby się ładowało i działało
text_label.pack()
buttonexit.pack()
root.mainloop()