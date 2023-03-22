from lista import vector
v1=vector()
v1.los()
print(v1)

v2=vector()
v2.stwwla([1,2,3])
print(v2)

v3=vector()
v3.stwwla([1,1,1])

print(v2.skalar(5.5))

print(v2.dlug())

print(v2.sum())

print(v3.iloskal(v1))

print(v3.__contains__(3))

print(v1+v2)

print(v1-v2)

print(v1.__getitem__(2))

print(1 in v2)