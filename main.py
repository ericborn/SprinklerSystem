import time
from datetime import datetime

# input of persons time schedule
persons_input = input('Please tell me what time?')


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
  
# set loop to run continuously 
running = True
    
while running:
    check_time(persons_input)     