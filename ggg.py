from matplotlib.animation import FuncAnimation
import rocket
import random
import matplotlib.pyplot as plt
wybor='piec'
x=50
if wybor=='piec':
    r1=rocket.Rocket(random.uniform(-x,x),random.uniform(-x,x))
    r2=rocket.Rocket(random.uniform(-x,x),random.uniform(-x,x))
    r3=rocket.Rocket(random.uniform(-x,x),random.uniform(-x,x))
    r4=rocket.Rocket(random.uniform(-x,x),random.uniform(-x,x))
    r5=rocket.Rocket(random.uniform(-x,x),random.uniform(-x,x))
    print(rocket.get_position(r1))
    print(rocket.get_position(r2))
    print(rocket.get_position(r3))
    print(rocket.get_position(r4))
    print(rocket.get_position(r5))
    l1=[]
    l2=[]
    l3=[]
    l4=[]
    l5=[]
    for x in range(100):
        l1.append(rocket.get_position(r1))
        if rocket.londowanie(r1)==False:
            rocket.move(r1, random.uniform(-1, 1), random.uniform(-1, 1))
            print(rocket.get_position(r1))
            rocket.get_distance(r1,r2,r3,r4,r5)
        else:
            print(rocket.londowanie(r1))
    for x1 in range(100):
        l2.append(rocket.get_position(r2))
        if rocket.londowanie(r2) == False:
            rocket.move(r2,random.uniform(-10,10),random.uniform(-10,10))
            print(rocket.get_position(r2))
            rocket.get_distance(r2,r1,r3,r4,r5)
        else:
            print(rocket.londowanie(r2))
    for x2 in range(100):
        l3.append(rocket.get_position(r3))
        if rocket.londowanie(r3) == False:
            rocket.move(r3,random.uniform(-1,1),random.uniform(-1,1))
            print(rocket.get_position(r3))
            rocket.get_distance(r3,r1,r2,r4,r5)
        else:
            print(rocket.londowanie(r3))
    for x3 in range(100):
        l4.append(rocket.get_position(r4))
        if rocket.londowanie(r4) == False:
            rocket.move(r4,random.uniform(-1,1),random.uniform(-1,1))
            print(rocket.get_position(r4))
            rocket.get_distance(r4,r1,r2,r3,r5)
        else:
            print(rocket.londowanie(r4))
    for x4 in range(100):
        l5.append(rocket.get_position(r5))
        if rocket.londowanie(r5) == False:
            rocket.move(r5,random.uniform(-1,1),random.uniform(-1,1))
            print(rocket.get_position(r5))
            rocket.get_distance(r5,r1,r2,r3,r4)
        else:
            print(rocket.londowanie(r5))
    def update(i):
        '''funkcja rysuje wykres'''
        ax.clear()
        ax.set_facecolor(plt.cm.Blues(.2))

        ax.set_xlim([-100,100])
        ax.set_ylim([-100,100])
        ax.scatter(x=0, y=0,s=1000, c='purple', marker='o')
        ax.scatter(x=l1[i][0],y=l1[i][1],s=100, c='red', marker='o')
        ax.scatter(x=l2[i][0], y=l2[i][1],s=100, c='green', marker='o')
        ax.scatter(x=l3[i][0], y=l1[i][1],s=100, c='black', marker='o')
        ax.scatter(x=l4[i][0], y=l1[i][1],s=100, c='orange', marker='o')
        ax.scatter(x=l5[i][0], y=l1[i][1],s=100, c='yellow', marker='o')
        [spine.set_visible(False) for spine in ax.spines.values()]
    fig, ax = plt.subplots(figsize=(6, 6))
    anime = FuncAnimation(
        fig=fig,
        func=update,
        frames=len(l1),
        interval=50
    )

    plt.show()
if wybor=='jeden':
    r1 = rocket.Rocket(0, 0)
    l = []
    for x in range(100):
        z = random.uniform(-5, 5)
        y = random.uniform(-5, 5)
        rocket.move(r1, z, y)
        print('przesuniecie o wektor')
        print(z, y)
        print('pozycja')
        l.append(rocket.get_position(r1))
        print(rocket.get_position(r1))


    def update(i):
        '''tworzenie animacji'''
        ax.clear()
        ax.set_facecolor(plt.cm.Blues(.2))

        ax.set_xlim([-100, 100])
        ax.set_ylim([-100, 100])
        ax.scatter(x=l[i][0], y=l[i][1], c='red', marker='o')
        [spine.set_visible(False) for spine in ax.spines.values()]


    fig, ax = plt.subplots(figsize=(6, 6))
    anime = FuncAnimation(
        fig=fig,
        func=update,
        frames=len(l),
        interval=50
    )

    plt.show()