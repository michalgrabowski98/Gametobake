from tkinter import *


#wprowadzanie imiona
def nameofplayer():
    name = txt.get()
    #if sprawdza czy coś zostało wprowadzone
    if name:
        lbl.configure (text = f"Hello {name}")
        btn.configure (text = "Next", command= answer)
    #delete czyści pole tekstowe txt od 0 - początek do END - koniec
    txt.delete(0, END)
    return nameofplayer

#tworzenie okna
root= Tk()

#tytuł
root.title("Gra")

#rozmiar okna
root.geometry ('1200x1000')

#pole do wprowadzania odpowiedzi
txt = Entry(root, width=10)
txt.grid(column = 2, row =1)

#label tutaj pojawia się tekst nieinteraktywny
lbl = Label(root, text = "Please, provide us, with name of your character:")
lbl.grid(column=1, row = 1)



#guzior do zatwierdzania
btn = Button(root, text = "Enter", command= nameofplayer)

#pozycja guziora
btn.grid(column=3, row=1)





























root.mainloop()