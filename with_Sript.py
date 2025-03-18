# Тестовый класс сценария
# Поля создания класса: string Имя, String Время начала работы сценария, String Время окончания работы сценария 
class MyScript():
    def __init__(self, nameSt, tmStart, tmFin):
        self.nameSt = nameSt
        self.tmStart = tmStart
        self.tmFin = tmFin
    
    def getNameSt(self):
        #print('ghjhjgjh')
        return self.nameSt
    def getTmStart(self):
        return self.tmStart
    def getTmFin(self):
        return self.tmFin

'''
def main():
    sr = MyScript('first','10:30','21:20')
    print('heloo')
    print(sr.getNameSt())

if __name__ == "__main__" :
    main()
'''