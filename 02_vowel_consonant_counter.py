# Program: Count vowels, consonants and spaces

sentence = input("Enter a sentence: ")

vowel_count = 0
consonant_count = 0
space_count = 0

for ch in sentence:
    if ch == " ":
        space_count += 1
    elif ch.lower() in "aeiou":
        vowel_count += 1
    elif ch.isalpha():
        consonant_count += 1

print("\nResults:")
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
print("Spaces:", space_count)
