from tkinter import *
import json
#_______________________-creates drop down of saved sites______________________

websites_saved = []
with open("pwdata.json", mode="r") as data_file:
    data = json.load(data_file)
    for key, value in data.items():
        websites_saved.append(key)
master = Tk()
variable = StringVar(master)
variable.set(websites_saved[0])  # default value
w = OptionMenu(master, variable, *websites_saved)
w.pack()


def ok():
    print("value is:" + variable.get())


button = Button(master, text="OK", command=ok, width=16, font=("Aerial", 9, "bold"))
button.pack()

mainloop()
