from time import sleep
import random
import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

# The callback for when a PUBLISH message is received from the server.
def on_publish(client, userdata, message_id):
    print(f"message with ID {message_id} published")
    

def color_Swap():
    random_number = random.randint(0,16777215)
    hex_number = str(hex(random_number))
    hex_number ='#'+ hex_number[2:]
    return hex_number
    
    
    #colors = ["coolest", "cool","neutral", "warm", "warmest"]
    #while i < 5:
        #return colors[i]
        
client = mqtt.Client()
# Client callback that is called when the client successfully connects to the broker.
client.on_connect = on_connect
# Client callback that is called when the client successfully publishes to the broker.
client.on_publish = on_publish


# Connect to the MQTT broker running in the localhost.
client.connect("192.168.110.55", 1883, 60)
message_counter = 0
i = 0
client.publish("zigbee2mqtt/LED/set", "on")
# The client will publish a message to the broker every 3 seconds.
while True:
   x = color_Swap()
   print(x)
   #client.publish("zigbee2mqtt/LED/set/effect", "breath")
   client.publish("zigbee2mqtt/LED/set/color", x)
   i += 1
   if i == 5:
       i = 0
   message_counter += 1
   sleep(2)
