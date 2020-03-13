from veriga_vozlov import Vozel, dodaj_na_konec, dodaj_na_zacetek, vrni_seznam, iz_seznama
import unittest

###NAVODILO: Sestavi funkcijo, ki sprejme verigo vozlov in za vsak element verige vrne število njegovih pojavitev v verigi.

def st_ponovitev(v):
    '''Funkcija sprejme verigo in vrne slovar, ki pove kolikokrat se pojavi element.'''

    pojavitve = dict()

    if v is None:
        return dict()
    
    elif v.naslednji is None:
        pojavitve[v.podatek] = 1
        
    else:
        while v.naslednji:
            if v.podatek in pojavitve.keys():
                pojavitve[v.podatek] += 1
            else:
                pojavitve[v.podatek] = 1
            v = v.naslednji

        if v.podatek in pojavitve.keys():
            pojavitve[v.podatek] += 1
        else:
            pojavitve[v.podatek] = 1

    return pojavitve



class Test_st_ponovitev(unittest.TestCase):

    def test_ponovitev(self):
        self.assertEqual(st_ponovitev(iz_seznama([])), {})
    def test_ponovitev(self):
        self.assertEqual(st_ponovitev(iz_seznama([5])), {5:1})
    def test_pomovitev(self):
        self.assertEqual(st_ponovitev(iz_seznama([5,5,6,3,9,3,-8,2,5,6,40,7,7,4,2,1])), {5:3, 6:2, 3:2, 9:1, -8:1, 2:2, 40:1, 7:2, 4:1, 1:1})
        
        


if __name__ == '__main__':
    unittest.main()
    




        
