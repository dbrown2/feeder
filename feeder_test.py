# test feeder control with python script

import pifacedigitalio as pf
from time import sleep






if __name__ == '__main__':
    pf.init()

    # set forward direction
    pf.digital_write(1,0)
    sleep(1)
    # turn on motor
    print('Running motor forward...')
    pf.digital_write(0,1)
    sleep(5)
    print('Changing Direction..')
    # turn off motor
    pf.digital_write(0,0)
    sleep(1)
    # set reverse direction
    pf.digital_write(1,1)
    sleep(1)
    # turn on motor
    print('Running motor reversed...')
    pf.digital_write(0,1)
    sleep(5)
    # turn off motor
    pf.digital_write(0,0)
    print('Done!')
    
   
