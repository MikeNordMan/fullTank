'''Доработать'''

import time
from paho.mqtt import client as mqtt_client


class MyPaho():
    def __int__(self):
        #self.broker = "192.168.68.116"
        #self.port = 1883
        self.topic = "hello/world"
        #self.client_id ='myname'
        #self.client = None
    def connect_mqtt(self) -> mqtt_client:
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Подключено к брокеру MQTT!")
            else:
                print("Не удалось подключиться, код возврата %d\n", rc)

        self.client = mqtt_client.Client('myname')
        self.client.on_connect = on_connect
        self.client.connect("192.168.68.116", 1883)
        return self.client

    def publish(self, client, topic):
        while True:
            time.sleep(1)
            msg_count = "eeesss"
            msg = f"messages: {msg_count}"
            result = client.publish(topic, msg)
            status = result[0]
            if status == 0:
                print(f"Отправить ` {msg} ` в тему ` {topic} `")
            else:
                print(f"Не удалось отправить сообщение в тему {topic} ")

            break

    def run(self):
        self.client = self.connect_mqtt()
        self.client.loop_start()
        self.publish(self.client, "hello/world")
        self.client.loop_stop()
