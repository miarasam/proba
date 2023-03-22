z=[1,2,12]
pocz=[]
wysortowane=[]
pocz.extend(z)

for x in range(len(z)):
    z[x]=str(z[x])
    z[x]=ord(z[x])
for m in range(len(z)):
    wysortowane.append(min(z))
    z.remove(min(z))
for q in range(len(wysortowane)):
    wysortowane[q]=chr(wysortowane[q])
    wysortowane[q]=int(wysortowane[q])
def rownosc(one,two):
    return one==two
print(rownosc(pocz,wysortowane))
