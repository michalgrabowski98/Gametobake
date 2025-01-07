#import dla tworzenia okna
import tkinter as tk

window = tk.Tk()   
window.mainloop()

#kod gry

#gracz nadaje imie swojej postaci
def nameofplayer():
    name = input("Please, provide us, with name of your character: ")
    return name

#przechowuje nazwe gracza z def nameofplayer
nameP=nameofplayer()

#gracz daje dwie odpowiedzi
answer = input(f"You wanna play some game {nameP}?(yes/no)")

#gracz dał tak, idziemy dalej z opowieścią
if answer.lower().strip() == "yes":
#jeśli na końcu damy .lower().strip() oszczędzamy sobie czas, lower strip daje nam odp w dowolnym rozmiarze znaków np YES yEs etc.
    answer = input("You have reached doors to big crypt. It's kinda strange to see also some ring to it, they have eletricity down there?").lower().strip()
    #women path
    if answer == "knock":
        answer = input (f"The old woman, around here 30s, opened the door and looks at you with her dark brown eyes - What is your wish to find here {nameP}?(tea/coffe)")

     #coffe   
    if answer == "coffe":
        answer = input (f"{nameP} Oh so you like coffe then, well, quite shame, but, oh well, nevermind")


    #tea
    elif answer == "tea":
        answer = input (f"Oh my, how lovely, please come in!")





#femboy path
    elif answer == "ring":
        print("test")

    else:
        print("Really? Try again")


#gracz dał nie albo coś innego
else:
    print ("That's fine, have a good time doing something else :)")