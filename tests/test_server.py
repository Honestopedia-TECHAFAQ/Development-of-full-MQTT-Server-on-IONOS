import unittest
from mqtt_server.server import MQTTServer

class TestMQTTServer(unittest.TestCase):
    def test_initialization(self):
        server = MQTTServer()
        self.assertIsNotNone(server)

if __name__ == "__main__":
    unittest.main()
