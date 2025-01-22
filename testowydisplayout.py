from tkinter import *

#wprowadzanie imiona
def nameofplayer():
    
    global name

    name = txt.get()

    #if sprawdza czy coś zostało wprowadzone
    if name:
        lbl.configure (text = f"Hello {name}. Do you want to play the game? (YES/NO)")
        btn.configure (text = "Next", command=answer1)
        txt.delete(0, END)

        #bez tego elsa mi nie działa xD nie wiem czm. on tu dla picu
    else: 
        lbl.configure (text = "Please press button EXIT to exit")
        btn.configure (text="EXIT", command= root.destroy)
        txt.delete(0, END)
    #delete czyści pole tekstowe txt od 0 - początek do END - koniec
    txt.delete(0, END)

def answer1():

    answer = txt.get().lower().strip()
    if answer == "yes":
        
        lbl.configure(text="You have reached doors to big crypt. It's kinda strange to see also some ring attached to this doors, they have eletricity down there?")
        btn.configure(text="Next", command=answer2)
        txt.delete(0, END)
    
    elif answer == "no": 
        lbl.configure (text = "Please press button EXIT to exit")
        btn.configure (text="EXIT", command= root.destroy)
        txt.delete(0, END)
    else:
        lbl.configure (text = "Please press button EXIT to exit")
        btn.configure (text="EXIT", command= root.destroy)
        txt.delete(0, END)

def answer2():
    answer = txt.get().lower().strip()
    if answer == "knock": 
        
        lbl.configure(text=f"The old woman, around here 30s, opened the door and looks at you with her dark brown eyes - What is your wish to find here {name}?")
        btn.configure(text= "Next", command= asnwer3women )

    elif answer == "ring":

        lbl.configure(text="X")
        btn.configure(text="Next", command=answer3femoby)

#womanpath

#femboypath







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
lbl = Label(root, text = "Please, provide us, with name of your character:", bg="grey",font= "30")
lbl.grid(column=1, row = 1)



#guzior do zatwierdzania
btn = Button(root, text = "Enter", command= nameofplayer)

#pozycja guziora
btn.grid(column=3, row=1)



root.configure(bg="grey")
  
root.mainloop()