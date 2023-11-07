from datetime import datetime
import json
import paho.mqtt.client as mq
from os import path

CLIENT_ID = "RECEIVER_01"
MQTT_BROKER = "broker.emqx.io"
TOPIC = "Test/111"
PORT = 1883
FLAG_CONNECTED = False

data_file = r"C:\Users\Selim\Desktop\pythonmqtt\data.json"    
data_file_objects = []                

def on_connect(client, userdata, flags, rc):
    global FLAG_CONNECTED
    if rc == 0:
        FLAG_CONNECTED = True
        print("Connected to MQTT Broker")
    else:
        print("Failed to connect to Mqtt Broker!")

def on_message(client, userdata, msg):
    
    payload = str(msg.payload.decode())   
    payload_object = json.loads(payload) 
    print("||----MESSAGE RECEIVED ----||\n ")
    print("payload : " + str(payload_object))
    data_file_objects.append(payload_object)  

 
    with open(data_file, 'w') as file:
        json.dump(data_file_objects, file, indent=4, separators=(',', ': '))


if path.isfile(data_file) is False:
    raise Exception("Data file not found")

# Read the contents of the JSON messages from MQTT
with open(data_file) as fp:
    messages_file_objects = json.load(fp)
    client = mq.Client(CLIENT_ID)
    client.on_connect = on_connect
    client.on_message = on_message
