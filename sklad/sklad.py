class Sklad:
    def __init__(self):
        self.podatki = []

    def vstavi(self, x):
        self.podatki.append(x)

    def prazen(self):
        return len(self.podatki) == 0

    def odstrani(self):
        if self.prazen(): raise ValueError('ODSTRANI: Sklad je prazen.')
        self.podatki.pop()

    def vrh(self):
        if self.prazen(): raise ValueError('VRH: Sklad je prazen.')
        return self.podatki[-1]

    def poberi(self):
        rez = self.vrh()
        self.odstrani()
        return rez

    def __str__(self):
        izp = 'DNO'
        for elt in self.podatki: izp += ' : ' + str(elt)
        return izp + ' : VRH'