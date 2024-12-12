#tipovačka pevnýho čísla

#kod donekonečna vyzývá k zadání čísla.
#po zadání čísla, bude sděleno, sdali je tipnuté číslo větší nebo menší než výherní číslo
#jakmile bude výherní číslo tipnuto, bude vypsáno "Výhra!!!!!"
import random

# Vygenerování náhodného výherního čísla
vyherni_cislo = random.randint(1, 100)  # Náhodné číslo mezi 1 a 100

print("Vítejte ve hře! Zadejte číslo od 1 do 100 a zkuste uhodnout výherní číslo.")

# Začátek hry
tip = ""

while tip != vyherni_cislo:  # Smyčka běží, dokud tip není rovný výhernímu číslu

        tip = int(input("Zadejte své číslo: "))

        # Kontrola tipu
        if tip < vyherni_cislo:
            print("Vaše číslo je menší než výherní číslo.")
        elif tip > vyherni_cislo:
            print("Vaše číslo je větší než výherní číslo.")
        else:
            print("Výhra!!!!!")

print("Konec hry")
