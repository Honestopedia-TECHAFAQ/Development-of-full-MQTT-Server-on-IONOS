import paho.mqtt.client as mqtt
import config

class MQTTServer:
    def __init__(self):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def on_connect(self, client, userdata, flags, rc):
        """Callback when the client connects to the broker."""
        if rc == 0:
            print(f"Connected successfully to MQTT broker at {config.MQTT_HOST}:{config.MQTT_PORT}")
            self.client.subscribe(config.SUBSCRIBE_TOPIC)
        else:
            print(f"Failed to connect, return code {rc}")

    def on_message(self, client, userdata, msg):
        """Callback when a message is received from the broker."""
        print(f"Message received on topic {msg.topic}: {msg.payload.decode()}")
        self.process_message(msg)

    def process_message(self, msg):
        """Process the message received from the sensor."""
        if msg.topic == config.SUBSCRIBE_TOPIC:
            message_payload = msg.payload.decode()
            if "trigger_actuator" in message_payload:
                response_message = "Actuator triggered by sensor"
                print(f"Publishing to {config.PUBLISH_TOPIC}: {response_message}")
                self.client.publish(config.PUBLISH_TOPIC, response_message)

    def start(self):
        """Connect to the MQTT broker and start the loop."""
        try:
            self.client.connect(config.MQTT_HOST, config.MQTT_PORT, 60)
            self.client.loop_forever()
        except Exception as e:
            print(f"Error while connecting or processing messages: {str(e)}")
if __name__ == "__main__":
    server = MQTTServer()
    server.start()
