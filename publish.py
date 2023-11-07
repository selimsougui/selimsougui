from datetime import datetime
import time
import json
import paho.mqtt.client as mq
from paho.mqtt import client


CLIENT_ID = "PUBLISHER_01"
MQTT_BROKER = "broker.emqx.io"
TOPIC = "Calcul/Tiempo"
PORT = 1883
FLAG_CONNECTED = False


x = 0
y = 0
total=0


def publish_message():
    global total
    timestamp = str(datetime.now().strftime("%H:%M:%S")) 
    msg_dictionary = {    
        "timestamp": timestamp,
        "total": total,
                    }
    msg = json.dumps(msg_dictionary) 
    try:
         result = client.publish(TOPIC, msg)  
    except :
        print("There was an error while publishing the messange")
    time.sleep(2)
    print("Message sent to the MQTT BROKER")


def on_connect(client, userdata, flags ,rc):
    global FLAG_CONNECTED
    if rc == 0:
        FLAG_CONNECTED = True
        print("Connected to MQTT Broker")
    else:
        print("Faild to connect to Mqtt Broker!")

client = mq.Client(CLIENT_ID)
client.on_connect = on_connect
client.connect(MQTT_BROKER, PORT)
client.subscribe(TOPIC, 0)

while True:

    total=x+y
    print("x =  : " + str(x))
    print("y= :" + str(y))
    print("total =  " + str(total))
    publish_message() 
    x = x +1
    y = y+2
