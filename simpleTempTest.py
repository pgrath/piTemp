#!/usr/bin/python

#using the adafruit dht11 driver
import Adafruit_DHT
import time

# Sensor should be set to Adafruit_DHT.DHT11
sensor = Adafruit_DHT.DHT11

# Example using a Raspberry Pi with DHT sensor
# connected to GPIO23.
#using pin 2
pin = 2

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).  
# If this happens try again!

temp = temperature * 1.8 + 32
print(temp)
print("in f")
def getTemp():
	if humidity is not None and temperature is not None:
		print 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)
	else:
		print 'Failed to get reading. Try again!'

#will repeat function
while True:
	getTemp()
	time.sleep(3)
