import random

items = ["apple", "banana", "cherry", "orange", "pear"]

selected_item = random.choice(items)

guess = input("Guess which item was selected: ")

if guess.lower() == selected_item:
    print("Congratulations! You guessed correctly.")
else:
    print(f"Sorry, the selected item was {selected_item}. Better luck next time!")
