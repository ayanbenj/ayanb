'''
Ayanna Benjamin
Personal Project
Cold or Hot Food Widget
Completed
'''
from tkinter import *

class CHFApp:
    def __init__(self):
        window = Tk()

        Label(window, text="Temperature of Food: ").pack()

        self.inputTemperatureofFood = DoubleVar()
        Entry(window,
              textvariable=self.inputTemperatureofFood).pack()

        Label(window, text="Reduction Temperature").pack()
        self.reductionLabel = Label(window, text="(None)")
        self.reductionLabel.pack()

        Button(window,
               text="Do It!",
               command=self.convertButtonClicked).pack()

        ################ EXTRA WIDGETS #####################

        Label(window,
              text="Poultry: ").pack()

        # 1 = Chicken, 2 = Beef, 3 = Pork
        self.foodType = IntVar()
        self.foodType.set(1)
        Radiobutton(window,
                    text="Chicken",
                    variable=self.foodType,
                    value=1).pack()
        Radiobutton(window,
                    text="Beef",
                    variable=self.foodType,
                    value=2).pack()
        Radiobutton(window,
                    text="Pork",
                    variable=self.foodType,
                    value=3).pack()

        Button(window,
               text="Show Ideal Temperature",
               command=self.showTempButtonClicked).pack()

        window.mainloop()

    def convertButtonClicked(self):
        f = self.inputTemperatureofFood.get()
        m = self.reduc(f)

        self.reductionLabel["text"] = str(m)

        print("The temperature of the meat is", f)
        print("Please reduce the room to this temperature", m)

    def showTempButtonClicked(self):
        option = self.foodType.get()
        if option == 1:
            self.inputTemperatureofFood.set(40)
        elif option == 2:
            self.inputTemperatureofFood.set(40)
        elif option == 3:
            self.inputTemperatureofFood.set(40)


    def reduc(self, f):
        if f <= 40:
            print("The Food is cold enough!")
            return f
        else:
            return (f - 40)


CHFApp()


