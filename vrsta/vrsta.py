class Elt:

    def __init__(self, vsebina, dummy=False):
        self.dummy = dummy
        if not dummy:
            self.vsebina = vsebina


class Vrsta:

    def __init__(self, zacetni_elti=None):
        self.zacetni = Elt(None, dummy=True)
        self.koncni = self.zacetni
        if zacetni_elti:
            for x in zacetni_elti:
                self.vstavi(x)

    def prazna(self):
        return self.zacetni.dummy

    def vstavi(self, vsebina):
        self.koncni.naslednji = Elt(None, dummy=True)
        self.koncni.vsebina = vsebina
        self.koncni.dummy = False
        self.koncni = self.koncni.naslednji

    def zacetek(self):
        if self.prazna():
            raise IndexError('vrsta je prazna')
        return self.zacetni.vsebina

    def odstrani(self):
        if self.prazna():
            raise IndexError('vrsta je prazna')
        self.zacetni = self.zacetni.naslednji

    def __repr__(self):
        seznam = []
        p = self.zacetni
        while not p.dummy:
            seznam.append(repr(p.vsebina))
            p = p.naslednji
        return 'Vrsta([{0}])'.format(', '.join(seznam))

    def __str__(self):
        if self.prazna():
            return 'ZACETEK : KONEC'
        seznam = []
        p = self.zacetni
        while not p.dummy:
            seznam.append(str(p.vsebina))
            p = p.naslednji
        return 'ZACETEK : ' + ' : '.join(seznam) + ' : KONEC'
