import random

# Komputer losuje liczbę od 1 do 100
wylosowana_liczba = random.randint(1, 100)

print("🎮 Witaj w grze 'Zgadnij liczbę'! 🎮")
print("Spróbuj odgadnąć liczbę od 1 do 100.")

while True:
    # Pobranie liczby od użytkownika
    proba = int(input("Podaj liczbę: "))

    if proba < wylosowana_liczba:
        print("📉 Za mało! Spróbuj ponownie.")
    elif proba > wylosowana_liczba:
        print("📈 Za dużo! Spróbuj ponownie.")
    else:
        print("🎉 Brawo! Zgadłeś liczbę!")
        break  # Koniec gry
        import random

        # Komputer losuje liczbę od 1 do 100
        wylosowana_liczba = random.randint(1, 100)
        maks_liczba_prob = 7  # Limit prób

        print("🎮 Witaj w grze 'Zgadnij liczbę'! 🎮")
        print(f"Spróbuj odgadnąć liczbę od 1 do 100. Masz {maks_liczba_prob} prób!")

        for proba_nr in range(1, maks_liczba_prob + 1):
            proba = int(input(f"Próba {proba_nr}/{maks_liczba_prob} - Podaj liczbę: "))

            if proba < wylosowana_liczba:
                print("📉 Za mało!")
            elif proba > wylosowana_liczba:
                print("📈 Za dużo!")
            else:
                print(f"🎉 Brawo! Zgadłeś liczbę w {proba_nr} próbie!")
                break  # Koniec gry
        else:
            print(f"❌ Przegrałeś! Wylosowana liczba to {wylosowana_liczba}.")

