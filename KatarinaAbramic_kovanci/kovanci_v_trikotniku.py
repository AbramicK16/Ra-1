
#Funkcija za optimalno vsoto kovancev v trikotniku.

def naj_vsota(trikotnik, m, n):
    '''najvecja vsota kovancev v trikotniku'''
    for i in range(m-1, -1, -1): #pogledamo trikotnik od spodaj gor
        for j in range(i + 1):
            #za vsak element pogledamo obe vrednosti in izpisemo maksimum
            if (trikotnik[i + 1][j] > trikotnik[i + 1][j + 1]): #ce je vrednost na levi strani vecja, jo pristejemo vsoti
                trikotnik[i][j] += trikotnik[i + 1][j]
            else:
                trikotnik[i][j] += trikotnik[i+1][j+1]
    return trikotnik[0][0]

##################################################


def vsota(trikotnik):
    '''vrne optimalno pot zapisano v podseznamih'''
    pot = [[' ' for i in range(j+1)] for j in range(len(trikotnik)-1)]
    if not trikotnik:
        return 0
    if len(trikotnik) == 1:
        return trikotnik[0][0]
    for i in range(len(trikotnik)-2,-1,-1):
        for j in range(i+1):
            trikotnik[i][j] = max(trikotnik[i][j]+trikotnik[i+1][j],trikotnik[i][j]+trikotnik[i+1][j+1])
            if trikotnik[i+1][j] > trikotnik[i+1][j+1]:
                pot[i][j] = 'levo'
            else:
                pot[i][j] = 'desno'
    return pot


def optimalna_pot (trikotnik):
    '''vrne opis optimalne poti z nizoma 'levo', 'desno' '''
    pot = vsota(trikotnik)
    tab = list()
    j = 0
    for i in range(len(pot)):
        if pot[i][j] == 'levo': #ce je optimalno vozlišče na levi, gremo na levo
            tab.append('levo')
        if pot[i][j]== 'desno': #ce je optimalno vozlišče na desni, gremo na desno
            j+=1
            tab.append('desno')
    return tab

def kateriKovanci (trikotnik):
    '''vrne vrednost kovancev, pri katerih je dosežena optimalna vsota'''
    cel_trikotnik = [[trikotnik[j][i] for i in range(j+1)] for j in range(len(trikotnik))] #cel trikotnik
    pot = vsota(trikotnik)
    tab = list() #v tabeli bomo shranjevali vrednosti
    j = 0
    tab = [cel_trikotnik[0][0]]
    for i in range(len(pot)):
        if pot[i][j] == 'levo': #ce se optimalen kovanec nahaja levo
            tab.append(cel_trikotnik[i+1][j]) #ga dodamo v tabelo
        if pot[i][j]== 'desno': #ce se optimalen kovanec nahaja desno
            j+=1
            tab.append(cel_trikotnik[i+1][j]) #ga dodamo v tabelo
    return tab

#testi

trikotnik1 =[[6],
            [5,2],
            [2,3,5],
            [8,7,10,3,],
            [1,9,13,4,3]]

trikotnik2 = [[2]]

trikotnik3 = [[1],
       [4, 8],
       [1, 5, 3]]

trikotnik4 = [[1, 0, 0],
       [4, 8, 0],
       [1, 5, 3]]

trikotnik5 =[[3,0,0,0,0],
            [1,4,0,0,0],
            [2,4,6,0,0],
            [8,9,9,3,0],
            [1,18,3,1,3]]

#print (vsota(trikotnik1))
print(optimalna_pot(trikotnik1))
#print(kateriKovanci(trikotnik1))
print(naj_vsota(trikotnik5,4,4))