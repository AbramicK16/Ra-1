from tkinter import*
from math import*
from random import*
from time import*

class DvojiskoDrevo: 
    '''Implementacija razreda DvojiskoDrevo.'''
        
    def __init__(self, podatek = None, levo = None, desno = None):
        ''' Konstruktor. '''
        
        self._levoPoddrevo = levo
        self._desnoPoddrevo = desno
        self._podatekVKorenu = podatek
        if podatek == None and levo == None and desno == None:
            self._prazno = True
        else:
            self._prazno = False
    
    
    def desnoPoddrevo(self):
        ''' Metoda vrne desno poddrevo danega dvojiškega drevesa. Če je drevo prazno, sproži izjemo. '''
        
        if(self.prazno()):
            raise Exception("Prazno drevo nima desnega poddrevesa");
        
        return self._desnoPoddrevo
    

    def levoPoddrevo(self):
        ''' Metoda vrne levo poddrevo danega dvojiškega drevesa. Če je drevo prazno, sproži izjemo. '''
        
        if(self.prazno()):
            raise Exception("Prazno drevo nima levega poddrevesa.");
        
        return self._levoPoddrevo
    

    def prazno(self):
        ''' Je drevo prazno? '''
        
        return self._prazno


    def vrniPodatek(self):
        ''' Metoda vrne podatek, ki je shranjen v korenu danega dvojiškega drevesa. Če je drevo prazno, sproži izjemo. '''
        
        if(self.prazno()):
            raise Exception("Prazno drevo nima podatka")
        
        return self._podatekVKorenu
    
    
    def sestavi(levoDrevo, podatekVKorenu, desnoDrevo):
        ''' Metoda sprejme levo drevo, podatek v korenu ter desno drevo. Kot rezultat nam vrne sestavljeno dvojiško drevo. '''
        
        novoDrevo = DvojiskoDrevo(podatekVKorenu, levoDrevo, desnoDrevo)
        novoDrevo._prazno = False
        return novoDrevo
    
  
    def __str__(self):
        ''' Metoda izpiše levi obhod danega dvojiškega drevesa. Če pri tem pride do napake, vrne niz 'Interna napaka'. '''
        
        try:
            izpis = DvojiskoDrevo.obhod(self, "lkd")
            return "[" + izpis[:-1] + "]"
        except Exception: 
            return "Interna napaka"


    def obhod(drevo, vzorec):
            
        ''' Vrne niz, ki predstavlja dani obhod dvojiškega drevesa. '''
        if(drevo.prazno()):
            return ""
        
        vrni = ""
        for znak in vzorec: 
            if znak == 'l':
                vrni += DvojiskoDrevo.obhod(drevo.levoPoddrevo(), vzorec)
            elif znak == 'd':
                vrni += DvojiskoDrevo.obhod(drevo.desnoPoddrevo(), vzorec)
            elif znak == 'k':
                vrni += str(drevo.vrniPodatek()) + ","
            else:
                raise Exception("Napačen znak v obhodu (" + str(znak) + "). Dovoljeni znaki so 'l', 'd' in 'k'.")

        return vrni
    
                
    def sestaviIzTabele(tabela, polozajKorena = 1):
        '''
        Sestavi drevo iz tabelarične predstavitve.
        tabela: tabelarična predstavitev drevesa.
        '''
        
        if(polozajKorena>=len(tabela) or tabela[polozajKorena] == None):
            return DvojiskoDrevo()
        
        levo = DvojiskoDrevo.sestaviIzTabele(tabela, 2 * polozajKorena)
        desno = DvojiskoDrevo.sestaviIzTabele(tabela, (2 * polozajKorena) + 1)
        return DvojiskoDrevo.sestavi(levo, tabela[polozajKorena], desno)
    

    def sestaviIskalno(tabela, nizko = False):
        '''
        Sestavi naključno iskalno drevo iz tabele. Če je nizko True, sestavi čim nižje dvojiško iskalno drevo.
        '''

        if len(tabela) == 0:
            return DvojiskoDrevo()
        tabela.sort() # najprej uredimo tabelo, če še ni urejena
        if not nizko:
            indeksKorena = randint(0, len(tabela) - 1)
        else:
            indeksKorena = len(tabela) // 2
        koren = tabela[indeksKorena]
        levoDrevo = DvojiskoDrevo.sestaviIskalno(tabela[:indeksKorena], nizko)
        desnoDrevo = DvojiskoDrevo.sestaviIskalno(tabela[(indeksKorena + 1):], nizko)
        return DvojiskoDrevo.sestavi(levoDrevo, koren, desnoDrevo)
    

    def narisi(self, isci = None, sirina = 1400, visina = 820, odVrha = 50, polmer = 15, kot = 5 * pi / 12, d = 330):
        '''
        Konstruktor, ki sprejme drevo, širino in višino platna, kje naj začne risati (od vrha) ter polmer vozlišč.
        Če je spremenljivka oglati nastavljena na False, nariše drevo z metodo narisi, sicer pa z narisi2 (ki je bolj oglato).
        Če želimo, nam metoda demonstrira iskanje elementa isci.
        '''

        okno = Tk()
        okno.title("Dvojiško drevo")
        risalnoPlatno = Canvas(okno, width = sirina, height = visina)
        risalnoPlatno.pack()
        if isci != None:
            DvojiskoDrevo.demonstriraj(self, risalnoPlatno, isci, sirina, visina, odVrha, polmer, kot, d) # kličemo funkcijo, ki demonstrira iskanje elementa
        else:
            DvojiskoDrevo.narisiDrevo(self, risalnoPlatno, sirina / 2, odVrha + polmer, polmer, kot, d) # kličemo funkcijo, ki samo nariše drevo
        okno.mainloop()


    def narisiDrevo(drevo, platno, x, y, r, kot = 5 * pi / 12, d = 330):
        '''
        Pomožna metoda za risanje drevesa. Središče korena je v točki (x, y), začetni kot med posamezno vejo in navpišnico
        je nastavljen na kot = 5 * pi / 12, začetna dolžina veje pa na d = 300. Z vsakim nivojem se kot med vejama in njuna
        dolžina zmanjša za nek količnik. Vozlišča imajo polmer r.
        '''
        
        if not drevo.prazno():
            platno.create_oval(x - r, y + r, x + r, y - r, fill = "white", width = 2)
            platno.create_text(x, y, text = drevo.vrniPodatek(), font = "Verdana 14")
            levo = drevo.levoPoddrevo()
            desno = drevo.desnoPoddrevo()
            if not levo.prazno():
                deltaX = (d + 2 * r) * sin(kot)
                deltaY = (d + 2 * r) * cos(kot)
                platno.create_line(x - r * sin(kot), y + r * cos(kot), x - deltaX + r * sin(kot), y + deltaY - r * cos(kot))
                DvojiskoDrevo.narisiDrevo(levo, platno, x - deltaX, y + deltaY, r, kot / 1.55, d / 1.65)
            if not desno.prazno():
                deltaX = (d + 2 * r) * sin(kot)
                deltaY = (d + 2 * r) * cos(kot)                
                platno.create_line(x + r * sin(kot), y + r * cos(kot), x + deltaX - r * sin(kot), y + deltaY - r * cos(kot))
                DvojiskoDrevo.narisiDrevo(desno, platno, x + deltaX, y + deltaY, r, kot / 1.55, d / 1.65)


    def demonstriraj(drevo, platno, element, sirina, visina, odVrha, polmer, kot, d):
        DvojiskoDrevo.narisiDrevo(drevo, platno, sirina / 2, odVrha + polmer, polmer, kot, d)
        platno.update() # vmes posodobimo platno
        sleep(2)
        DvojiskoDrevo.poisci(drevo, platno, element, sirina / 2, odVrha + polmer, polmer, kot, d) # nato kličemo funkcijo za demonstracijo


    def poisci(drevo, platno, iskalni, x, y, r, kot = 5 * pi / 12, d = 330):
        '''
        Demonstrira iskanje elementa v drevesu.
        '''

        if not drevo.prazno():
            koren = drevo.vrniPodatek()
            if iskalni == koren:
                sleep(1)
                platno.create_oval(x - r, y + r, x + r, y - r, fill = "red", width = 3)
                platno.create_text(x, y, text = koren, font = "Verdana 14")
                platno.update()
            elif iskalni < koren:
                levo = drevo.levoPoddrevo()
                if not levo.prazno():
                    deltaX = (d + 2 * r) * sin(kot)
                    deltaY = (d + 2 * r) * cos(kot)
                    sleep(1)
                    platno.create_line(x - r * sin(kot), y + r * cos(kot), x - deltaX + r * sin(kot), y + deltaY - r * cos(kot), fill = "red", width = 5)
                    platno.update()
                    DvojiskoDrevo.poisci(levo, platno, iskalni, x - deltaX, y + deltaY, r, kot / 1.55, d / 1.65)
                    platno.update()
            else:
                desno = drevo.desnoPoddrevo()
                if not desno.prazno():
                    deltaX = (d + 2 * r) * sin(kot)
                    deltaY = (d + 2 * r) * cos(kot)
                    sleep(1)
                    platno.create_line(x + r * sin(kot), y + r * cos(kot), x + deltaX - r * sin(kot), y + deltaY - r * cos(kot), fill = "red", width = 5)
                    platno.update()
                    DvojiskoDrevo.poisci(desno, platno, iskalni, x + deltaX, y + deltaY, r, kot / 1.55, d / 1.65) # na vsaki 2 sekundi kličemo rekurzivno
                    platno.update()    

      
