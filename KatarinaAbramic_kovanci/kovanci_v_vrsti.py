#Funkcija, ki vrne optimalno vsoto kovancev v vrsti
def naj_vsota1(K, i = None):
    '''optimalna vsota za prvih i kovancev, pri cemer ne smemo vzeti sosednjih dveh kovancev'''
    if i is None:
        i = len(K)
    if i == 0:
        return 0
    if i == 1:
        return K[0]
    if i == 2:
        return max(K[0], K[1])
    vzamemo = K[i-1] + naj_vsota1(K, i-2)
    nevzamemo = naj_vsota1(K, i-1)
    return max(vzamemo, nevzamemo)


#Funkcija, ki vrne vrednosti kovancev, pri katerih je dosezena optimalna vrednost
def vrednosti_opt_vsota(tab):
    '''vrne vrednosti kovancev, pri katerih je dosezena optimalna vsota.
    Pri tem ne smemo vzeti sosednjih dveh kovancev'''
    opt_vsota = 0
    for i in range(2**(len(tab))):
        niz = bin(i)[2:] #stevilo spremenimo v binarno in odrežemo '0b'
        if '11' not in niz: #preverimo da ne vzamemo dveh zaporednih stevil
            if len(niz) < len(tab): #nizu moramo na zacetek dodati ustrezno st. nicel
                niz = (len(tab)-len(niz))*'0' + niz
            tab_nizov = list(niz)
        nova_vsota = 0
        for i, el in enumerate(tab_nizov):
            if el == '1': #pristejemo element, ker je pri vsoti izbran
                nova_vsota += tab[i]
        if nova_vsota > opt_vsota: #ce smo nasli boljso vsoto, obstojeco najboljšo zamenjamo
            opt_vsota = nova_vsota
            max_niz = niz #zapomnimo si indekse izbranih kovancev
    vrednosti_izbranih_kovancev = []
    for i, el in enumerate(max_niz):
        if el == '1': #ce je kovanec v resitvi si zapomnimo njegovo vrednost
            vrednosti_izbranih_kovancev += [tab[i]]
    return vrednosti_izbranih_kovancev

##############################################################

#testi
tab1 = [13, 11, 6, 4, 4, 17, 5, 4, 15, 7, 17, 11, 13, 15, 14]
tab2 = [2, 6, 12, 7, 23, 13, 24, 77, 1]
tab3 = [1, 0, 1, 0, -1, 0, 1, -1]
tab4 = [-5, 1, 6, -15, 15, 50, 10, 1, 40]

print(naj_vsota1(tab1))
print(naj_vsota1(tab2))
print(naj_vsota1(tab3))
print(naj_vsota1(tab4))

print(vrednosti_opt_vsota(tab1))
print(vrednosti_opt_vsota(tab2))
print(vrednosti_opt_vsota(tab3))
print(vrednosti_opt_vsota(tab4))
