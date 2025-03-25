from tkinter import *

#wprowadzanie imiona początek gry
def nameofplayer():
    
    global name
    name = txt.get()

    #if sprawdza czy coś zostało wprowadzone
    if name:
        lbl.configure (text = f"Hello {name}. Do you want to play the game? (YES/NO)")
        btn.configure (text = "YES", command= lambda: answer1(1))
        btn.place (relx=0.45)
        Lblbox.configure (text= f"Name: {name}\nStage:1")
        
        #miejsce tworzenia guzika nr2
        btn1.configure (text = "NO", command= lambda:[answer1(0)] )
        btn1.place(relx=0.55, rely=0.6, anchor=CENTER)
              
       
        #bez tego elsa mi nie działa xD nie wiem czm. on tu dla picu
    else: 
        lbl.configure (text = "Please press button EXIT to exit")
        btn.configure (text="EXIT", command= root.destroy)
        
    #delete czyści pole tekstowe txt od 0 - początek do END - koniec
    

def answer1(btn_id):

    
    if btn_id == 1:
        
        lbl.configure(text="You have reached doors to big crypt. It's kinda strange to see also some ring attached to this doors, they have eletricity down there?")
        btn.configure(text="Knock", command= lambda:answer2(2))
        Lblbox.configure (text= f"Name: {name}\nStage:2")
        btn1.configure(text="ring",command=lambda:answer2(3))
        
    
    elif btn_id == 0: 
        lbl.configure (text = "Please press button EXIT to exit")
        btn.configure (text="EXIT", command= root.destroy)
        btn.place(relx=0.5, rely=0.6, anchor=CENTER)
        btn1.grid()
        Lblbox.configure (text= f"Name: {name}\nStage:2")
        
        #znikanie guzika
        
    #else:
        #lbl.configure (text = "Please press button EXIT to exit")
        #btn.configure (text="EXIT", command= root.destroy)
        #

def answer2(btn_id):
    if btn_id ==2:
        
        lbl.configure(text=f"The old woman, around here 30s, opened the door and looks at you with her dark brown eyes - What is your wish to find here {name}?")
        Lblbox.configure (text= f"Name: {name}\nStage:3")
        btn.configure(text= "Next", command= answer3women)
        


    elif btn_id == 3:

        lbl.configure(text="X")
        Lblbox.configure (text= f"Name: {name}\nStage:3")
        btn.configure(text="Next", command=answer3femoby)
        

#womanpath
def answer3women():
    answer = txt.get().lower().strip()

#czym jest szczęście
    if answer == "happines":
        lbl.configure(text=f"A rather peculiar and somewhat melancholic request has been received from your esteemed establishment, {name}.\nMight you be so kind as to discuss the matter over a spot of tea and a selection of biscuits?")
        Lblbox.configure (text= f"Name: {name}\nStage:4")
        btn.configure(command= answer4women_happines)
        
#czym jest miłość?
    elif answer == "love":
        lbl.configure (text= f"Love, you say? Oh, my dear {name}, pray tell me you have not resorted to seeking the aid of the dark arts in this matter!")
        Lblbox.configure (text= f"Name: {name}\nStage:4")
        btn.configure(command= answer4women_love)
        
#        
    else:
        lbl.configure (text="I can only answer to you in matters of lovers or your own personal happines.\n I'm so sorry, but you have to leave this place if you don't have any of this matter on your mind")
        btn.configure (text="Happines", command = answer4women_happines)
        btn.place(relx=0.55, rely=0.6)
        button_next_to_btn = Button(root,text="Love",command= answer4women_love)
        button_next_to_btn.place(relx=0.45, rely=0.6, anchor=CENTER)

def answer4women_happines():
    answer = txt.get().lower().strip()
    if answer == "yes":
        lbl.configure(text="X")

def answer4women_love():
    answer = txt.get().lower().strip()
    if answer == "yes":
        lbl.configure (text="X")
#femboypath






#tworzenie okna
root= Tk()

#tytuł
root.title("Gra")

#rozmiar okna
root.geometry ('1200x1000')

#pole do wprowadzania odpowiedzi
txt = Entry(root, width=10)
#txt.grid(column = 2, row =1)
txt.place(relx=0.5, rely=0.55, anchor=CENTER)

#label tutaj pojawia się tekst nieinteraktywny
lbl = Label(root, text = "Please, provide us, with name of your character:", bg="grey",font= "30")
#lbl.grid(column=1, row = 1)
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)


#guzior do zatwierdzania
btn = Button(root, text = "Enter", command= lambda:[nameofplayer(),txt.destroy()])

#pozycja guziora
#btn.grid(column=3, row=1)
btn.place(relx=0.5, rely=0.6, anchor=CENTER)

#textbox w górnej części we ramce
frame = Frame(root)
frame.pack(anchor='ne')

#lblbox tam się staty robią
Lblbox = Label(frame, text= "Great game",font="25")
Lblbox.pack(side ='top')

#button exit, przycisk wyjścia dla gracza 
button_exit = Button(frame, text= "EXIT", command= root.destroy)
button_exit.pack(side = 'top')


#def hide_button(widget):
   # widget.pack()
btn1 = Button(root)
btn1.place()



root.configure(bg="grey")
  
root.mainloop()