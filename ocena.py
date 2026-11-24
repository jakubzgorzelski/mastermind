def ocena(slowo_docelowe , sprawdzane):
    dlugosc = len(slowo_docelowe)
    if len(sprawdzane) != dlugosc
        print("zla dlugosc wyrazu!!")
        return []
    wyniki = [0,0,0,0,0]
    for i in range(dlugosc):
        if sprawdzane[i] in slowo_docelowe:
            for j in range(dlugosc):
                wyniki[i] = sprawdzane[j]
    for i in range(dlugosc):
        if slowo_docelowe[i] == sprawdzane[i]:
            wyniki[i] = 0
        else:
            wynik[i] = 2
    for i in range(dlugosc):
        print(sprawdzane[i] , end=" ")
    for j in range(dlugosc):
        print(wyniki[j])
