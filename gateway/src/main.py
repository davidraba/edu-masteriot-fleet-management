import os
from mongo import Mongo
from mqtt import MQTT
from signal import pause

hostDB = os.getenv('HOSTDB', 'edu.insylo.io')
portDB = os.getenv('PORTDB', 47017)

mongo = Mongo(hostDB, portDB)
mqtt = MQTT(mongo)

mongo.connect()
mqtt.run()

try:
    pause()
except KeyboardInterrupt:
    pass

mqtt.stop()
mongo.disconnect()
