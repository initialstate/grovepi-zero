from grovepi import grovepi
import os
import time

# --------- User Settings ---------
# The DHT_SENSOR_TYPE below may need to be changed depending on which DHT sensor you have:
#  0 - DHT11 - blue one - comes with the GrovePi+ Starter Kit
#  1 - DHT22 - white one, aka DHT Pro or AM2302
#  2 - DHT21 - black one, aka AM2301
DHT_SENSOR_TYPE = 1
# Connect the DHT sensor to one of the digital pins (i.e. 2, 3, 4, 7, or 8)
DHT_SENSOR_PIN = 4
# Set the time between sensor reads
SECONDS_BETWEEN_READS = 1
METRIC_UNITS = False
# ---------------------------------

def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

while True:
    try:
        [temp_c,hum] = grovepi.dht(DHT_SENSOR_PIN,DHT_SENSOR_TYPE)
        if isFloat(temp_c):
            if (METRIC_UNITS):
                print "Temperature(C) = " + str(temp_c)
            else:
                temp_f = temp_c * 9.0 / 5.0 + 32.0
                temp_f = float("{0:.2f}".format(temp_f))
                print "Temperature(F) = " + str(temp_f)
        if ((isFloat(hum)) and (hum >= 0)):
            print "Humidity(%) = " + str(hum)

    except IOError:
        print ("Error")

    time.sleep(SECONDS_BETWEEN_READS)