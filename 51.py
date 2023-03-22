rgb=[100,10,255]
int(rgb[0]),int(rgb[1]),int(rgb[2])
p=0
for m in range(3):
    if rgb[m] > 255 or rgb[m] < 1 or len(rgb) != 3:
        print('nie istnieje')
        m=4
        p=1
if p==0:
    rgb[0]=hex(rgb[0]).strip("0x")
    rgb[1]=hex(rgb[1]).strip("0x")
    rgb[2]=hex(rgb[2]).strip("0x")
    z = [len(i) for i in rgb]
    for x in range(3):
        if z[x]!=2:
            rgb[x]='0'+rgb[x]
    print('#'+"".join(rgb))
