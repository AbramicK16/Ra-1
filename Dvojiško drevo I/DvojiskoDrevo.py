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
        ''' Metoda vrne desno poddrevo danega dvojiškega drevesa.
            Če je drevo prazno, sproži izjemo. '''
        if(self.prazno()):
            raise Exception("Prazno drevo nima desnega poddrevesa");
        
        return self._desnoPoddrevo
    

    def levoPoddrevo(self):
        '''Metoda vrne levo poddrevo danega dvojiškega drevesa. Če je drevo prazno, sproži izjemo.'''
        if(self.prazno()):
            raise Exception("Prazno drevo nima levega poddrevesa");
        
        return self._levoPoddrevo
    

    def prazno(self):
        ''' Je drevo prazno? '''
        return self._prazno


    def vrniPodatek(self):
        '''Metoda vrne podatek, ki je shranjen v korenu danega dvojiškega drevesa. Če je drevo prazno, sproži izjemo.''' 
        if(self.prazno()):
            raise Exception("Prazno drevo nima podatka")
        
        return self._podatekVKorenu
    
    
    def sestavi(levoDrevo, podatekVKorenu, desnoDrevo):
        '''Metoda sprejme levo drevo, podatek v korenu ter desno drevo. Kot rezultat nam vrne sestavljeno dvojiško drevo.'''
        novoDrevo = DvojiskoDrevo(podatekVKorenu, levoDrevo, desnoDrevo)
        novoDrevo._prazno = False
        return novoDrevo
    

         
    def __str__(self):
        '''Metoda izpiše levi obhod danega dvojiškega drevesa.
           Če pri tem pride do napake, vrne niz 'Interna napaka'.'''
        try:
            izpis = DvojiskoDrevo.obhod(self, "lkd")
            return "[" + izpis[:-1] + "]"
        except Exception: 
            return "Interna napaka"
        
    
    
    
    def obhod(drevo, vzorec):
            
        '''Vrne niz, ki predstavlja dani obhod dvojiškega drevesa.'''
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
    
                
    def sestaviIzTabele(tabela, polozajKorena=1):
        '''Sestavi drevo iz tabelarične predstavitve.
           tabela: tabelarična predstavitev drevesa.
        '''
        if(polozajKorena>=len(tabela) or tabela[polozajKorena] == None):
            return DvojiskoDrevo()
        
        levo = DvojiskoDrevo.sestaviIzTabele(tabela, 2 * polozajKorena)
        desno = DvojiskoDrevo.sestaviIzTabele(tabela, (2 * polozajKorena) + 1)
        return DvojiskoDrevo.sestavi(levo, tabela[polozajKorena], desno)
