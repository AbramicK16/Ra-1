from veriga_vozlov import Vozel, dodaj_na_konec, dodaj_na_zacetek, vrni_seznam, iz_seznama

#Sestavi funkcijo, ki sprejme verigo vozlov in za vsak element verige vrne število njegovih pojavitev v verigi.
def pojavitve(prvi):
    '''za vsak element verige vrne število njegovih pojavitev'''
    slovar = dict()
    while prvi is not None:
        if prvi.podatek not in slovar.keys():
            slovar[prvi.podatek] = 1  # dodamo podatek kot kljuc v slovar
        else:  # ce pa je ta kljuc ze v slovarju, mu povecamo vrednost
            slovar[prvi.podatek] += 1
        prvi = prvi.naslednji
    return slovar



##Testni primeri:

seznam1 = [1, 2, 3, 1]
veriga1 = iz_seznama(seznam1)
#print(veriga1)
#print(pojavitve(veriga1))
#print('resitev')
#print('True')

seznam2 = [1, 2, 2, 3, 1]
veriga2 = iz_seznama(seznam2)
#print(veriga2)
#print(pojavitve(veriga2))

seznam3 = [1, 2, 2,3, 5, 6,  3, 1]
veriga3 = iz_seznama(seznam3)
#print(veriga3)
#print(pojavitve(veriga3))

seznam4 = []
veriga4 = iz_seznama(seznam4)
#print(veriga4)
#print(pojavitve(veriga4))

seznam5 = [1]
veriga5 = iz_seznama(seznam5)
#print(veriga5)
#print(pojavitve(veriga5))

seznam6 = [5,2,7,1,4,1,5,3,7]
veriga6 = iz_seznama(seznam6)

vozli = [veriga1, veriga2, veriga3, veriga4, veriga5, veriga6]
sez = [{1:2, 2:1, 3:1}, {1:2, 2:2, 3:1}, {1:2, 2:2, 3:2, 5:1, 6:1}, {}, {1:1}, {5:2, 2:1, 7:2, 1:2, 4:1,3:1}]

rezultat = True
for el in range(len(sez)):
    if sez[el]!= pojavitve(vozli[el]):
        rezultat = False
        print('False')
if rezultat:
    print('True')

