import random

class Vozel:
    '''
    Razred, ki predstavlja posamezen vozel s podatkom v verižnem seznamu.
    '''
    def __init__(self, podatek, naslednji=None):
        self._podatek = podatek
        self._naslednji = naslednji

    def get_podatek(self):
        '''referenca na podatek'''
        return self._podatek

    def get_naslednji(self):
        '''referenca na naslednji podatek'''
        return self._naslednji

    def set_naslednji(self, val):
        self._naslednji = val

    def izpisi(self, zamik=" "):
        zamik += str((str(self._podatek) + " -> "))
        if self._naslednji != None:
            self._naslednji.izpisi(zamik)
        else:
            print(zamik[:-4])

class VerizniSeznam:
    def __init__(self, podatek, naslednji=None):
        self._podatek = podatek
        self._naslednji = naslednji
        self._zacetek = None

    def get_podatek(self):
        '''referenca na podatek'''
        return self._podatek

    def get_naslednji(self):
        '''referenca na naslednji podatek'''
        return self._naslednji

    def set_naslednji(self, val):
        self._naslednji = val

    def izpisi(self, zamik=" "):
        zamik += str((str(self._podatek) + " -> "))
        if self._naslednji != None:
            self._naslednji.izpisi(zamik)
        else:
            print(zamik[:-4])

################################################################################

def uredi(clenVerige):
    '''uredi verigo po velikosti'''

    zacetekNic = Vozel(40)  # prva nula v novi verigi
    zacetekEna= Vozel(41)  # prva enka v novi verigi
    zacetekDva = Vozel(42)  # prva dvojka v novi verigi
    konecNic = zacetekNic
    konecEna = zacetekEna
    konecDva = zacetekDva

    while True:  # ko gre zanka v neskončnost

        #kje_smo = clenVerige.get_podatek()  #prvi clen verige

        naslednji = clenVerige.get_naslednji() #zapisemo naslednji clen.
        if clenVerige.get_podatek() == 0:  # če je člen verige enak 0, ga dodamo v nule

            #ce je konec nicel enak None, potem na njega prevezemo clen verige
            if konecNic:
                konecNic.set_naslednji(clenVerige)  #koncu nicel dodamo prvi vozel in konec popravimo nanj
                konecNic = clenVerige
                konecNic.set_naslednji(None) #zadnja nicla ima tako referenco na None
            else:
                konecNic = clenVerige
                zacetekNic = clenVerige
        elif clenVerige.get_podatek() == 1:  # če je člen verige enak 1, ga dodamo v enke
            if konecEna:
                konecEna.set_naslednji(clenVerige)  # objektu enke dodamo prvi element in referenco popravimo nanj
                konecEna = clenVerige
                konecEna.set_naslednji(None) #zadnja enka ima tako referenco na None
            else:
                konecEna = clenVerige
                zacetekEna = clenVerige
        elif clenVerige.get_podatek() == 2:  # če je člen verige enak 2, ga dodamo v dvojke
            if konecDva:
                konecDva.set_naslednji(clenVerige)  # objektu dvojke dodamo prvi element in referenco popravimo nANJ
                konecDva = clenVerige
                konecDva.set_naslednji(None) #zadnja dvojka ima sedaj referenco n None
            else:
                konecDva = clenVerige
                zacetekDva = clenVerige
        else:
            print("Slaba veriga")

        clenVerige = naslednji
        if not naslednji:  # če ni naslednjega elementa prekinemo zanko
            break

    #vsi konci imajo sedaj referenco na None
    konecNic.set_naslednji(None)
    konecEna.set_naslednji(None)
    konecDva.set_naslednji(None)

    #dolocimo kazalca na objekta na začetku in koncu seznama
    zacetek = None
    konec = None

    #ce imamo prvo niclo, potem je to nas zacetek, konec pa je nastavljen na konecNic
    if zacetekNic != None:
        zacetek = zacetekNic
        konec = konecNic

    if zacetekEna != None:
        if zacetek == None:  # če nismo imeli prej nicel
            zacetek = zacetekEna
            konec = konecEna

        # ce smo imeli prej ze nicle, nam kazalec konec kaze na zadnjo niclo, kateri dodamo enko
        else:
            konec.set_naslednji(zacetekEna._naslednji)  # kazalec konec kaže na zadnji objekt z ničlo
            konec = konecEna

    if zacetekDva != None:
        if zacetek == None:  # če nismo imeli ničel al enk
            zacetek = zacetekDva
            konec = konecDva
        # ce smo imeli prej ze nicle in/ali enke, nam kazalec konec kaze na zadnjo niclo ali enko, kateri dodamo dvojko
        else:
            konec.set_naslednji(zacetekDva._naslednji)  # kazalec konec kaže na zadnji objekt z ničlo ali enico
            konec = konecDva


    konec.set_naslednji(None)  # zadnji dvojki sledi None
    konecNic.naslednji = zacetekEna._naslednji
    konecEna.naslednji = zacetekDva._naslednji
    return zacetek._naslednji

def veriga():
    a = VerizniSeznam(0)  # prvi člen
    '''b = VerizniSeznam(0, a)
    a.set_naslednji(b)
    c = VerizniSeznam(2, b)
    b.set_naslednji(c)
    '''
    clen = a
    for i in range(9):
        b = VerizniSeznam(random.randint(0,2))
        clen.set_naslednji(b)
        clen = b
    clen.set_naslednji(None)
    a.izpisi()
    # print("se nazaj")
    # clen.izpisi_nazaj()
    print("urejamo in izpišemo normalno!")
    prvi = uredi(a)
    prvi.izpisi()
    # print("se urejeni nazaj")
    # zadnji.izpisi_nazaj()


veriga()



