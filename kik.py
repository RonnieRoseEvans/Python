def wyswietl_plansze(plansza):
    print(f"\n[{plansza[0]}] [{plansza [1]}] [{plansza [2]}]")
    print(f"[{plansza[3]}] [{plansza[4]}] [{plansza[5]}]")
    print(f"[{plansza[6]}] [{plansza[7]}] [{plansza[8]}]")
plansza = ['1', '2' , '3', '4' , '5' , '6', '7', '8', '9']
wyswietl_plansze(plansza)
def wykonaj_ruch(plansza, pozycja, znak):
    if plansza[pozycja - 1] == 'x' or plansza[pozycja - 1] == 'o':
        print("Pole jest juz zajęte")
    else:
        plansza[pozycja - 1] = znak
wykonaj_ruch(plansza, 1, 'x')
wykonaj_ruch(plansza, 5, 'o')
wyswietl_plansze(plansza)