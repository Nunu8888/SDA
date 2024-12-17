faktury_k_vystaveni = [
    ["Panasonic", 30000, "Martin Novotný"],
    ["Oracle", 22000, "Petr Lukoš"],
    ["Porsche", 32345, "Ivo Gira"],
    ["Siemens", 2000, "Luboš Šejk"],
]
ico_moji_firmy = 3456785
#Vypište
#Faktura ID 0. Vystavuje firma 3456785. Faktura pro Martin Novotný na částku 30000 pro firmu Panasonic

for index, faktura in enumerate(faktury_k_vystaveni):
    print(f"Faktura ID {index}. Vystavuje firma {ico_moji_firmy}. Faktura pro {faktura[2]} na částku {faktura[1]} pro firmu {faktura[0]}")