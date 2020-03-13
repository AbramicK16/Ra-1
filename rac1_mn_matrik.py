#### 2. SKLOP - MNOŽENJE MATRIK ####

#-------------------------------- 1. NALOGA: MNOŽENJE MATRIK

# Denimo, da moramo za izračun fizikalne simulacije velikokrat zmnožiti med
# seboj 6 matrik fiksne velikosti. V kakšnem vrstnem redu naj jih množimo,
# da bomo porabili kar čimmanj operacij, če so matrike velikosti
# 3x4, 4x5, 5x5, 5x2, 2x2 ter 2x3? Koliko operacij pri tem porabimo?
# Če je možnih načinov množenja z minimalnim številom operacij več, napiši vse!

# FUNNKCIJE

def st_mnozenj(dim):
    ''' Vrnemo trojico: shemo, st mnozenj in slovar 'trojke' '''

    p = [dim[0][0]]
    for el in dim:
        p.append(el[1])


    m = [[0 for x in range(len(p))] for x in range(len(p))] 
    n = len(p)
    trojke_vse = dict() # beležimo naš k, oz kje 'razdelimo'
    trojke = dict()
    # m[i,j] = minimalno št operacij
    # za izračun A[i]A[i+1]...A[j] = A[i..j] 
  
    # če množimo eno matriko je cena 0
    for i in range(1, n): 
        m[i][i] = 0
  
    for L in range(2, n): 
        for i in range(1, n-L+1): 
            j = i+L-1
            m[i][j] = float('inf')
            for k in range(i, j): 
  
                # q = cena / skalarna množenja
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if q == m[i][j]:
                    prej = trojke[i,j]
                    if isinstance(prej, list):
                        z = prej.append(k)
                        trojke_vse[i,j]= z
                    else:
                        trojke_vse[i,j]= [k,prej]
                if q < m[i][j]: 
                    m[i][j] = q
                    trojke_vse[i,j]= k
                    trojke[i,j]= k
    return m[1][n-1],trojke,trojke_vse
                
    
    
def pomoc(P, i, j, dim):
    izraz = ''
   
    if i==j:
        izraz+='A'+str(i)
    else:
        izraz+= '('
        izraz+=pomoc(P, i, P[i,j],dim)
        izraz+=pomoc(P, P[i,j] + 1, j,dim)
        izraz+= ')'
    return izraz

def vrstni_red(dim):
    s = st_mnozenj(dim)[2]
    
    return pomoc(st_mnozenj(dim)[1],1, len(dim),dim)


# REŠITEV ZA DOLOČEN PRIMER


print('Število operacij: ' + str(st_mnozenj([(3,4),(4,5),(5,5),(5,2),(2,2),(2,3)])[0]))
trojke1 = st_mnozenj([(3,4),(4,5),(5,5),(5,2),(2,2),(2,3)])[1]
trojke2 = st_mnozenj([(3,4),(4,5),(5,5),(5,2),(2,2),(2,3)])[1]
trojke2[3, 5] = 4
trojke2[1, 6] = 5
print('Mozni nacini mnozenja:' + str(pomoc(trojke1, 1, len([(3,4),(4,5),(5,5),(5,2),(2,2),(2,3)]),[(3,4),(4,5),(5,5),(5,2),(2,2),(2,3)]))
      +', '+ str(pomoc(trojke2, 1, len([(3,4),(4,5),(5,5),(5,2),(2,2),(2,3)]),[(3,4),(4,5),(5,5),(5,2),(2,2),(2,3)])))
      


