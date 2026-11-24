def ocena(slowo_docelowe , sprawdzane):
    dlugosc = len(sprawdzane)
    wyniki = [0,0,0,0,0]
    for i in range(dlugosc):
        if slowo_docelowe[i] == sprawdzane[i]:
            wyniki[i] = 0
        elif sprawdzane[i] in slowo_docelowe:
            wynik[i] = 1
        else:
            wynik[i] = 2)
    for i in range(dlugosc):
        print(sprawdzane[i] , end=" ")
    for j in range(dlugosc):
        print(wyniki[j])
