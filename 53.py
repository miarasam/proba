licz=40
def add(f1,f2):
    return f1+f2
fibb=[0,1]
for x in range(licz-2):
    f1=fibb[x]
    f2=fibb[x+1]
    fibb.append(add(f1, f2))
print(fibb)