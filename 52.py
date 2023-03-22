html='#640af'
z=[*html]
xd=0
if len(z)!=7:
    raise ValueError('bład')
    xd=1
if xd==0:
    del z[0]
    d = []
    p = 0
    for x in range(len(z)):
        z[x] = int(z[x], base=16)
    for m in range(3):
        d.append(16 * z[p] + z[p + 1])
        p = p + 2
    print(d)
