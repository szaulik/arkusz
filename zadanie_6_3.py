def najtansza_droga(tablica):
    n = len(tablica)
    m = len(tablica[0])

    # Tworzymy tablicę kosztów
    koszty = [[0] * m for _ in range(n)]

    # Inicjalizacja kosztu w lewym dolnym rogu
    koszty[-1][0] = tablica[-1][0]

    # Wypełnianie pierwszej kolumny (ruch w górę)
    for i in range(n-2, -1, -1):
        koszty[i][0] = koszty[i+1][0] + tablica[i][0]

    # Wypełnianie pierwszego wiersza (ruch w prawo)
    for j in range(1, m):
        koszty[-1][j] = koszty[-1][j-1] + tablica[-1][j]

    # Wypełnianie reszty tablicy kosztów
    for i in range(n-2, -1, -1):
        for j in range(1, m):
            koszty[i][j] = tablica[i][j] + min(koszty[i+1][j], koszty[i][j-1])

    # Śledzenie ścieżki
    droga = []
    i, j = n - 1, 0  # Startujemy w lewym dolnym rogu
    droga.append((i+1, j+1))  # Dodajemy 1, aby numerować od 1 (i, j zaczynają się od 0)

    while i != 0 or j != m-1:
        if i == 0:  # Jeśli jesteśmy na górze, idziemy w prawo
            j += 1
        elif j == m-1:  # Jeśli jesteśmy na prawej krawędzi, idziemy w górę
            i -= 1
        else:  # Wybieramy mniejszy koszt
            if koszty[i-1][j] < koszty[i][j+1]:
                i -= 1
            else:
                j += 1

        droga.append((i+1, j+1))  # Dodajemy 1, aby numerować od 1

    droga.reverse()  # Odwracamy drogę, żeby była w porządku od początkowego do końcowego punktu
    return droga, koszty[0][-1]


def zapisz_wynik_do_pliku(nazwa_pliku, droga, koszt):
    with open(nazwa_pliku, 'w') as plik:
        # Wypisz współrzędne drogi
        for i, (wiersz, kolumna) in enumerate(droga):
            plik.write(f"{wiersz} {kolumna}\n")
        
        # Uzupełnij do 1004 linii, powtarzając ostatni krok
        for _ in range(1004 - len(droga)):
            plik.write(f"{droga[-1][0]} {droga[-1][1]}\n")
        
        # Na końcu wypisz koszt drogi
        plik.write(f"{koszt}\n")


def wczytaj_dane_z_pliku(nazwa_pliku):
    with open(nazwa_pliku, 'r') as plik:
        # Wczytujemy dane z pliku
        tablica = [list(map(int, linia.split())) for linia in plik]
    return tablica


# Główna funkcja
def main():
    tablica = wczytaj_dane_z_pliku('pliki/anomalie.txt')
    droga, koszt = najtansza_droga(tablica)
    zapisz_wynik_do_pliku('wynik6_3.txt', droga, koszt)


# Uruchomienie
main()
