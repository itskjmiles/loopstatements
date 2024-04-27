import random

# List of moods
moods = ["Happy", "Sad", "Energetic", "Calm"]

# Days of the week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Loop through each day and select a random mood
for day in days:
    mood = random.choice(moods)
    print(f"On {day}, you were feeling {mood}.")
