import rocket
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
poz=[]
x=50
il=5
ra=[]
for z in range(2*il):
    ra.append((random.uniform(-x,x)))
l=['r1','r2','r3','r4','r5']
for zi in range(il):
    l[zi]=rocket.Rocket(ra[2*zi],ra[2*zi+1])
for kil in range(5):
        poz.append(l[kil].get_position())
        l[kil].londowanie()
        l[kil].move(random.uniform(-5, 5), random.uniform(-5, 5))
        print(l[kil].get_position())
        l[kil].get_distance(l[kil-1],l[kil-2],l[kil-3],l[kil-4])

print(poz)
wyk=50
def update(i):
    '''funkcja rysuje wykres'''
    ax.clear()
    ax.set_facecolor(plt.cm.Blues(.2))

    ax.set_xlim([-wyk, wyk])
    ax.set_ylim([-wyk, wyk])
    ax.scatter(x=0, y=0, s=1000, c='purple', marker='o')
    ax.scatter(x=poz[i][0], y=poz[i][1], s=100, c='red', marker='o')
    ax.scatter(x=poz[i+100][0], y=poz[i+100][1], s=100, c='green', marker='o')
    ax.scatter(x=poz[i+200][0], y=poz[i+200][1], s=100, c='black', marker='o')
    ax.scatter(x=poz[i+300][0], y=poz[i+300][1], s=100, c='orange', marker='o')
    ax.scatter(x=poz[i+400][0], y=poz[i+400][1], s=100, c='yellow', marker='o')
    [spine.set_visible(False) for spine in ax.spines.values()]


fig, ax = plt.subplots(figsize=(6, 6))
anime = FuncAnimation(
    fig=fig,
    func=update,
    frames=int(len(poz)/5),
    interval=50
)

plt.show()
