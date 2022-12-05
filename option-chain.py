#class concept


class bala():
    def chandar(self):
        print('hey senamika')
    def selvi(self):
        print('gethu')
    def amma(self):
        print('amma')
    def appa(self):
        print('vera level')

'''

d = bala()
d.chandar()
d.selvi()
d.appa()

'''


class demo():
    def __int__(self):
        bal = 'hey thoapakata'
        print('constructor method')

    def show(self,bal):
        print('execute show', bal)
'''
bal = 'hey thoapakata'
b = demo()
b.show(bal)
'''

class student():
    global selfname, selfskill, selfperformance
    selfname = 'Bala'
    selfskill = 'good'
    selfperformance = 'Extraordinary'
    def __int__(self):
        self.name = 'Bala'
        self.skill = 'good'
        self.performance = 'Extraordinary'
    def priint(self):
        print(selfname, selfskill, selfperformance)

'''
baa = student()
baa.priint()
'''

class hell:
    def __int__(self):
        self.name = 57
#    def name(self,name):
#        print('the name is',name)

'''
he = hell()
he.name(52)
'''

class variable:
    love = "don't know"

    def __int__(self):
        variable.love = 'i aam not sure'
    def insmethod(self):
        love = 'searching'
    @classmethod
    def clsmethod(cls):
        cls.love = 'will find it'



x = 10

def show():
#    global x
#    x = x+10
    print(x+1)


show()

print(x)