import kolmod
import dyskmod
dyskmod.pro([10,1,1])
dyskmod.pro([0,0,1])
if kolmod.kolizja([10,1,1],[0,0,1])==True:
    print(True)
else:
    print(False)
