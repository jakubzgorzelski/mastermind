def ocena(slowo_docelowe , sprawdzane):
    #2 - jest na miejscu
    #1 - nie na miejscu
    #0 - chuja
    dlugosc = len(slowo_docelowe)
    if len(sprawdzane) != dlugosc:
        print("zla dlugosc wyrazu!!")
        return []
    wyniki = [0] * dlugosc
    pozostale = sprawdzane.copy()
    for i in range(dlugosc):
        if sprawdzane[i] == slowo_docelowe[i]:
            wyniki[i] = 2
            pozostale[i] = None
    for i in range(dlugosc):
        if wyniki[i] == 0 and sprawdzane[i] in slowo_docelowe:
            wyniki[i] = 1
            pozostale[pozostale.index(sprawdzane[i])] = None




    # for i in range(dlugosc): #2 sposob moze kiedys nie dziala 
    #     litera = slowo_docelowe[i]
    #     for j in range(dlugosc):
    #         if sprawdzane[j] == litera:
    #             wyniki[j] = 2
    #         if (litera in sprawdzane) and sprawdzane[j] != slowo_docelowe[j]:
    #             wyniki[j] = 1
    #         if litera not in sprawdzane:
    #             wyniki[j] = 0
            
            
    for i in range(dlugosc):
        print(sprawdzane[i] , end=" ")
    print()
    for j in range(dlugosc):
        print(wyniki[j] , end=" ")
    return wyniki
