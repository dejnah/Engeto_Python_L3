#1. Vytvoř nové sety z listů `skupina_1` a `skupina_2`,
#2. zjisti, jestli se někdo z uchazečů nevyskytuje v obou skupinách, pokud ano, vypiš `"máme uchazeče ve dvou skupinách"`,
#3. jinak vypiš oznámení: `"žádný uživatel není v obou skupinách"`,
#4. pokud někdo takový existuje, odstraň jej z jedné ze skupin,
#5. přidej do druhého setu email `"m.holinka@gmail.com"`,
#6. sjednoť oba sety a výsledek ulož jako *frozenset*.

skupina_1 = [
    'h.vybíralová@firma.cz', 'w.štrumlová@firma.cz', 'm.vybíralová@firma.cz',
    's.bechyňka@firma.cz', 'z.urbánková@firma.cz', 'l.riečan@firma.cz',
    'v.koudelová@firma.cz', 'f.vorlová@firma.cz', 'i.seleš@firma.cz'
]

skupina_2 = [
    'j.šmíd@firma.cz', 'j.procházková@firma.cz', 'l.riečan@firma.cz', 'd.hlavatá@firma.cz', 
    'm.železný@firma.cz', 'p.niklesová@firma.cz', 'b.skok@firma.cz',
]


from pprint import pprint


#1
set_1 = set(skupina_1)
set_2 = set(skupina_2)
print(type(set_1))
print(type(set_2))

#2, 3
if set_1.isdisjoint(set_2) == 0:
    print("máme uchazeče ve dvou skupinách")
else: 
    print("žádný uživatel není v obou skupinách")
print()

#4
print(set_1.intersection(set_2))
set_1.remove('l.riečan@firma.cz')
print()
pprint(set_1)
print()

#5
set_2.add("m.holinka@gmail.com")

#6
pprint(set_2)
print()
u_set = frozenset(set_1.union(set_2))
print(type(u_set))
pprint(u_set)
