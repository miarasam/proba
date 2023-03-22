class Rocket:
  ''''''
  def __init__(self,x,y):
    '''tworzy klase rocket'''
    self.x=x
    self.y=y
  def move(self,przesuniecieox,przesuniecieoy):
    '''przesuwa rakiete o dane wspolzedne'''
    self.x=przesuniecieox+ self.x
    self.y=przesuniecieoy+self.y
  def get_position(self):
    '''oddaje pozycje wybranej rakiety w liscie'''
    return [self.x,self.y]
  def get_distance(self,rakieta2,rakieta3,rakieta4,rakieta5):
    '''liczy i pisze w konsoli odleglosc miedzy glowna rakieta a pozostalymi'''
    print((((rakieta2.x-self.x)**2+(rakieta2.y-self.y)**2)**(1/2)),(((rakieta3.x - self.x) ** 2 + (rakieta3.y - self.y) ** 2) ** (1 / 2)),
      (((rakieta4.x - self.x) ** 2 + (rakieta4.y - self.y) ** 2) ** (1 / 2)),
      (((rakieta5.x - self.x) ** 2 + (rakieta5.y - self.y) ** 2) ** (1 / 2)))

  def londowanie(self):
    '''sprawdza kiedy rakieta londuje na planecie'''
    k=[]
    londuje=((self.x)**2+(self.y)**2)**(0.5)
    if londuje<14:
      return 'rakieta wyladowala'






