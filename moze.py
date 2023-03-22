slo='kot'
ana='ktt'
slo.lower()
ana.lower()
base=[*slo]
fake=[*ana]
base2=[]
fake2=[]
def rownosc(one, two):
    return one == two
if len(base)==len(fake):
    for x in range(len(base)):
        base[x]=ord(base[x])
        fake[x]=ord(fake[x])
    for c in range(len(fake)):
        base2.append(min(base))
        fake2.append(min(fake))
    print(rownosc(base2, fake2))
else:
    print(rownosc(base, fake))