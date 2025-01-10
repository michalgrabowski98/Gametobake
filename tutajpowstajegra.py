from tkinter import *


#wprowadzanie imiona
def nameofplayer():
    global name
    name = txt.get()
    #if sprawdza czy coś zostało wprowadzone
    if name:
        lbl.configure (text = f"Hello {name}, you wanna play same game (yes/no)")
        #guzik przenosi do kolejnych opcji
        btn.configure (text = "Next", command = answer1)
    
    #delete czyści pole tekstowe txt od 0 - początek do END - koniec
    txt.delete(0, END)
    return name
    
 
#otwarcie gry, def2
def answer1():
    answer = txt.get().lower().strip()


    if answer == "yes":
        lbl.configure (text=("You have reached doors to big crypt. It's kinda strange to see also some ring to it, they have eletricity down there?"))
        btn.configure (text = "Next", command= answer2)
        txt.delete(0, END)  
        #koniec gry
    else:
        btn.configure (text="Exit", command= root.destroy)
        lbl.configure (text="please press exit to close the game")
        txt.delete(0, END)       


def answer2():
    answer = txt.get()

    if answer == "knock":
        lbl.configure (text= ("The old woman, around here 30s," 
                              "opened the door and looks at you with her dark brown eyes -"
                                f"What is your wish to find here {name}?(tea/coffe))")
                        )
        btn.configure (text="Next", command=answer3)
        txt.delete(0, END)


def answer3():
    answer = txt.get().lower().strip()

    if answer == "x":
        lbl.configure(text="test")





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