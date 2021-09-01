# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 17:58:00 2021

"""
#import RPi.GPIO as GPIO
import time
from datetime import datetime, timedelta
from dateutil import parser

# input of persons time schedule
#persons_input = input('Please tell me what time?')

day_schedule = []
run_time_list = []

# each zone 1-6 maps to GPIO port +1 of the zone number
# 1 maps to 2, 2 to 3, etc.
zone_dict = {1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7}
day_dict = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday',
            4: 'Friday', 5: 'Saturday', 6: 'Sunday'}

# def start_relay(zone_number):
#     GPIO.setmode(GPIO.BCM)
#     GPIO.setup(zone_dict[zone_number])
#     GPIO.output(zone_dict[zone_number], True)
#     return(str(zone_dict[zone_number]) + ' is on')
    
# def stop_relay(relay_number):
#     GPIO.setmode(GPIO.BCM)
#     GPIO.setup(relay_number)
#     GPIO.output(relay_number, False)
    
# add a time to start to the run_time_list
def set_run_time(run_time):
    if type(run_time) == str:
        run_time_list.append(run_time)
    else:
        return('Invalid time')

def get_run_time():
    if len(run_time_list) > 0:
        return(run_time_list)
    else:
        return('List is empty')

def clear_run_time():
    if len(run_time_list) > 0:
        run_time_list.clear()     
    else:
        return('List is already empty')

def remove_single_run_time(run_time):
    if run_time in run_time_list:
        run_time_list.remove(run_time)
        return(run_time_list)
    else:
        return('Time not found')

def set_run_schedule(day):
    if type(day) == str:
        day_schedule.append(day)
    else:
        return('Invalid day')

def get_run_schedule():
    if len(day_schedule) > 0:
        return(day_schedule)
    else:
        return('List is empty')

set_run_schedule('Wednesday')

set_run_time('17:00:00')

# !!!TODO!!!
# Need this check time to only fire the command if the time is in the window
# and its a day that watering should happen
def check_day():
    now = datetime.now()
    for item in day_dict.values():
        for key, value in day_dict.items():
            if item == value:
                if key == now.weekday():
                    print('run today')
                    return(check_time())
                else:
                    print('no run today')
                
 

# function to check persons input against current time
# also adds to the time to create a window of time
def check_time():
        
    # find current time
    now = datetime.now()  
    
    # loops through times in the run time list
    for time_item in run_time_list:    
        
        # creates a datetime object from the time list item
        striped_time = datetime.strptime(time_item, '%H:%M:%S')
        
        # sets the time list item to todays date
        parsed_time = datetime(now.year, now.month, now.day, striped_time.hour, striped_time.minute)
        
        # if time between 1 minute prior or after the current time do the commands
        if parsed_time - timedelta(minutes=1) <= now <= parsed_time + timedelta(minutes=1):
            return('do command at time')
            # need a check that if this flag is on, do not run a second time
            # might actually be fine because the program will have already 
            # triggered the GPIO and water would still be on
        else:
            return('do nothing')
            # wont work here, would cause the loop to sleep after each item in the list
            #time.sleep(5)


#check_time()

check_day()
# # set loop to run continuously 
# running = True
    
# while running:
#     check_time(persons_input)  