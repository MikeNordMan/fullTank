# Пытаемся создать скрипт для публикации сообщений на малинке
import time
from paho.mqtt import client as mqtt_client

broker = '"192.168.68.116"'
port = 1883
topic = "hello/world"
client_id ='myname'

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Подключено к брокеру MQTT!")
        else:
            print("Не удалось подключиться, код возврата %d\n", rc)

    client = mqtt_client.Client(client_id) # client.username_pw_set(имя пользователя, пароль)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish ( client ):
    msg_count = 1
    while True :
        time.sleep( 1 )
        msg = f"messages: {msg_count}"
        result = client.publish(topic, msg) # result: [0, 1]
        status = result[ 0 ]
        if status == 0 :
             print ( f"Отправить ` {msg} ` в тему ` {topic} `" )
        else :
             print ( f"Не удалось отправить сообщение в тему {topic} " )
        msg_count += 1
        if msg_count > 5:
            break

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)
    client.loop_stop()


if __name__ == '__main__':
     run()

