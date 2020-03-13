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

    def izpisi(self):
        print(str(self._podatek))
        if self._naslednji:
            self._naslednji.izpisi()


def uredi(vozel):
    novVozelEna = Vozel(41)
    konecEna = Vozel(41)
    novVozelNic = Vozel(40)
    konecNic = Vozel(40)
    novVozelDva = Vozel(42)
    konecDva = Vozel(42)
    kje_smo = vozel.podatek #referenca na prvi vozel
    while kje_smo is not None:
        vozel.podatek = kje_smo.podatek
        if vozel.podatek == 0:
            novVozelNic = Vozel(vozel.podatek)
            konecNic.naslednji = novVozelNic
            konecNic = konecNic.naslednji

        #kje_smo = kje_smo.naslednji
        elif vozel.podatek == 1:
            novVozelEna = Vozel(vozel.podatek)
            konecEna.naslednji = novVozelEna
            konecEna = konecEna.naslednji
        #kje_smo = kje.naslednji
        elif vozel.podatek == 2:
            novVozelDva = Vozel(vozel.podatek)
            konecDva.naslednji = novVozelDva
            konecDva = konecDva.naslednji

        else:
            print('slaba veriga')
        kje_smo = kje_smo.naslednji
    return novVozelNic.naslednji














