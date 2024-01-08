import csv

def adatok_betoltese(fajlnev):
    adatok = []
    try:
        with open(fajlnev, 'r') as file:
            reader = csv.reader(file)
            for sor in reader:
                adatok.append(sor)
        return adatok
    except FileNotFoundError:
        print("A megadott fájl nem található.")
        return None

def adatok_listazasa(adatok):
    for sor in adatok:
        print(sor)

def adatok_mentese_fajlba(adatok, kimeneti_fajlnev):
    try:
        with open(kimeneti_fajlnev, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(adatok)
        print(f"Az adatok sikeresen mentve a '{kimeneti_fajlnev}' fájlba.")
    except Exception as e:
        print(f"Hiba történt a mentés során: {e}")

def idotartomanyban_listazas(adatok, kezdo_ev, vegso_ev):
    eredmeny = [sor for sor in adatok if kezdo_ev <= int(sor[0]) <= vegso_ev]
    if eredmeny:
        for sor in eredmeny:
            print(sor)
    else:
        print("Nincs találat az adott időtartományban.")

def main():
    fajlnev = input("Kérem, adja meg a fájl nevét: ")
    adatok = adatok_betoltese(fajlnev)

    if adatok:
        while True:
            print("\n1. Minden adat listázása a képernyőre")
            print("2. Minden adat listázása egy fájlba")
            print("3. Adott időtartományban lévő vívmányok listázása")
            print("4. Kilépés")

            valasztas = input("Válasszon egy opciót (1-4): ")

            if valasztas == '1':
                adatok_listazasa(adatok)
            elif valasztas == '2':
                kimeneti_fajlnev = input("Adja meg a kimeneti fájl nevét: ")
                adatok_mentese_fajlba(adatok, kimeneti_fajlnev)
            elif valasztas == '3':
                kezdo_ev = int(input("Adja meg az időtartomány kezdő évét: "))
                vegso_ev = int(input("Adja meg az időtartomány végső évét: "))
                idotartomanyban_listazas(adatok, kezdo_ev, vegso_ev)
            elif valasztas == '4':
                print("Kilépés...")
                break
            else:
                print("Érvénytelen választás. Kérem, válasszon újra.")

if __name__ == "__main__":
    main()
