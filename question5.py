# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

# Task 1
print("Task 1:")
for index, genre in enumerate(genres, start=1):
    print(f"Track {index}: Now playing {genre}")

# Task 2
print("\nTask 2:")
index = 1
while index <= len(genres):
    genre = genres[index - 1]
    print(f"Track {index}: Now playing {genre}")
    if genre == 'Hip-hop':
        break
    index += 1

# Task 3
print("\nTask 3:")
for index in range(len(genres)):
    genre = genres[index]
    if genre == 'Classical':
        continue
    print(f"Track {index + 1}: Light show ready for {genre}")
