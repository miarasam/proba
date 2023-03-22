def pro(x,y,r):
    '''sprawdza czy taki dysk może istnieć o parametrach x,y,r i tworzy z tych parametrów listy '''
    if r>0:
        return False
    else:
        return [x,y,r]
def kolizja(dysk1,dysk2):
    '''sprawdza czy pomiedzy danymi dyskami zachodzi kolizja jesli tak daje true jesli nie false '''
    promienie = dysk1[2]+dysk2[2]
    dlugoscab = ((dysk2[1] - dysk1[1]) ** 2 + (dysk2[0] - dysk1[0]) ** 2) ** 0.5
    if promienie>dlugoscab:
        return True
    else:
        return False
def wek(przesuniecieox,przesuniecieoy,dysk):
    '''przesuwa podany dysk o podany wektor i wypisuje nowe wlasnosci'''
    dysk[0]=przesuniecieox+dysk[0]
    dysk[1]=przesuniecieoy+dysk[1]
    print(dysk)