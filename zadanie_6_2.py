def srednia_i_anomalie(plik_we, plik_wynik): 
    with open(plik_we, "r") as f, open(plik_wynik, "w") as out: 
        roznice = [] 
        wiersze = [] 
        for linia in f: 
            liczby = list(map(int, linia.split())) 
            diff = [abs(liczby[i] - liczby[i+1]) for i in range(len(liczby)-1)]
            roznice.extend(diff) 
            wiersze.append(diff) 
        srednia = sum(roznice) / len(roznice) 
        anomalie = [1 if all(d > srednia for d in diff) else 0 for diff in wiersze] 
        out.write(f'{srednia}\n') 
 
srednia_i_anomalie('pliki/anomalie_przyklad.txt', 'wynik6_2.txt')