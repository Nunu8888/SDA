zvirata = ["Kočka", "Pes", "Had"]

#TADY NAPSAT FORCYKLUS KTERÝ POSTUPNĚ VYPÍŠE
#"Kočka běhá"
#"Pes běhá"
#"Had běhá"

for zvire in zvirata:
    print(f"{zvire} běhá")

#Druhá část úkolu
stari = [["Žirafa", 20], ["Slon", 40], ["Dikobraz", 5]]
#NAPSAT FORCYKLUS PŘES stari. Pro každý prvek (list) vypíšete:
#Žirafa má věk 20
#Slon má věk 40
#Dikobraz má věk 5

for info_o_zviteti in stari:
    print(info_o_zviteti)
    print(f"{info_o_zviteti[0]} má věk {info_o_zviteti[1]}")