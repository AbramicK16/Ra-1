from DvojiskoDrevoRisi import DvojiskoDrevo
#from sklad import Sklad
import unittest


### Vrni višino drevesa.

def visina(dv_drevo):
    '''Vrne višino dv. drevesa.'''

    if dv_drevo.prazno():
        return 0

    return 1 + max(visina(dv_drevo.levoPoddrevo()), visina(dv_drevo.desnoPoddrevo()))


### Vrni število vseh vozlišč.

def st_vozlisc(dv_drevo):
    '''Prešteje koliko je v dv. d. vozlisc.'''

    if dv_drevo.prazno():
        return 0

    return 1 + st_vozlisc(dv_drevo.levoPoddrevo()) + st_vozlisc(dv_drevo.desnoPoddrevo())


### Preveri, ali je dano drevo izrojeno.

def je_izrojeno(dv_drevo):
    '''Preveri ali je dano drevo izrojeno.'''

    if dv_drevo.prazno():
        return True

    elif not dv_drevo.levoPoddrevo().prazno() and not dv_drevo.desnoPoddrevo().prazno(): #če levo ali desno pdddrevo ni prazno
        return False
    else:
        if not dv_drevo.levoPoddrevo().prazno():
            return je_izrojeno(dv_drevo.levoPoddrevo())
        else:
            return je_izrojeno(dv_drevo.desnoPoddrevo())


### Preveri, ali je dano drevo iskalno.

def je_iskalno(dv_drevo, l = DvojiskoDrevo(), d = DvojiskoDrevo()):
    '''Vrne True, če je drevo iskalno in False sicer.'''
    
    if dv_drevo.prazno():
        return True
    if (not l.prazno()) and dv_drevo.vrniPodatek() <= l.vrniPodatek():
        return False
    if (not d.prazno()) and dv_drevo.vrniPodatek() >= d.vrniPodatek():
        return False
    return je_iskalno(dv_drevo.levoPoddrevo(), l, dv_drevo) and je_iskalno(dv_drevo.desnoPoddrevo(), dv_drevo, d) 

            
        
###---------------------------------------TESTI

class Test_vaje(unittest.TestCase):

    #visina
    def test_visina1(self):
        self.assertEqual(visina(DvojiskoDrevo.sestaviIzTabele([], polozajKorena = 1)), 0)
    def test_visina2(self):
        dv = DvojiskoDrevo.sestaviIzTabele([0,1,2,3], polozajKorena = 1)
        self.assertEqual(visina(dv), 2)
    def test_visina3(self):
        dv = DvojiskoDrevo.sestaviIzTabele([0,1,2,3,DvojiskoDrevo(),4,5,DvojiskoDrevo(),DvojiskoDrevo(),DvojiskoDrevo(),6], polozajKorena = 1)
        self.assertEqual(visina(dv), 4)
    def test_visina4(self):
        dv = DvojiskoDrevo.sestaviIzTabele([0,1,2,3,4,5,6,7,8,9,10,11], polozajKorena = 1)
        self.assertEqual(visina(dv), 4)

    #vozlisca
    def test_vozlisca1(self):
        dv = DvojiskoDrevo.sestaviIzTabele([0,1,2,3,4,5,6,7,8,9,10,11], polozajKorena = 1)
        self.assertEqual(st_vozlisc(dv),11)
    def test_vozlisca2(self):
        dv = DvojiskoDrevo.sestaviIzTabele([], polozajKorena = 1)
        self.assertEqual(st_vozlisc(dv),0)
    def test_vozlisca3(self):
        d6 = DvojiskoDrevo.sestavi(DvojiskoDrevo(), 6, DvojiskoDrevo())
        d5 = DvojiskoDrevo.sestavi(d6, 5, DvojiskoDrevo())
        d4 = DvojiskoDrevo.sestavi(DvojiskoDrevo(), 4, DvojiskoDrevo())
        d3 = DvojiskoDrevo.sestavi(d5, 3, DvojiskoDrevo())
        d2 = DvojiskoDrevo.sestavi(DvojiskoDrevo(), 2, d4)
        d1 = DvojiskoDrevo.sestavi(d2, 1, d3)
        self.assertEqual(st_vozlisc(d1),6)

    #izrojeno
    def test_izrojeno1(self):
        dv = DvojiskoDrevo.sestaviIzTabele([], polozajKorena = 1)
        self.assertEqual(je_izrojeno(dv),True)
    def test_izrojeno2(self):
        dv = DvojiskoDrevo.sestaviIzTabele([0,1,2,3,4,5,6,7,8,9,10,11], polozajKorena = 1)
        self.assertEqual(je_izrojeno(dv),False)
    def test_izrojeno3(self):
        dv = DvojiskoDrevo.sestaviIzTabele([0,1,2,3,DvojiskoDrevo(),4,5,DvojiskoDrevo(),DvojiskoDrevo(),DvojiskoDrevo(),6], polozajKorena = 1)
        self.assertEqual(je_izrojeno(dv),False)
    def test_izrojeno4(self):
        d5 = DvojiskoDrevo.sestavi(DvojiskoDrevo(), 5, DvojiskoDrevo())
        d4 = DvojiskoDrevo.sestavi(d5, 4, DvojiskoDrevo())
        d3 = DvojiskoDrevo.sestavi(DvojiskoDrevo(), 3, d4)
        d2 = DvojiskoDrevo.sestavi(DvojiskoDrevo(), 2, d3)
        d1 = DvojiskoDrevo.sestavi(d2, 1, DvojiskoDrevo())
        self.assertEqual(je_izrojeno(d1),True)

    #iskalno
    def test_iskalno1(self):
        dv = DvojiskoDrevo.sestaviIzTabele([], polozajKorena = 1)
        self.assertEqual(je_iskalno(dv),True)
    def test_iskalno2(self):
        dv = DvojiskoDrevo.sestaviIzTabele([0,1,2,3,4,5,6,7,8,9,10,11], polozajKorena = 1)
        self.assertEqual(je_iskalno(dv),False)
    def test_iskalno3(self):
        dv = DvojiskoDrevo.sestaviIzTabele([0,6,2,9,1,3,8,10], polozajKorena = 1)
        self.assertEqual(je_iskalno(dv),True)
    def test_iskalno4(self):
        dv = DvojiskoDrevo.sestaviIzTabele([0,2,1,3], polozajKorena = 1)
        self.assertEqual(je_iskalno(dv),True)
    def test_iskalno5(self):
        dv = DvojiskoDrevo.sestaviIzTabele([0,6,2,9,1,3,8,5], polozajKorena = 1)
        self.assertEqual(je_iskalno(dv),False)
    
        
    
        
if __name__ == '__main__':
    unittest.main()

