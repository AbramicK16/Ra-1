import random

class Vozel:
    '''
    Razred, ki predstavlja posamezen vozel s podatkom v verižnem seznamu.
    '''
    def __init__(self, podatek, naslednji=None):
        self.podatek = podatek
        self.naslednji = naslednji

    def get_podatek(self):
        '''referenca na podatek'''
        return self._podatek

    def get_naslednji(self):
        '''referenca na naslednji podatek'''
        return self._naslednji

    def set_naslednji(self, val):
        self._naslednji = val

class VerizniSeznam:
    '''
    Razred, ki predstavlja verižni seznam z začetkom in koncem.
    '''
    def __init__(self):
        self._zacetek = None
        self._konec = None

    def __str__(self):
        niz = ''
        vozel = self._zacetek
        while vozel is not None:
            niz += '{} -> '.format(repr(vozel.podatek))
            vozel = vozel.naslednji
        return niz + '•'

    def vstavi_na_zacetek(self, podatek):
        '''podatek vstavi na zacetek seznama'''
        vozel = Vozel(podatek)
        if self._zacetek is None:
            self._zacetek = vozel
        else:
            prvi = self._zacetek
            self._zacetek = vozel
            vozel.naslednji = prvi
        return self._zacetek

    #klele morva tole funkcijo za izpis popravt oziroma sm ti jo, da dela sepravi pr teb je bla koda taka:
    # def izpisi(self):
    #     print(str(self._podatek))
    #     if self._naslednji:
    #         self._naslednji.izpisi()

    def izpisi(self):
        """Funckija izpise celotno verigo po vrsti"""
        kje_smo = self._zacetek
        sez_podatkov = list()
        while kje_smo is not None:
            sez_podatkov.append(str(kje_smo.podatek))
            kje_smo = kje_smo.naslednji
        print(' -> '.join(sez_podatkov))


def uredi(verizni_seznam):
    #spremenljivko vozel ti bom spremenu v verizni seznam ker drgac se bos motila z poimenovanjem
    #prou tko pa nerabs 6 zacetnih vozlov ampak samo tri
    #na zacetku bosta dve spremenljivki kazale na isti vozel ampak na koncu bo ena vedno kazala na zacetk vozla druga pa se bo premikala s tem k bomo dodajal vozle
    #prav tako sm ti preimenoval novVozel*** v zacetek***
    zacetekEna = Vozel(41)
    konecEna = zacetekEna
    zacetekNic = Vozel(40)
    konecNic = zacetekNic
    zacetekDva = Vozel(42)
    konecDva = zacetekDva
    #tuki tvoja vozel.podatek ne more delta zaradi tega ker imas kot vozel parameter podan verizni seznam in ne vozel
    #tako da mors spremenit takole
    #kje_smo = vozel.podatek  #referenca na prvi vozel to je tvoja
    kje_smo = verizni_seznam._zacetek
    #zdj mava v spremenljivki kje smo prvi vozel v tistmu veriznemu seznamu
    while kje_smo is not None:
        # v tej zanki morš se zjd premikat po veriznem seznamu in umes podatke vstavljat v ostale tri verige vozlov
        # to bova nrdila tko da na zacetku si podatek zapomne in potem z ifi pregleda kera stevilka je

        #verizni_seznam.podatek = kje_smo.podatek tega dela ubistvu ne potrebuješ oziroma nima smisla ker ti hocs spremenit podatek v osnovnem veriznem seznamu
        #tuki napiseva samo neko spremenljivko, ki bo prestavljala podatek tistga vozla na katerem smo trenutno (kje_smo)
        trenutni_podatek = kje_smo.podatek

        if trenutni_podatek == 0:
            #tuki morva v verigo vozlov z niclami vstavit en vozel z vrednostjo nic
            #potem morva samo se spremnit parameter konecNic da bo kazal na zadnji vozel v verigi
            #novVozelNic = Vozel(trenutni_podatek)
            konecNic.naslednji = Vozel(trenutni_podatek)
            konecNic = konecNic.naslednji

        elif trenutni_podatek == 1:
            #enako kot za zgorn if
            #novVozelEna = Vozel(trenutni_podatek)
            konecEna.naslednji = Vozel(trenutni_podatek)
            konecEna = konecEna.naslednji

        elif trenutni_podatek == 2:
            #enako kot za zgorn if
            #novVozelDva = Vozel(trenutni_podatek)
            konecDva.naslednji = Vozel(trenutni_podatek)
            konecDva = konecDva.naslednji

        else:
            print('slaba veriga')

        kje_smo = kje_smo.naslednji

    #tuki morva še povezat vse verige skupi
    #sepravi najprej na zadnji vozel nicel dodamo prvi vozel ena, .naslednji je zato, da spustimo vozel ki si ga na zacetku skreirala kot pomoznega
    konecNic.naslednji = zacetekEna.naslednji
    #tuki pa dodamo na koncnji vozel enk dodamo prvi vozel dva
    konecEna.naslednji = zacetekDva.naslednji

    #tukej ti zdj vrne vn verigo vozlov
    return zacetekNic.naslednji


#tole bo testni primer k bo zgenerirou en vezirni seznam z 10 elementi k bojo mel med 0 in 2 vrednosti
testni_seznam = VerizniSeznam()
for i in range(10):
    testni_seznam.vstavi_na_zacetek(random.randint(0, 2))
testni_seznam.izpisi()

resitev = uredi(testni_seznam)
#tukej samo sprinta verigo vozlev, zato da vidimo ce deluje pravilno
while resitev is not None:
    print(resitev.podatek)
    resitev = resitev.naslednji











