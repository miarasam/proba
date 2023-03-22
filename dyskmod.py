macierz=[[5,2,3,4],[3,25,3,4],[3,5,2,6],[2,3,-5,3]]
kol=len(macierz)
rzad=len(macierz[0])
if macierz[0][0]!=1 and macierz[0][0]!=0:
    macierz[0][0] = 1
    for x in range(rzad):
        macierz[0][rzad]=macierz[0][rzad]/macierz[0][0]
print(macierz)
