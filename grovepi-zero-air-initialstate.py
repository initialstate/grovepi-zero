from grovepi import grovepi
import time
from ISStreamer.Streamer import Streamer

# --------- User Settings ---------
# Connect the Grove Air Quality Sensor to one of the analog pins (i.e. 0, 1, 2)
AIR_SENSOR_PIN = 0
# Initial State settings
BUCKET_NAME = ":partly_sunny: Indoor Environment"
BUCKET_KEY = "GPZa"
ACCESS_KEY = "PLACE YOUR INITIAL STATE ACCESS KEY HERE"
# Set the time between sensor reads
MINUTES_BETWEEN_READS = 1
# ---------------------------------

def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

streamer = Streamer(bucket_name=BUCKET_NAME, bucket_key=BUCKET_KEY, access_key=ACCESS_KEY)

while True:
    try:
        airSensorVal = grovepi.analogRead(AIR_SENSOR_PIN)

        if isFloat(airSensorVal):
            if airSensorVal > 700:
                # print "High pollution"
                streamer.log("Air Quality", ":fog: :bangbang:")
            elif airSensorVal > 300:
                # print "Low pollution"
                streamer.log("Air Quality", ":foggy: :exclamation:")
            else:
                # print "Air fresh"
                streamer.log("Air Quality", ":rainbow:")

            # print "Air Quality =", airSensorVal
            streamer.log("Air Quality Sensor", airSensorVal)
            streamer.flush()

    except IOError:
        print "Error"

    time.sleep(60*MINUTES_BETWEEN_READS)
