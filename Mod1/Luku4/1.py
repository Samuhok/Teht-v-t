pituus = float(input("Anna kuhan pituus senttimetreinä: "))

if pituus < 37:
    puuttuu = 37 - pituus
    print("Laske kuha takaisin järveen.")
    print(f"Alimmasta sallitusta pyyntimitasta puuttuu {puuttuu} cm.")
else:
    print("Kuha on tarpeeksi pitkä.")