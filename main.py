# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 17:58:00 2021

"""
import RPi.GPIO as GPIO
import time
from datetime import datetime

# input of persons time schedule
#persons_input = input('Please tell me what time?')

program_schedule = []

# each zone 1-6 maps to GPIO port +1 of the zone number
# 1 maps to 2, 2 to 3, etc.
zone_dict = {1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7}

def start_relay(zone_number):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(zone_dict[zone_number])
    GPIO.output(zone_dict[zone_number], True)
    return(str(zone_dict[zone_number]) + ' is on')
    
def stop_relay(relay_number):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(relay_number)
    GPIO.output(relay_number, False)

# function to check persons input against current time
# also adds to the time to create a window of time
def check_time(time):
    
    # adjust forward 1 minute
    adjusted_time = time + ' add 1'
    
    # find current time and convert to hour, min, sec
    now = datetime.now()
    cur_time = now.strftime("%H:%M:%S")
    
    # print the time and adjusted time
    print(time)
    print(adjusted_time)
    
    # if time between range, do command, otherwise sleep for 5
    if '19:56:00' <= cur_time <= '19:57:00':
        print('do command at time')
    else:
        print('do nothing')
        time.sleep(5)
  
# # set loop to run continuously 
# running = True
    
# while running:
#     check_time(persons_input)  