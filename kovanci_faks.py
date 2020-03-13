def naj_vsota(K, i = None):
    '''optimalna vsota za prvih i kovancev'''
    if i is None:
        i = len(K)
    if i == 0:
        return 0
    if i == 1:
        return K[0]
    if i == 2:
        return max(K[0], K[1])
    vzamemo = K[i-1] + naj_vsota(K, i-2)
    nevzamemo = naj_vsota(K, i-1)
    return max(vzamemo, nevzamemo)


tab = [13, 11, 6, 4, 4, 17, 5, 4, 15, 7, 17, 11, 13, 15, 14]
print(naj_vsota(tab))

##################################################
pomni = dict()
def naj_vsota(K, i = None):
    '''optimalna vsota za prvih i kovancev'''
    if i is None:
        i = len(K)
        if i in pomni:
            return pomni[i]
    if i == 0:
        return 0
    if i == 1:
        return K[0]
    if i == 2:
        return max(K[0], K[1])
    vzamemo = naj_vsota(K, i-2)
    nevzamemo = naj_vsota(K, i-1)
    rezultat =  max(K[i-1] + vzamemo, nevzamemo)
    pomni[i] = rezultat
    return rezultat

tab = [13, 11, 6, 4, 4, 17, 5, 4, 15, 7, 17, 11, 13, 15, 14]
print(naj_vsota(tab))

###################################################

def naj_vsota(K, i = None):
    '''optimalna vsota za prvih i kovancev'''
    if i is None:
        i = len(K)
    if i == 0:
        return 0
    if i == 1:
        return K[0]
    if i == 2:
        return max(K[0], K[1])
    vzamemo = K[i-1,-1] + naj_vsota(K, i-2)
    nevzamemo = naj_vsota(K, i-1)
    return max(vzamemo, nevzamemo)

def koliko(K, i = None):
    ''''''
    if i is None:
        i = len(K)
    if i == 0:
        return 0
    if i == 1:
        return K[0]
    if i == 2:
        return max(K[0], K[1])
    tabela = list()
    vzamemo = K[i-1,-1] + naj_vsota(K, i-2)
    nevzamemo = naj_vsota(K, i-1)
    return max(vzamemo, nevzamemo)
