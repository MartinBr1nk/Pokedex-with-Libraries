import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import customtkinter as ctk
from tkinter import StringVar

# Load dataset (Example dataset, should be replaced with actual Pokémon data)
data = {
    "Name": ["Pikachu", "Charmander", "Squirtle", "Bulbasaur"],
    "Type": ["Electric", "Fire", "Water", "Grass"],
    "Generation": [1, 1, 1, 1],
    "Moveset": ["Thunderbolt, Quick Attack", "Flamethrower, Scratch", "Water Gun, Tackle", "Vine Whip, Tackle"]
}
df = pd.DataFrame(data)

# GUI setup
ctk.set_appearance_mode("dark")
root = ctk.CTk()
root.title("Pokedex")
root.geometry("600x400")


# Search functionality
def search_pokemon():
    query = search_var.get().capitalize()
    result = df[df['Type'] == query]

    if not result.empty:
        result_text.set(result.to_string(index=False))
        plot_pokemon_type_distribution()
    else:
        result_text.set("No Pokémon found with that type.")


def plot_pokemon_type_distribution():
    type_counts = df['Type'].value_counts()
    plt.figure(figsize=(5, 3))
    plt.bar(type_counts.index, type_counts.values, color='skyblue')
    plt.xlabel("Type")
    plt.ylabel("Count")
    plt.title("Pokémon Type Distribution")
    plt.xticks(rotation=45)
    plt.show()


# UI Elements
search_var = StringVar()
result_text = StringVar()

search_label = ctk.CTkLabel(root, text="Enter Pokémon Type:")
search_label.pack(pady=5)

search_entry = ctk.CTkEntry(root, textvariable=search_var)
search_entry.pack(pady=5)

search_button = ctk.CTkButton(root, text="Search", command=search_pokemon)
search_button.pack(pady=5)

result_label = ctk.CTkLabel(root, textvariable=result_text)
result_label.pack(pady=10)

# Run app
root.mainloop()
