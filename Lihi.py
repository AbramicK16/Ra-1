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

def izpisi_liha(vozel):
    '''vrne novo verigo v kateri so sami lihi podatki'''
    novVozel = Vozel(42)
    konec = Vozel(42)
    kje_smo = vozel
    while kje_smo is not None:
        vozel.podatek = kje_smo.podatek
        if vozel.podatek % 2 == 1:
            novVozel = Vozel(vozel.podatek)
            konec.naslednji = novVozel
            konec = konec.naslednji
        kje_smo = kje_smo.naslednji
    return novVozel


    zacetekEna = Vozel(41)
    konecEna = zacetekEna
    zacetekNic = Vozel(40)
    konecNic = zacetekNic
    zacetekDva = Vozel(42)
    konecDva = zacetekDva

    kje_smo = verizni_seznam._zacetek #prvi vozel v veriznem seznamu
    while kje_smo is not None:
        trenutni_podatek = kje_smo.podatek #podatek tistega vozla, na katerem smo trenutno (kje_smo)

        if trenutni_podatek == 0:
            konecNic.naslednji = Vozel(trenutni_podatek) #v verigo vozlov z niclami vstavimo en vozel z vrednostjo nic
            konecNic = konecNic.naslednji #parameter konecNic spremenimo, da bo kazal na zadnji vozel v verigi

        elif trenutni_podatek == 1:
            konecEna.naslednji = Vozel(trenutni_podatek)
            konecEna = konecEna.naslednji

        elif trenutni_podatek == 2:
            konecDva.naslednji = Vozel(trenutni_podatek)
            konecDva = konecDva.naslednji

        else:
            print('slaba veriga')

        kje_smo = kje_smo.naslednji
    #sedaj je treba povezat vse verige skupaj
    #najprej na zadnji vozel nicel dodamo prvi vozel ena, .naslednji je zato, da izpustimo pomozni vozel
    konecNic.naslednji = zacetekEna.naslednji
    #dodamo na koncni vozel enk prvi vozel dvojk, kjer ravno tako vzamemo .naslednji vozel, da izpustimp prvega
    konecEna.naslednji = zacetekDva.naslednji