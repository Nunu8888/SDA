#v řetězci: "qsxht!trfecdtcbgřáýčerdxdpsěš d21rřcřetčěpe**u?rsS"
#Ignorujte prvních pět znaků
#Otočte řetězec
#Vypište každý čtvrtý znak

text = "qsxht!trfecdtcbgřáýčerdxdpsěš d21rřcřetčěpe**u?rsS"
text_bez_peti= text[5:]
print(f"Řetězec po ignorování prvních pěti znaků: {text_bez_peti}")


otoceny_text = text_bez_peti[::-1]
print(f"Otočený řetězec: {otoceny_text}")


kazdy_ctvrty = otoceny_text[::4]
print(f"Každý čtvrtý znak z otočeného řetězce: {kazdy_ctvrty}")

