#import
from idlelib.configdialog import help_pages

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
Wall1 = '#a9a9a9'
Wall2 = '#4D7C8A'
Button = '#7F9C96'
Button2 = '#8FAD88'
SearchBar = '#CBDF90'

def destroy_button():
    for widget in buttonFrame.winfo_children(): # this destroys the buttons
        widget.destroy()

def search_call(): #search
    query = searchBar.get().strip().lower()
    filteredData = fileread[fileread["Name"].str.lower().str.contains(query)]
    destroy_button()
    for index,row in filteredData.iterrows():
        name = row["Name"]
        type1 = row["Type 1"]
        type2 = row.get("Type 2", None)
        hp = row["HP"]
        atk = row["Attack"]
        defense = row["Defense"]
        spAtk = row["Sp. Atk"]
        spDef = row["Sp. Def"]
        spd = row["Speed"]
        gen = row["Generation"]
        leg = row["Legendary"]

        pSearchName = filteredData["Name"].iloc[0]  # Get the 'Name' of the first entry for that count
        pSearchButton = ctk.CTkButton(buttonFrame, text=name, fg_color=Button2,
                                      command=lambda
                                          name = name,
                                          type1 = type1,
                                          type2 = type2,
                                          hp = hp,
                                          atk = atk,
                                          defense =defense,
                                          spAtk = spAtk,
                                          spDef = spDef,
                                          spd = spd,
                                          gen = gen,
                                          leg = leg:
                                          poke_button_press(name, type1, type2, hp, atk, defense, spAtk, spDef, spd, gen, leg))



                                    #tempName=name: poke_button_press(tempName))
        pSearchButton.pack(pady=5, fill="both", expand=True)


def poke_button_press(name, type1, type2, hp, atk, defense, spAtk, spDef, spd, gen, leg):
    dataFrame.delete("1.0", "end") #clears the frame so new stuff can appear

#this is text for the buttons for the pokemon so the pokemon work 
    dataFrame.insert("1.0",
                    f"name: {name}"
                     f"\nType 1: {type1}"
                     f"\nType 2: {type2}"
                     f"\nHP: {hp}"
                     f"\nAttack: {atk}"
                     f"\nDefense: {defense}"
                     f"\nSp. Atk: {spAtk}"
                     f"\nSp. Def: {spDef}"
                     f"\nSpeed: {spd}"
                     f"\nGeneration: {gen}"
                     f"\nLegendary: {leg}")



app = ctk.CTk(fg_color=Wall1)
app.geometry("500x900")
app.title("Pokedex with added storm flute")
app.resizable(width = False, height = False)

dataFrame = ctk.CTkTextbox(app)
pokestats = dataFrame.insert(0.0,"Pokemon Stats Go Here!")
dataFrame.pack(side = "right", fill="y")

searchFrame = ctk.CTkFrame(app, fg_color= Wall1)
searchFrame.pack(fill= "x")

buttonFrame = ctk.CTkScrollableFrame(app, fg_color= Wall2)
buttonFrame.pack(fill= "both", expand= True)

searchBar = ctk.CTkEntry(searchFrame,width= 300, fg_color= SearchBar)
searchBar.pack(side= "left", padx= 10)

searchEntry = ctk.CTkButton(searchFrame, fg_color= Button, text= "Search", command=search_call())
searchEntry.pack(side= "right", padx= 10)



search_call()

app.mainloop()

