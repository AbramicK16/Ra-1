from veriga_vozlov import Vozel, dodaj_na_konec, dodaj_na_zacetek, vrni_seznam, iz_seznama
import unittest

def pojavitve(prvi):
    '''za vsak element verige vrne število njegovih pojavitev'''
    slovar = dict()
    while prvi is not None:
        if prvi.podatek not in slovar.keys():
            slovar[prvi.podatek] = 1  # dodamo podatek kot kljuc v slovar
        else:  # ce pa je ta kljuc ze v slovarju, mu povecamo vrednost
            slovar[prvi.podatek] += 1
        prvi = prvi.naslednji
    return slovar


class Test_pojavitve(unittest.TestCase):

    def test_ponovitev(self):
        self.assertEqual(pojavitve(iz_seznama([])), {})
    def test_ponovitev(self):
        self.assertEqual(pojavitve(iz_seznama([1])), {1:1})
    def test_ponovitev(self):
        self.assertEqual(pojavitve(iz_seznama([1, 2, 3, 1])), {1:2, 2:1, 3:1})
    def test_ponovitev(self):
        self.assertEqual(pojavitve(iz_seznama([1, 2, 2, 3, 1])), {1:2, 2:2, 3:1})
    def test_ponovitev(self):
        self.assertEqual(pojavitve(iz_seznama([1, 2, 2,3, 5, 6,  3, 1])), {1:2, 2:2, 3:2, 5:1, 6:1})
    def test_pomovitev(self):
        self.assertEqual(pojavitve(iz_seznama([5,2,7,1,4,1,5,3,7])), {5:2, 2:1, 7:2, 1:2, 4:1,3:1})

if __name__ == '__main__':
    unittest.main()