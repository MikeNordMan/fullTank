'''Создание клиетнтского MQTT'''
'''в функцию on_connect добавил properties и... заработало
   так же прищлось пришлось добавить mqtt_client.CallbackAPIVersion.VERSION2 
   в client = mqtt_client.Client изнасально было client = mqtt_client.Client(client_id)
   на малинке пришлось все это убрать!!!
   дальше продолжаем сдесь и корректируем на малинке'''

'''Переносим на малинку'''

from paho.mqtt import client as mqtt_client


broker = 'm4.wqtt.ru'
port = 8626
topic = "p/mqtt"

client_id = 'u_DDEQIA'
username = 'u_DDEQIA'
password = 'WkzNqZHN'


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc, properties):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION2, client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    print('im here')
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()