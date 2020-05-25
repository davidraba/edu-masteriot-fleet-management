import os
from mongo import Mongo
from mqtt import MQTT
from signal import pause

hostDB = os.getenv('HOSTDB', 'db_host')
portDB = os.getenv('PORTDB', 27017)

print("{}::{}".format(hostDB, portDB))
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
