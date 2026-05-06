import paho.mqtt.client as mqtt
import os
from dotenv import load_dotenv

load_dotenv()

class MQTTClient:
    def __init__(self):
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        self.client.username_pw_set(os.getenv('USERNAME'), os.getenv('PASSWORD'))
        self.client.tls_set(certfile=None)
        self.client.connect(os.getenv('BROKER'), int(os.getenv('PORT')), 60)

    def _start(self):
        self.client.loop_start()

    def _publish(self, msg):
        self.client.publish('rele/controle', msg)

    def _message(self, callback):
        self.client.on_message = callback
    
    def _connect(self, callback):
        self.client.on_connect = callback
        self.client.subscribe('rele/estado')
    
    def _desconnect(self, callback):
        self.client.on_desconnect = callback
