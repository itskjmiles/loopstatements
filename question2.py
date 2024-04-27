import random

moods = ["Happy", "Sad", "Energetic", "Calm", "Tired"]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

times_of_day = ["morning", "afternoon", "evening"]
for day in days:
    for time in times_of_day:
        mood = random.choice(moods)
        print(f"On {day} {time} you were {mood}.")
