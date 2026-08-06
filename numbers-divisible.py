starting_number = int(input())
ending_number = int(input())

count = 0

while starting_number <= ending_number:
    if starting_number % 3 == 0:
        count += 1
    starting_number += 1

print(f"Divisible by 3: {count}")