import random


def haslo(liczba_znakow,zbior):
    l=[]
    if 'a' in zbior:
        for x in range(26):
            l.append(chr(x+97))
    if 'b' in zbior:
        for xx in range(26):
            l.append((chr(xx+65)))
    if 'c' in zbior:
        for xxx in range(10):
            l.append(xxx)
    if 'd' in zbior:
        for xxxx in range(33,127):
            if xxxx<48 or xxxx>57 and xxxx<65 or xxxx>90 and xxxx<97 or xxxx>122:
                l.append(chr(xxxx))
    if 'e' in zbior:
        p=[260,262,280,321,	323,211,346,377,379,261,263,281,322,324,243,347,378,380]
        for z in range(len(p)):
            l.append(chr(p[z]))
    haselko=random.choices(l,k=liczba_znakow)
    return (''.join(haselko))

print(haslo(8,'abcde'))
