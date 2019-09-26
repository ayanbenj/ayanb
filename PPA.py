'''
Author: Ayanna Benjamin
Started: 9/25/2019
Personal Project, PPA Pokemon Persoanlity App
Not yet completed
'''
from tkinter import *

class PPApp:
    def __init__(self):
        window = Tk()

        window.title("PPApp")
        #introduction right here
        l1 = Label(window,
      text= "Welcome To the Pokemon Personality App")

        l2 = Label(window,
           text= "What is your greatest personality trait?")
        l3 = Label(window,
           text= "What is your favorite color?")
        l4 = Label(window,
           text= "What is your favorite type in Pokemon?")

        Entry_1 = Entry(window)
        Entry_2 = Entry(window)
        Entry_3 = Entry(window)

        # making the button personalize
        b1 = Button(window,
               text= "PERSONALIZE",
               command = self.personalizePokemon)
        b2 = Button(window,
                    text="CLICK ME!",
                    command=self.getit)
        b3 = Button(window,
                    text="CLICK ME!",
                    command=self.getit2)
        b4 = Button(window,
                    text="CLICK ME!",
                    command=self.getit3)
        #placement of introduction
        l1.grid(row = 0, column = 0)
        l2.grid(row = 1, column = 0)
        l3.grid(row = 2, column = 0)
        l4.grid(row = 3, column = 0)

        #making boxes for the personalities
        Entry_1.grid(row = 1, column = 1)
        Entry_2.grid(row = 2, column = 1)
        Entry_3.grid(row = 3, column = 1)

        #placement of button
        # placement of button
        b1.grid(row=3, column=3)
        b2.grid(row=1, column=2)
        b3.grid(row=2, column=2)
        b4.grid(row=3, column=2)
        window.mainloop()

        ################ EXTRA WIDGETS #####################

    def getit(self):
        personality = self.Entry_1.get()
    def getit2(self):
        color = self.Entry_2.get()
    def getit3(self):
        pktype = self.Entry_3.get()

    def personalizePokemon(self, check1 = getit, check2 = getit2, check3 = getit3 ):
        self.personality = check1
        self.color = check2
        self.pktype = check3
        if check1 and check2 and check3 == words:
            print("Looking good so far")
        else:
            print("Please try a different word")

def words(self):
    check1 = ["happy", "kind", "sweet", "independent", "loyal", "excited","bubbly"\
        ,"aggravating", "annoying", "proud", "cute", "smart", "precious", "adorable"]

    check2 = ["red", "blue", "green", "orange", "yellow", "light green", "indigo", \
                 "purple", "violent", "pink", "black", "white", "gray", "brown"]
    check3 = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting", \
                 "Poison", "Ground", "Psychic", "Flying", "Bug", "Rock", "Ghost", \
                 "Dragon"]

    #def recheck(self):
     #      self.personality = check1
      #     self.color = check2
       #    self.pktype = check3
        #   if self == check1[0] and self.l3 == check2[3] and self.l4 == check3[2]:
         #       picture = ImageTk.PhotoImage(file='Bulbasaur.png')

          #      label1 = Label(image=picture)
           #     label1.image = picture
            #    label1.grid(row=1, column=4, columnspan=2)




PPApp()