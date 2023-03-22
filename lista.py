import random
class vector:

    def __init__(self,args=3):
        "funkcja tworzy wektor o danej ilosci argumentow uzupelniajac je zerami"
        self.list=([0]*args)

    def los(self):
        """funkcja losuje losowe wartosci wektorów od -100 do 100 i
        nadpisuje je nad wczesniejsze wartosci"""
        for i in range(len(self.list)):
            self.list[i]=random.uniform(-100,100)


    def stwwla(self,lista_wart):
        """
        funkcja:
        nadpisuje wektor o podanych wartoscich w liscie
        parametr:
        lista zawierajaca tyle elementow co wczesniej stworzony wektor
        output:
        nowe wartosci funkcji
        """
        if len(lista_wart)!=len(self.list):
            raise ValueError("zły wymiar vektora")
        else:
            self.list=lista_wart
        return self.list

    def __add__(self,a):
        """operator dodaje dwa wektory"""
        c=[]
        if len(a.list)!=len(self.list):
            raise ValueError("zły wymiar vektora")
        else:
            for i in range(len(self.list)):
                d=self.list[i]+a.list[i]
                c.append(d)
        return c

    def __sub__(self,a):
        """"operator odejmowania dwoch wektorow"""
        b=[]
        if len(a.list)!=len(self.list):
            raise ValueError("zły wymiar vektora")
        else:
            for i in range(len(self.list)):
                c=self.list[i]-a.list[i]
                b.append(c)
        return b

    def skalar(self,skalary):
        """funkcja
        mnozy wektor przez skalar
        parametr:
        float(skalary)
        output:
        wektor pomnozony przez skalar"""
        b=[]
        for x in range(len(self.list)):
            b.append(self.list[x]*skalary)
        return b

    def dlug(self):
        """funkcja: oblicza dlugosc wektora
        output dlugosc wektora"""
        b=[]
        for x in range(len(self.list)):
            b.append(self.list[x]**2)
        c=sum(b)**(1/2)
        return c

    def sum(self):
        """funkcja oblicza sume elementow wektora
        output suma elementow wektora"""
        b=sum(self.list)
        return b

    def iloskal(self,a):
        """funkcja oblicza iloczyn skalarny dwoch wektorow
        parametr: a wektor/lista o rownej ilosci parametrow
        output: iloczyn skalarny"""
        b=[]
        if len(a.list)!=len(self.list):
            raise ValueError("zły wymiar vektora")
        else:
            for i in range(len(self.list)):
                b.append((self[i] * a[i]))
        return sum(b)

    def __str__(self):
        """operator reprezentujacy wektory za pomoca tekstu"""
        return 'wektor to '+ str(self.list)

    def __getitem__(self, item):
        """operator pozwalajacy na dostep do danej czesci wektora"""
        if len(self.list)<=item or -len(self.list)>item:
            raise ValueError("argument poza listą")
        else:
            return self.list[item]

    def __contains__(self, item):
        """operator pozwalajacy sprawdzic czy dana liczba jest w wetorze
        parametr item(float)
        output jesli sie znajduje to returnuje true jesli nie to false"""
        return item in self.list
