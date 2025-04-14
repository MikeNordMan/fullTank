import tkinter
from tkinter import *


class SettingsPump(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.timeMax = 0 # Время работы скважены max(мин)
        self.timeRecicle = 0 # Время работы восстановления скважены (мин)
        self.powerPump = 0 # Мощность насоса
        self.rainSensor = False # Датчик дождя
        
    def setTimeMax(timeMax):
        self.timeMax = timeMax
    def setTimeRecicle(timeRecicle):
        self.timeRecicle = timeRecicle
    def setPowerPump(powerPump):
        self.powerPump = powerPump
    def setRainSensor(rainSensor):
        self.rainSensor = rainSensor
        
        
    def getTimeMax():
        return self.timeMax
    def getTimeRecicle():
        return self.timeRecicle
    def getPowerPump():
        return self.powerPump
    def getRainSensor():
        return self.rainSensor