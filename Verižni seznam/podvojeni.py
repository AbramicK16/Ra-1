from veriga_vozlov import Vozel, dodaj_na_konec, dodaj_na_zacetek, vrni_seznam, iz_seznama



def podvojeni_el(prvi):
    '''Sestavi funkcijo, ki odstrani podvojene
        elemente v verigi vozlov z enim samim pregledom verige. '''
    mn = set()
    if prvi == None:
        return {}
    while prvi != None:
        if prvi not in mn:
            mn.add(prvi.podatek)
        drugi = prvi
        prvi = drugi.naslednji
        if prvi in mn:
            nov = prvi.naslednji
            drugi.naslednji = nov
            prvi = nov
    return mn


##Testni primeri:

seznam1 = [1, 2, 3, 1, 5, 3, 1]
veriga1 = iz_seznama(seznam1)
#print(veriga)
#print(pojavitve(veriga))
#print('resitev')
#print('True')

seznam2 = [2, 2, 2, 2, 2]
veriga2 = iz_seznama(seznam2)
#print(veriga)
#print(pojavitve(veriga))

seznam3 = [1, 2, 3, 7, 5, 6, 4, 8]
veriga3 = iz_seznama(seznam3)
#print(veriga)
#print(pojavitve(veriga))

seznam4 = []
veriga4 = iz_seznama(seznam4)
#print(veriga)
#print(pojavitve(veriga))

seznam5 = [1]
veriga5 = iz_seznama(seznam5)
#print(veriga)
#print(pojavitve(veriga))

vozli = [veriga1, veriga2, veriga3, veriga4, veriga5]
sez = [{1, 2, 3, 5}, {2}, {1, 2, 3, 7, 5, 6, 4, 8}, {}, {1}]


for el in range(len(sez)):
    if sez[el]!= podvojeni_el(vozli[el]):
        print('False')
    else:
        print('True')
