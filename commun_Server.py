'''
Цель - организация связи с сервером (Малинка) через класс
    отправка и приес сообщений

    1. Настройка класса произведена
    2. Попытка содинить с приложением (не получилось)
    3. Пробуем ПОТОК (непонятна передача данных между потоками)
    4. Попытка содинить с приложением (получилось, loop_forever блокировал,
     заменил на loop_start)
    5.
'''

import time
import asyncio
import tkinter
from tkinter import *
from paho.mqtt import client as mqtt_client

class ComRaspbery():
#class ComRaspbery(tkinter.Frame):
    def __init__(self, infoMsg):
    #def __init__(self):
    #def __init__(self, master):
        #super().__init__(master)
        self.infoMsg = infoMsg  # Экземпляр Инфокласса
        self.broker = "192.168.68.116"
        self.port = 1883
        self.topic = "hello/world"
        self.client_id ='myname'
        self.countMSGstart = 0 # Счетчик сообщений о подключении устройства
        self.countMSGoff = 0 # Счетчик сообщений об отключении устройства

        self.frame = Frame()
        #self.runConnect()

    def connect_mqtt(self):
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Подключено к брокеру MQTT!")
            else:
                print("Не удалось подключиться, код возврата %d\n", rc)

        self.client = mqtt_client.Client(self.client_id)
        self.client.on_connect = on_connect
        self.client.connect(self.broker, self.port)

        return self.client

    #def publish(self, client, topic, text):
    def publish(self, topic, text):
        while True:
            time.sleep(1)
            msg = f"messages: {text}"
            result = self.client.publish(topic, msg)
            status = result[0]
            if status == 0:
                print(f"Отправить ` {msg} ` в тему ` {topic} `")
            else:
                print(f"Не удалось отправить сообщение в тему {topic} ")

            break

    def subscribe(self, client):
        def on_message(client, userdata, msg):
            textMsg = msg.payload.decode()
            #print(textMsg)
            topic = msg.topic
            #print(topic)
            '''тут работать с сообщениями'''
            if topic == "hello/world":
                print('В тему пришло')


            if topic == 'dev/start':
                self.countMSGstart += 1
                if self.countMSGstart > 1:
                    print('Устройство Включено')
                    self.sendMsgInfo('Устройство Включено')
                    self.infoMsg.setDevice_flag()
                    print(self.infoMsg.getDevice_flag())

            if topic == 'dev/life':
                self.countMSGoff +=1
                if self.countMSGoff > 1:
                    print('Потеряна связь с устройством!')
                    self.sendMsgInfo('Потеряна связь с устройством!')
                    self.infoMsg.setDevice_flag()
                    print(self.infoMsg.getDevice_flag())

        client.subscribe('hello/world')
        client.subscribe('dev/life')
        client.subscribe('dev/start')
        client.on_message = on_message



    def runConnect(self): # Тут запускаемся
        print('Start')
        self.client = self.connect_mqtt()
        self.subscribe(self.client)
        #self.client.loop_forever() не работает
        self.client.loop_start() # работает вроде


    def connectDevice(self):
        pass

    def setTopic(self):
        pass

    def getTopic(self):
        return self.topic

    def sendMsgInfo(self, text): # Вывод сообщений работы сервера на экран
        self.infoMsg.setMsg(text)

    ''''При подключении к брокеру необходимо убирать первые сообщения из топиков'''
    def clearTopic(self, count):
        if count > 1:
            return True


    '''
    def sleepDevice(self):
            self.publish(self.client, 'device/sleep', 'y')
            print('Отправленно')
            self.timer = self.frame.after(10000, self.sleepDevice)
    '''
    def setFlagSleep(self):
        pass
'''
def app():
    nConnect = ComRaspbery()
    nConnect.runConnect()

if __name__ == '__main__':
    app()
'''