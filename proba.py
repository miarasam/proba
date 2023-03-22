class vec:
    def __int__(*args):
        print('wek stwo',len(args))
        for arg in args:
            print('war',arg)
        lista=[0,1,2]
    def __str__(self):
        return 'wekt x={0.a} y={0.b} z={0.c}'.format(self)
    def __add__(self, abba):
        self[0]=self[0]+abba[0]