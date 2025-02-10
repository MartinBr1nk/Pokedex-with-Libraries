#import
from idlelib.configdialog import help_pages

import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
import csv
import numpy as np
import customtkinter as ctk

def generate_type_graph():
    type_counts = fileread['Type 1'].value_counts().add(fileread['Type 2'].value_counts(), fill_value=0)
    #fill value means that if anything is empty it sets that value to zero and type_counts counts all the types with both types

    #plotting with  matplotlib
    plt.figure(figsize=(10,6))
    type_counts.sort_values(ascending=False).plot(kind='bar',color = 'blue')
    plt.title('Amount of Pokemon per type')
    plt.xlabel('TYPE')
    plt.ylabel('No. of Pokemon')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

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

def destroy_button(): # this destroys the buttons
    for widget in buttonFrame.winfo_children():
        widget.destroy()

def search_call(): #searches stuff and actually works! searches by type not by name
    query = searchBar.get().strip().lower()
    filteredData = fileread[
        fileread['Type 1'].str.lower().str.contains(query) |
        fileread['Type 2'].str.lower().str.contains(query)
    ]
    destroy_button()
    filteredData = filteredData.drop_duplicates(subset=['Name','Type 1','Type 2'])
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

        ppName = filteredData["Name"].iloc[0]  # Get the 'Name' of the first entry for that count
        ppButton = ctk.CTkButton(buttonFrame, text=name, fg_color=Button2,
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

        ppButton.pack(pady=5, fill="both", expand=True)

                                    #tempName=name: poke_button_press(tempName))



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
app.geometry("900x900")
app.title("Pokedex with added storm flute")
app.resizable(width = False, height = False)

dataFrame = ctk.CTkTextbox(app)
pokestats = dataFrame.insert(0.0,"Pokemon Stats Go Here! \n MAKE SURE TO SEARCH BY \n TYPE NOT BY NAME")
dataFrame.pack(side = "right", fill="y")

searchFrame = ctk.CTkFrame(app, fg_color= Wall1)
searchFrame.pack(fill= "x")

buttonFrame = ctk.CTkScrollableFrame(app, fg_color= Wall2)
buttonFrame.pack(fill= "both", expand= True)

searchBar = ctk.CTkEntry(searchFrame,width= 300, fg_color= SearchBar)
searchBar.pack(side= "left", padx= 10)

searchButton = ctk.CTkButton(searchFrame, fg_color= Button, text= "Search", command=search_call)
searchButton.pack(side= "right", padx= 10)

#Frame for the button
functionFrame = ctk.CTkFrame(searchFrame)
functionFrame.pack(fill="x")

#Graph Button to summon matplotlib
# Create the button
graphButton = ctk.CTkButton(functionFrame,
                            command=generate_type_graph,  # Ensure this function is defined
                            fg_color=Button2,  # Use the color defined above
                            hover_color=Button,  # Use the color defined above
                            text='Graph')  # Corrected the attribute to lowercase 'text'
graphButton.pack(side="left", expand=True, padx=5, pady=5)

search_call()

app.mainloop()

