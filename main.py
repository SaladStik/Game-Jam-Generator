# main.py
import random
from themes import the_themes as game_themes
from genres import game_genres
import tkinter as tk

def get_random_theme_and_genre():
    theme = random.choice(game_themes)
    genre = random.choice(game_genres)
    return theme, genre

if __name__ == "__main__":
    theme, genre = get_random_theme_and_genre()
    window = tk.Tk()
    window.geometry("720x300")
    greeting = tk.Label(text="Ready To Generate", font=("Arial", 20))
    greeting.pack()
    def update_theme_and_genre():
        theme, genre = get_random_theme_and_genre()
        greeting.config(text=f"Theme: {theme}\n\nGenre: {genre}")
    button = tk.Button(window, text="Generate", command=update_theme_and_genre)
    button.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
    window.mainloop()
    
