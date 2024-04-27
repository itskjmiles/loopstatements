# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

# Task 1: Loop through a slice of the genres list and print out the genres
print("Task 1:")
for genre in genres[1:4]:
    print(genre)

# Task 2: Use list comprehension to create a new list with "Music" appended to each genre
print("\nTask 2:")
genre_music = [genre + " Music" for genre in genres]
print(genre_music)

# Task 3: Write a loop using range() to print out a countdown from 10 to 1
print("\nTask 3:")
for num in range(10, 0, -1):
    print(num)
print("The beat drops now!")
