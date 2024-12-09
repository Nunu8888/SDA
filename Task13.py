text = input("Zadej text: ")

kontrola_male = text.islower()
kontrola_velke = text.isupper()

print(f"Vlozeny text je malymi {kontrola_male}")
print(f"Vlozeny text je velkymi {kontrola_velke}")