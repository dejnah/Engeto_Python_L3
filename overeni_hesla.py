# vytvoř program, který se pokusí ověřit, jestli heslo vložené uživatelem patří k jeho účtu.
# Zapiš všechny proměnné výše
# zapiš podmínku, která zkontroluje, jestli se hodnoty v proměnných jmeno a heslo shodují s klíčem a hodnotou ve slovníku uzivatel
# pokud se shodují, vypiš oznámení: Ahoj Marek vítej v aplikaci! Pokračuj...
# pokud se neshodují, opět vypiš oznámení: Uživatelské jméno nebo heslo nejsou v pořádku!

jmeno = 'Marek'
heslo = '1234'
uzivatel = {'Marek': '1234'}

if uzivatel.get(jmeno) == heslo:
  print("Ahoj", jmeno, "vítej v aplikaci! Pokračuj...")
# print(f"Ahoj {jmeno} vítej v aplikaci! Pokračuj...")
else:
  print("Uživatelské jméno nebo heslo nejsou v pořádku!")
