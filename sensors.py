import RPi.GPIO as GPIO
import time, threading, dht11
from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory, PNOperationType
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
import sys
import Adafruit_DHT

pnconfig = PNConfiguration()

pnconfig.subscribe_key = 'sub-c-99b2f757-497d-4a91-861b-95ce13125533'
pnconfig.publish_key = 'pub-c-d6e8028a-60ab-4860-85d8-84e6af8d04a6'
pnconfig.user_id = '6e6e91be-676d-11ed-9022-0242ac120002'
pubnub = PubNub(pnconfig)

my_channel = "Channel-Pumpkin"
sensors_list = ["dht11"]
data = {}

def my_publish_callback(envelope, status):
    # check was the request successfully completed
    if not status.is_error():
        pass # Message was sucessfully published
    else:
        pass # Handle the publish message error. Can more details about the error by looking at the 'cateogey' property


class MySubscribeCallback(SubscribeCallback):
    def presence(self, pubnub, presence):
        pass # handle incoming presence data

    def status(self, pubnub, status):
        if status.category == PNStatusCategory.PNUnexpectedDisconnectCategory:
            pass # What should you do if connection drops

        elif status.category == PNStatusCategory.PNConnectedCategory:
            # Connect event. Publish something
            pubnub.publish().channel(my_channel).message("Hello World").pn_async(my_publish_callback)
        
        elif status.category == PNStatusCategory.PNReconnectedCategory:
            pass
            # This happens when disconnected and then reconnected

        elif status.category == PNStatusCategory.PNDecryptionErrorCategory:
            pass
            # Client configured to encrypt messages and the live feed recevies plain text

    def message(self, pubnub, message):
        try:
            print(message.message, " : ", type(message.message))
            msg = message.message
            print("Received json: ", msg)
            keys = list(msg.keys())
            if(key[0]) == "event": #{"event" : {"sensors_name":True}}
                self.handle_event(msg)
        except Exception as e:
            print("Received: ", message.message)
            print(e)


    def handle_event(self, msg):
        global data
        event_data = msg["event"]
        keys = list(event_data.keys())
        if key[0] in sensors_list:
            if event_data[key[0]] is True:
                data["dht11"] = True
            elif event_data[key[0]] is False:
                data["dht11"] = False

def publish(pub_channel, msg):
    pubnub.publish().channel(pub_channel).message(msg).pn_async(my_publish_callback)

#Function for sensor dht11 and csv output

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
id=int(0)
idPlant=int(1)
instance = dht11.DHT11(pin=4)

def temp_humidity():
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(11, 4)
        print('Temp: {0:0.1f} C Humidity: {1:0.1f} %'.format(temperature, humidity))
        time.sleep(1)


if __name__ == '__main__':
    sensors_thread = threading.Thread(target=temp_humidity())
    sensors_thread.start()
    pubnub.add_listener(MySubscribeCallback())
    pubnub.subscribe().channels(my_channel).execute()


# PIR_pin = 23
# Buzzer_pin = 24

# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(PIR_pin, GPIO.IN)
# GPIO.setup(Buzzer_pin, GPIO.OUT)

# def beep(repeat):
#     for i in range(0, repeat):
#         for pulse in range(60):
#             GPIO.output(Buzzer_pin, True)
#             time.sleep(0.001)
#             GPIO.output(Buzzer_pin, False)
#             time.sleep(0.001)
#         time.sleep(0.02)


# def motion_detection():
#     data["alarm"] = False
#     trigger = False
#     while True:
#         if GPIO.input(PIR_pin):
#             print("Motion detected")
#             beep(4)
#             trigger = True
#             publish(my_channel, {"motion":"Yes"})
#             time.sleep(1)
#         elif trigger:
#             publish(my_channel, {"motion":"No"})
#             trigger = False
#         if data["alarm"]:
#             beep(2)


