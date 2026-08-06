text = input()

vowel_count = 0

for ch in text:
    if ch in "aeiou":
        vowel_count += 1

print(f"Vowel Count: {vowel_count}")