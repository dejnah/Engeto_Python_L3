sluzby = ("dostupné filmy", "detaily filmu", "seznam režisérů")
oddelovac = "=" * 62

film_1 = {
    "jmeno": "Shawshank Redemption",
    "rating": "93/100",
    "rok": 1994,
    "reziser": "Frank Darabont",
    "stopaz": 144
}

film_2 = {
    "jmeno": "The Godfather",
    "rating": "92/100",
    "rok": 1972,
    "reziser": "Francis Ford Coppola",
    "stopaz": 175
}

film_3 = {
    "jmeno": "The Dark Knight",
    "rating": "90/100",
    "rok": 2008,
    "reziser": "Christopher Nolan",
    "stopaz": 152
}

# sjednoť předchozí 3 slovníky do jednoho slovníku 'filmy'
# .. klíčem bude jméno filmu a samotný slovník následuje
# .. jako hodnota.

#výpis pro uživatele viz zadání:
#zobraz mi dostupné filmy dle zadání:
#zobraz detaily o filmu dle zadání:
#zobraz seznam režisérů:


filmy = dict()

#jednotlivé slovníky sjednotím do slovníku filmy, klíčem budou jména filmů
filmy = {
    film_1["jmeno"]: film_1,
    film_2["jmeno"]: film_2,
    film_3["jmeno"]: film_3
}

from pprint import pprint
pprint(filmy)
print()
print()


#1 VÍTEJTE...
#vypíšu pozdrav, změním na velká písmena a vycentruji
pozdrav = ("Vítej v našem filmovém slovníku!".upper().center(62))
#vypíšu výstup - nabídku - dle grafického zadání, použiji oddělovač ze zadání
print(pozdrav)
print(oddelovac)
print((sluzby[0] + " | " + sluzby[1] + " | doporuč film").center(62))
print()
print()

#2 DOSTUPNÉ FILMY...
#vypíšu výstup - dostupné filmy - dle grafického zadání

print((sluzby[0].capitalize() + ":").center(62))
print(oddelovac)
print(*filmy.keys(), sep = ", ")          # * tzv rozbalí klíče do jednotlivých argumentů
print(oddelovac)

print()
print()

#3 ZOBRAZ DETAILY O FILMU...
# vyber z dostupné služby v nabídce a zobraz jména filmů
print(str(sluzby[1].capitalize() + ":"))
print(oddelovac)
print(filmy['The Dark Knight'])
print(oddelovac)
print()


#4 ZOBRAZ SEZNAM REŽISÉRU...
print("Všichni režiséři:")
print(oddelovac)
reziseri = set()
reziseri.add(film_1["reziser"])
reziseri.add(film_2["reziser"])
reziseri.add(film_3["reziser"])

print(reziseri)
print(oddelovac)
print()

#reziseri2 = set()
#for nazev_filmu in filmy.keys():
#    reziseri2.add(filmy[nazev_filmu]["reziser"])
#print(reziseri2)
#print()
