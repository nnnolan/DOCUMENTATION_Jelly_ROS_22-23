#!/usr/bin/env python3

import rospy
import time
import serial
from std_msgs.msg import Float32

rospy.init_node("hydrophone_test")

generic_publisher = rospy.Publisher('/jelly/delay',Float32,queue_size=1)

def main():
    '''
    Main program function
    '''

    ser = serial.Serial('/dev/ttyS1', 9600)

    while (True):
        l = ser.readline()
        delay_time = float(l)
        message = Float32()
        message.data = delay_time
        generic_publisher.publish(message)
        # print(twos_comp(data, 8), ": ", bin(data)) # print the value of Port B
        time.sleep(0.5)  # Wait 500ms


if __name__ == "__main__":
    main()
