import tkinter as tk
from PIL import Image, ImageTk
import random

window = tk.Tk()
window.geometry("500x360")
window.title("Dice Roll")
def roll_dice():
    a = random.randint(1,6)
    label = tk.Label(window,text= a).pack()

button = tk.Button(window,text = "click", command=roll_dice)
button.pack()

# dice = ["dice1.png","dice2.png","dice3.png","dice4.png","dice5.png","dice6.png"]
# Image = ImageTk.PhotoImage(Image.open())



window.mainloop()
