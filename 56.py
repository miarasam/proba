z=['1','2','12']
p=[]
w=[]
w.extend(z)
for x in range(len(z)):
    p.append(min(z))
    z.remove(min(z))
def rownosc(one,two):
    return one==two
print(rownosc(p,w))