'''
author =
'''
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
garpike and stingray are also present.'''
         ]
# Program si vyžádá si od uživatele přihlašovací jméno a heslo

reg_uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

username = input("Username: ")
password = input("Password: ")
oddelovac = "-" * (len("Enter a number btw. 1 and 3 to select: ") + 1)
print(oddelovac)

# Program zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů. Pokud je uživatel registrovaný, pozdraví
# jej a umožni mu analyzovat texty. Pokud není, upozorni jej a ukonči program.

if username in reg_uzivatele and reg_uzivatele[username] == password:
    print("Welcome to the app, " + username)
else:
    print("Wrong credentials. Can´t continue.")
    quit()

# Program nechá uživatel vybrat mezi třemi texty, uloženými v proměnné TEXTS.

print("We have 3 texts to be analyzed.")
print(oddelovac)

vstup = input("Enter a number btw. 1 and 3 to select: ")
print(oddelovac)

# Pro vybraný text spočítá následující statistiky.

if vstup.isdigit() and int(vstup) in range(1, 4):
    index = int(vstup) - 1
    slova = TEXTS[index].split()
    pocet_slov = len(slova)

    velka_zac_pismena = 0
    velka_pismena = 0
    mala_pismena = 0
    cisla = 0
    suma = 0

    for slovo in slova:
        if slovo.istitle():
            velka_zac_pismena += 1
        elif slovo.isupper():
            velka_pismena += 1
        elif slovo.islower():
            mala_pismena += 1
        elif slovo.isnumeric():
            cisla += 1
            suma += int(slovo)

    print(
        "There are " + str(pocet_slov) + " words in the selected text.\n"
        "There are " + str(velka_zac_pismena) + " titlecase words.\n"
        "There are " + str(velka_pismena) + " uppercase words.\n"
        "There are " + str(mala_pismena) + " lowercase words.\n"
        "There are " + str(cisla) + " numeric strings.\n"
        "The sum of all the numbers is " + str(suma) +"."
        )
    print(oddelovac)
    print("LEN|" + "OCCURENCES".center(18) + "|NR.")
    print(oddelovac)

# Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu.

    vyskyty = {}

    for slovo in slova:
        delka_slova = len(slovo.strip(".,"))
        if delka_slova in vyskyty:
            vyskyty[delka_slova] += 1
        else:
            vyskyty.setdefault(delka_slova, 1)

    sorted_vyskyty = sorted(vyskyty)

    for vyskyt in sorted_vyskyty:
        print(" " * (2 - len(str(vyskyt))) + str(vyskyt) + "|" + "*" * vyskyty[vyskyt] + (" " * (19-vyskyty[vyskyt])) + "|" + str(vyskyty[vyskyt]))

# Pokud uživatel vybere takové číslo textu,které není v zadání, program jej upozorní a skončí. Pokud uživatel zadá
# jiný vstup než číslo, program jej rovněž upozorní a skončí.

else:
    print("Input is not digit or in range 1-3. Can´t continue.")
    quit()
