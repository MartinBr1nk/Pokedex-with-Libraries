#import
import pandas as pd
import matplotlib as plt
from tkinter import *
from tkinter import ttk
import csv
import numpy as np
import customtkinter as ctk

#making a home page pretty much
currentScene ="Main"
#changing search to Poke-Type
searchyepokemon = "Type"
#making my python read the csv file
fileread = pd.read_csv('pokemon_data.csv')
print(fileread)
#colours for tkinter
Wall1 = '#1B4079'
Wall2 = '#4D7C8A'
Button = '#7F9C96'
Button2 = '#8FAD88'
SearchBar = '#CBDF90'

app = ctk.CTk(fg_color=Wall1)
app.geometry("500x900")
app.title("Pokedex with added storm flute")
app.resizable(width = False, height = False)

button = ctk.CTkButton(app, text="AAAAA")
button.pack()

app.mainloop()

