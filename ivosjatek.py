import random
import time
import os

# Kérdések beolvasása fájlból
def kerdesek_betoltese(fajlnev):
    if not os.path.exists(fajlnev):
        print(f"Hiba: A(z) '{fajlnev}' fájl nem található.")
        return []
    
    with open(fajlnev, encoding="utf-8") as f:
        kerdesek = [sor.strip() for sor in f if sor.strip()]
    return kerdesek

# Főprogram
print("Üdv a Felelsz vagy Iszol játékban!")
jatekosok = input("Add meg a játékosok neveit vesszővel elválasztva: ").split(",")
jatekosok = [nev.strip().capitalize() for nev in jatekosok]

kerdesek = kerdesek_betoltese("kerdes.txt")
if not kerdesek:
    print("Nincsenek betölthető kérdések. Kilépés...")
    exit()

print("\nKezdődik a játék! Nyomj Ctrl+C a kilépéshez.")
print("-" * 40)

try:
    while True:
        for jatekos in jatekosok:
            print(f"\n{jatekos} következik!")
            dontes = input("Felelsz vagy iszol? (F/I): ").strip().upper()
            if dontes == "F":
                kerdes = random.choice(kerdesek)
                print(f"\nA kérdésed: {kerdes}")
            elif dontes == "I":
                print(f"\n{jatekos}, igyál egyet! 🍻")
            else:
                print("Érvénytelen válasz! Automatikus ivás! 😅")
                print(f"{jatekos}, igyál egyet! 🍻")
            time.sleep(1)
except KeyboardInterrupt:
    print("\n\nJáték vége! Köszi, hogy játszottatok! 🎉")
