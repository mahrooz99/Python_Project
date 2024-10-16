from tkinter import *
import tkinter.font as font
import random
from english_words import get_english_words_set

# Global variables
score = 0
time_limit = 30  # Time limit for the game in seconds
# Using the built-in source from the package
words = list(get_english_words_set(sources=['en']))  # Fetch words from the english_words package

def start_game():
    global score, time_limit
    score = 0
    time_limit = 30  # Reset the timer
    timer_label.config(text=f'Time: {time_limit}s')
    score_label.config(text=f'Score: {score}')
    start_button.config(state=DISABLED)
    user_input.delete(0, END)
    generate_word()

    # Start the countdown timer
    countdown()

def countdown():
    global time_limit
    if time_limit > 0:
        timer_label.config(text=f'Time: {time_limit}s')
        time_limit -= 1
        timer_label.after(1000, countdown)
    else:
        finish_game()

def finish_game():
    result_label.config(text=f'Game Over! Your score is: {score}')
    start_button.config(state=NORMAL)
    user_input.config(state=DISABLED)

def generate_word():
    if time_limit > 0:
        random_word = random.choice(words)
        word_label.config(text=random_word)

def check_input(event):
    global score
    if user_input.get() == word_label['text']:
        score += 1
        score_label.config(text=f'Score: {score}')
        user_input.delete(0, END)
        generate_word()

def create_ui():
    global word_label, score_label, timer_label, user_input, start_button, result_label

    # Main window
    root = Tk()
    root.title("Typing Speed Test")
    root.geometry("600x400")
    root.config(bg="lightblue")

    # Title label
    title_label = Label(root, text="Typing Speed Test", font=('Helvetica', 24, 'bold'), bg='lightblue')
    title_label.pack(pady=10)

    # Word display
    word_label = Label(root, text='', font=('Helvetica', 32), fg='blue', bg='lightblue')
    word_label.pack(pady=20)

    # User input
    user_input = Entry(root, font=('Helvetica', 24), justify='center')
    user_input.pack(pady=20)
    user_input.bind('<Return>', check_input)

    # Score and timer
    score_label = Label(root, text=f'Score: {score}', font=('Helvetica', 18), bg='lightblue')
    score_label.pack(pady=10)

    timer_label = Label(root, text=f'Time: {time_limit}s', font=('Helvetica', 18), bg='lightblue')
    timer_label.pack(pady=10)

    # Start button
    start_button = Button(root, text='Start Game', font=('Helvetica', 18), command=start_game)
    start_button.pack(pady=10)

    # Result label
    result_label = Label(root, text='', font=('Helvetica', 18), bg='lightblue')
    result_label.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_ui()
