from tkinter import *
import random
root=Tk()
root.title("Colour Gen")
root.geometry("600x400")

dictionary = {'Colour': ["maroon","lawn","cyan","cyan4","red"]}

def bg_change():
    random_number = random.randint(0,4)
    print(dictionary["colour"][random_number])
    root.configure(background = dictionary["colour"][random_number])
    