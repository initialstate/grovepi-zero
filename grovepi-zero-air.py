from grovepi import grovepi
import time

# --------- User Settings ---------
# Connect the Grove Air Quality Sensor to one of the analog pins (i.e. 0, 1, 2)
AIR_SENSOR_PIN = 0
# Set the time between sensor reads
SECONDS_BETWEEN_READS = 1
# ---------------------------------

def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

while True:
    try:
        airSensorVal = grovepi.analogRead(AIR_SENSOR_PIN)

        if isFloat(airSensorVal):
            if airSensorVal > 700:
                print "High pollution"
            elif airSensorVal > 300:
                print "Low pollution"
            else:
                print "Air fresh"

            print "Air Quality = ", airSensorVal

    except IOError:
        print "Error"

    time.sleep(SECONDS_BETWEEN_READS)
