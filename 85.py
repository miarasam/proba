import random
import kolmod
import dyskmod
import wektmod
import matplotlib.pyplot as plt
list=[]
a=[]
b=[]
r=[0.5] #promien
for x in range(100):
    c = random.uniform(-15+r[0], 15-r[0])  #tworzenie losowych srodkow dyskow
    c1= random.uniform(-15+r[0], 15-r[0])
    d=[c,c1,r[0]]
    if dyskmod.pro(d)==False:
        raise ValueError('bład')
    a.append(d[0])
    b.append(d[1])
    list.append(d)     #lista z wszytkimi danymi dysku i wszystkich dysków
print(list)
for zx in range(0,99):
    for z in range(zx+1,100):
        kolmod.kolizja(list[zx],list[z])    #sprawdzenie czy wystepuje kolizja
        for p12 in range(z):
            while kolmod.kolizja(list[p12], list[z]) == True:       #jesli wystepuje przesuniecie dysku
                if list[z][0]<=15-3*r[0]:
                    wektmod.wek(2*r[0],0,list[z])
                else:
                    if list[z][1]<15-3*r[0]:
                        wektmod.wek(-30+4*r[0], 2*r[0], list[z])
                    else:
                        wektmod.wek(-30+4*r[0],-30+4*r[0],list[z])
                p12=0
print(list)
a1 = []
b1 = []
for x in range(100):                    #lista po przesunieciu wszystkich dyskow
    a1.append(list[x][0])
    b1.append(list[x][1])

radius = r[0]
for i in range(len(a)):
    circle = plt.Circle((a[i], b[i]),
                        r[0], alpha=0.5)
    plt.gca().add_patch(circle)
plt.xlim(-15, 15)
plt.ylim(-15, 15)
plt.show()
for i in range(len(a1)):
    circle1 = plt.Circle((a1[i], b1[i]),
                        r[0], alpha=0.5)
    plt.gca().add_patch(circle1)
plt.xlim(-15, 15)
plt.ylim(-15, 15)
plt.show()