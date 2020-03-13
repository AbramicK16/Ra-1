def sestaviZ(s, predmet):
    '''Sestavi in vrne množico Z_i.'''
    z = []
    for el in s:
        nov = tuple(sum(i) for i in zip(predmet, el))
        z.append(nov)
    return z

def sestaviS(s, z):
    '''Sestavi množivo S_(i+1). '''
    novas = sorted(s+z, key=lambda x: x[0])
    res = [(0,0)]
    for i in range(len(novas)):
        if novas[i][1]>res[-1][1]:
            res.append(novas[i])
    r = res[::-1]
    s = []
    for i in range(1,len(r)):
        if r[i-1][0] != r[i][0]:
            s.append(r[i])
    if r[0][0] != r[1][0]:
        s.insert(0,r[0])
    return s[::-1]

def mnoziceS(predmeti):
    '''Sprejme tabelo predmetov in vrne seznam vseh množic S.'''
    mn = [[(0,0)]]
    for par in predmeti:
        z = sestaviZ(mn[-1],par)
        mn.append(sestaviS(mn[-1],z))
    return mn

def max_zadovoljstvo(predmeti, velikost):
    '''Vrne nam velikost, ki jo zapolnemo in največjo možno vrednost.'''
    mnozice_s = mnoziceS(predmeti)
    zadnja_s = mnozice_s[-1]
    i = 0
    if zadnja_s[-1][0] < velikost:
        return zadnja_s[-1]
    else:
        while zadnja_s[i][0] < velikost:
            i += 1
        return zadnja_s[i-1]

def resitev01(predmeti, velikost):
    ''' Vrnemo seznam ničl in enk, ki povedo kateri predmet vzamemo in katerega ne.'''
    sez = [0]*len(predmeti)
    opt = max_zadovoljstvo(predmeti, velikost)
    s = mnoziceS(predmeti)
    i = len(sez)-1
    while i>=0:
        if opt in s[i]:
            sez[i] = 0
        else:
            opt = (opt[0]-predmeti[i][0], opt[1]-predmeti[i][1])
            sez[i] = 1
        i -= 1
    return sez

print('Vse množice S: ' + str(mnoziceS([(11,4),(6,8),(9,3),(4,5),(5,6)])))
print('Velikost, ki jo zasedemo in max vrednost: '+str(max_zadovoljstvo([(11,4),(6,8),(9,3),(4,5),(5,6)],25)))

print('Katere predmete vzamemo: ' +str(resitev01([(11,4),(6,8),(9,3),(4,5),(5,6)],25)))
