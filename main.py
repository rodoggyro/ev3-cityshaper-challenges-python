#!/usr/bin/env micropython
import time
from ev3dev2.motor import OUTPUT_A, OUTPUT_D, MoveTank, SpeedPercent, follow_for_ms
from ev3dev2.sensor.lego import GyroSensor, UltrasonicSensor
from ev3dev2.sound import Sound
import os
from sys import stderr

us = UltrasonicSensor()
gyro = GyroSensor()

def reset():  
    for sleepTime in [2, 0.5]:
        gyro.mode = 'GYRO-RATE'
        gyro.mode = 'GYRO-ANG'
        time.sleep(sleepTime)
    us.mode = 'US-DIST-CM'   

def gyro_follow():
    tank_drive = MoveTank(OUTPUT_A, OUTPUT_D)
    run = True
    while run:
        current_angle = gyro.angle
        tank_drive.on(SpeedPercent(25), SpeedPercent(25))
        if current_angle >= 1:
            tank_drive.on(SpeedPercent(25), SpeedPercent(37.5))
        elif current_angle <= -1:
            tank_drive.on(SpeedPercent(37.5), SpeedPercent(25))
        if us.distance_centimeters <= 20:
            tank_drive.stop()
            break
        
reset()
gyro_follow()


print('Please Run Again Or Change E V 3 Code')
time.sleep(10)