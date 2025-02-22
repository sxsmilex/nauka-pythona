# Program sprawdzający, czy liczba jest dodatnia, ujemna, czy zerem

# Pobranie liczby od użytkownika
liczba = float(input("Podaj liczbę: "))

# Sprawdzenie, czy liczba jest dodatnia, ujemna, czy zerem
if liczba > 0:
    print("Liczba jest dodatnia.")
elif liczba < 0:
    print("Liczba jest ujemna.")
else:
    print("Liczba jest zerem.")
