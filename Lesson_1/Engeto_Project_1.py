TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.''']

print("Projekt_1.py:\nPrvní projekt do Engeto Online Python Akademie")  # Hlavička projektu
print("Autor: Kateina Kvapilova")
print("e-mail: kvapilova.katerina@gmail.com")
print("-" * 40)
print("$ Python Project1.py")


users = {                                             # Slovník uživatelů
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

jmeno = input("Enter your login username: ").lower()  # Zadání uživatelského jména, ošetřeno proti velkým písmenům

if jmeno not in users:                                # Kontrola, zda je uživatelské jméno platné
    print("Unknown login name. The game's over!")
    print("-" * 40)
    sys.exit()

heslo = input("Enter your login password: ")          # Zadání hesla

import sys
if jmeno in users:
    if users[jmeno] == heslo:                         # Správně zadané jméno a heslo otevře aplikaci
        print("-" * 40)
        print(f"Welcome to the app, {jmeno.capitalize()}!")
        print("We have 3 texts for you to be analyzed.")
        print("-" * 40)
    else:                                             # Špatně zadané jméno nebo heslo, ukončení aplikace
        print("Close, but no cigar! The game's over!")
        print("-" * 40)
        sys.exit()

user_input = input(f"Write the text number between 1 and {len(TEXTS)}: ")

if user_input.isdigit():                              # Kontrola, zda je vstup číslo a zda spadá do rozsahu dostupných textů
    user_input = int(user_input)
    if 1 <= user_input <= len(TEXTS):
        selected_text = TEXTS[user_input - 1]         # Správný výběr textu na základě vstupu uživatele
        print("-" * 40)
        print(f"You have chosen Text {user_input}:{selected_text}")
        print("-" * 40)
    else:
        print("Sorry, we don't have text with this number. The game's over!")          # Zadání čísla mimo rozsah
        print("-" * 40)
        sys.exit()
else:
    print("Incorrect input. The game's over.")                                         # Zadání nečísla
    print("-" * 40)
    sys.exit()

# Odstranit přebytečné mezery a text rozdělit do slov
words = selected_text.split()

# Počítání parametrů
word_count = len(words)                                                              # Celkový počet slov
title_case_count = sum(1 for word in words if word.istitle())                        # Slova začínající velkým písmenem
upper_case_count = sum(1 for word in words if word.isupper() and word.isalpha())     # Slova psaná velkými písmeny
lower_case_count = sum(1 for word in words if word.islower())                        # Slova psaná malými písmeny
numeric_count = sum(1 for word in words if word.isdigit())                           # Počet čísel
numeric_sum = sum(int(word) for word in words if word.isdigit())                     # Součet všech čísel
                
print(f"There are {word_count} words in the selected text.")                         # Výpis výsledků
print(f"There are {title_case_count} in titlecase.")
print(f"There are {upper_case_count} in uppercase.")
print(f"There are {lower_case_count} in lowercase.") 
print(f"There are {numeric_count} numeric strings.") 
print(f"The sum of all numbers {numeric_sum}.")

# Analýza četnosti délek slov
# Odstranit interpunkci a spočítat délky slov
length_counts = {}

for word in words:
    word_length = len(word.strip(",.!?"))
    if word_length in length_counts:
        length_counts[word_length] += 1
    else:
        length_counts[word_length] = 1

# Výpis sloupcového grafu pro délky slov
print("-" * 40)
print("LEN | OCCURENCES           | NR.")
print("-" * 40)

for length in sorted(length_counts):
    count = length_counts[length]
    print(f"{str(length).rjust(3)} | {'*' * count:<20} | {count}")

print("-" * 40)