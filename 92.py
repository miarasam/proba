import rocket
import random
r1=rocket.Rocket(0,0)
for x in range(10):
    z=random.uniform(-10,10)
    y=random.uniform(-10,10)
    rocket.move(r1,z,y)
    print('przesuniecie o wektor')
    print(z,y)
    print('pozycja')
    rocket.get_position(r1)

