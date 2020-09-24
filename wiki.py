import wikipedia
from tkinter import *

__author__ = "Sahal Mulki"

print("Made by " + __author__)


def retrieve_input():
    inputValue=textBox.get("1.0","end-1c")
    summary_wiki = wikipedia.summary(inputValue)

    popup = Tk()
    popup.wm_title("Results:")
    label = Label(popup, text=summary_wiki[0:200] + "....", font=("Helvetica", 10))
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

root = Tk()

textBox = Text(root, height=2, width=10)
textBox.pack()
buttonsearch = Button(root, height=1, width=10, text="Search",
                    command=lambda: retrieve_input())

buttonsearch.pack()

root.mainloop()
