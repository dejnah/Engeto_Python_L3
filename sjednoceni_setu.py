cisla_1 = (1, 1, 2, 3, 4)
cisla_2 = (5, 6, 7, 7, 8)

# Zapiš všechny proměnné výše
# vytvoří ze zadaných proměnných sety,udělá sjednocení hodnot obou nově vzniklých setů a uloží jej do proměnné sjednocene_hodnoty
# vypíše výsledek s ohlášením "Sjednocené hodnoty ze zadání:".

cisla_1 = (1, 1, 2, 3, 4)
cisla_2 = (5, 6, 7, 7, 8)

cisla_3 = set(cisla_1)
cisla_4 = set(cisla_2)

sjednocene_hodnoty = cisla_3.union(cisla_4)
print("Sjednocené hodnoty ze zadání:", sjednocene_hodnoty)

print(type(cisla_1))
print(type(cisla_2))
print(type(cisla_3))
print(type(cisla_4))
print(cisla_3)
print(cisla_4)
