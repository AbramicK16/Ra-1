from veriga_vozlov import Vozel, dodaj_na_konec, dodaj_na_zacetek, vrni_seznam, iz_seznama

def kolikokrat_se_pojavi(v):
    '''sprejme verigo vozlov in za vsak element verige vrne število njegovih pojavitev v verigi.'''

    elementi={ }
    kjesmo=v
    if kjesmo==None:
        return elementi
    while kjesmo != None:
        if kjesmo.podatek in elementi:
            elementi[kjesmo.podatek] += 1
        else:
            elementi[kjesmo.podatek] = 1
        kjesmo=kjesmo.naslednji
        
    return elementi
    

#Testi:
veriga0 = iz_seznama([1,2,3,4,5,6,7,8,9,10,22])
veriga1 = iz_seznama([1,2,3,2,5,6,7,2,9,10,22])
veriga2 = iz_seznama([1,2,33,4,5,33,-20,0,0])
veriga3 = iz_seznama([])
veriga4 = iz_seznama(['asd',-10, 0, None, None, True, False, False, 'asd', '123', 123]) #dogovor, 0 in False štejemo skupaj
veriga5 = None


vozli = [veriga0, veriga1, veriga2, veriga3, veriga4, veriga5]
seznam = [ {1:1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1, 8:1, 9:1, 10:1, 22:1},
           {1:1, 2:3, 3:1, 5:1, 6:1, 7:1, 9:1, 10:1, 22:1},
           {1:1, 2:1, 33:2, 4:1, 5:1, -20:1, 0:2},
           {},
           {'asd':2,-10:1, 0:3, None:2, True:1, '123':1, 123:1},
           {} ]

pravilno = True
for i in range(len(seznam)):
    if seznam[i]!= kolikokrat_se_pojavi(vozli[i]):
        pravilno = False
        print('Primer ' + str(i+1) + ': vrnilo je: ' + str(kolikokrat_se_pojavi(vozli[i]))+ '\n       moralo pa bi: ' + str(seznam[i]))
if pravilno:
    print('Ocena RAČ1: 10!')