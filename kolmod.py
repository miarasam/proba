def kolizja(dysk1,dysk2):
    '''sprawdza czy pomiedzy danymi dyskami zachodzi kolizja jesli tak daje true jesli nie false '''
    promienie = dysk1[2]+dysk2[2]
    dlugoscab = ((dysk2[1] - dysk1[1]) ** 2 + (dysk2[0] - dysk1[0]) ** 2) ** 0.5
    if promienie>dlugoscab:
        return True
    else:
        return False
