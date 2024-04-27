# Task 1
iteration_count = 0
while True:
    print("Inside the loop")
    iteration_count += 1
    if iteration_count >= 5:
        break

# Task 2
iteration_count = 0
condition_met = False
while not condition_met:
    print("Inside the loop")
    iteration_count += 1
    if iteration_count >= 5:
        condition_met = True
