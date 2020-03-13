from veriga_vozlov import Vozel, dodaj_na_konec, dodaj_na_zacetek, vrni_seznam, iz_seznama


def podvojeni_el(prvi):
    '''Sestavi funkcijo, ki odstrani podvojene
        elemente v verigi vozlov z enim samim pregledom verige.
        Fukcija vrne množico števil končnega verižnega seznama.'''
    mn = set()
    if prvi == None:
        return {}             #Če je veriga prazna vrnemo prazno množico
    while prvi != None:
        if prvi not in mn:         #Če podatek še ni v množici ga tja shranimo
            mn.add(prvi.podatek)        
        drugi = prvi                 #Zapomniti si moramo en podatek za nazaj
        prvi = drugi.naslednji       #Pregledamo naslednji element
        if prvi in mn:                     #Če se element že nahaja v množici
            nov = prvi.naslednji           #poiščemo njegovega naslednika
            drugi.naslednji = nov          #in njegovega predhodnika nastavimo tako, da sedaj kaže na njegovega naslednjika
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


rezultat = True
for el in range(len(sez)):
    if sez[el]!= podvojeni_el(vozli[el]):
        rezultat = False
        print('False')
if rezultat:
    print('Bravo!')
