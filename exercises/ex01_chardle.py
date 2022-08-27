"""Small step to wordle- EX01."""

__author__ = "730523557"

word_choice: str = input("Enter a 5-character word: ")
if len(word_choice) != 5:
    print("Error: Word must contain 5 characters.")
    exit()

character_choice: str = input("Enter a single character: ")
if len(character_choice) != 1:
    print("Error: Character must be a single character.")
    exit()

instances_of_character: int = 0 
print("Searching for " + character_choice + " in " + word_choice) 
if character_choice == word_choice[0]:
    print(character_choice + " found in index 0.")
    instances_of_character = instances_of_character + 1
if character_choice == word_choice[1]:
    print(character_choice + " found in index 1.")
    instances_of_character = instances_of_character + 1
if character_choice == word_choice[2]:
    print(character_choice + " found in index 2.")
    instances_of_character = instances_of_character + 1
if character_choice == word_choice[3]:
    print(character_choice + " found in index 3.")
    instances_of_character = instances_of_character + 1
if character_choice == word_choice[4]:
    print(character_choice + " found in index 4.")
    instances_of_character = instances_of_character + 1
if instances_of_character == 1:
    print(str(instances_of_character) + " instance of " + character_choice + " found in " + word_choice)
if instances_of_character > 1:
    print(str(instances_of_character) + " instances of " + character_choice + " found in " + word_choice )
if instances_of_character == 0:
    print("No instances of " + character_choice + " found in " + word_choice)
