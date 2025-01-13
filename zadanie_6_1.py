def licz_sortowane(plik_we, plik_wynik): 
    with open(plik_we, "r") as f, open(plik_wynik, "w") as out: 
        licznik = 0 
        for linia in f: 
            liczby = list(map(int, linia.split())) 
            if liczby == sorted(liczby): 
                licznik += 1 
        out.write(f'{licznik}\n') 
 

licz_sortowane('pliki/anomalie_przyklad.txt', 'wynik6_1.txt')