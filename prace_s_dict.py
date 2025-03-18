#1. Vytvoř slovník `student = {"jméno": "Jan", "příjmení": "Novák", "věk": 20}`,
#2. přidej do slovníku klíč `obor` s hodnotou `"Informatika"`,
#3. přidej do slovníku klíč `"kontakt"` s hodnotami: `{"email": "jan.novak@gmail.com", "mobil": "+420777666555"}`,
#4. získej ze slovníku `student` klíč `pohlavi`, pokud je součástí slovníku, jinak nesmí skončít výjimkou,
#5. získej ze slovníku `kontakt` klíč `mobil`, pokud je součástí slovníku, jinak nesmí skončít výjimkou,
#6. vypiš všechny klíče ze slovníku `student`,
#7. zjisti, kolik klíčů a hodnot má slovník `student`.

#1
student = {"jméno": "Jan", "příjmení": "Novák", "věk": 20}

#2
student["obor"] = "Informatika"
print(student)

#3
student["kontakt"] = {"email": "jan.novak@gmail.com", "mobil": "+420777666555"}
print(student)

#4
print(student.get("pohlavi", "Tento klíč neexistuje!"))

#5
print(student.get("kontakt").get("mobil", "Tento klíč neexistuje!"))

#6
print(student.keys())

#7
print(len(student))


from pprint import pprint
pprint(student)
