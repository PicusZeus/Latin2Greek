#from collections import Counter
#import re

#greek_untranslatables = frozenset([u'', ]) 

#def try_with_zipfs_law():
#  ''' Use Zipf's Law to identify words with the same counts'''
#  #use counter for greek and latin text
import os

import RPi.GPIO as GPIO

from bottle import get, post, run, request

# set board to Broadcom (so that the pins are numbered as shown
# here: http://pi.gadgetoid.com/pinout
GPIO.setmode(GPIO.BCM)

# prepare pins that we want to use
OPERATE_PIN = 2
STEER_PIN = 3
LIGHT_PIN = 4

for pin in pins:
    GPIO.setup(pin, GPIO.OUT)
#GPIO.setup(BUZZER_PIN, GPIO.OUT)

PIN_NAMES = {
    OPERATE_PIN: 'operate',
    STEER_PIN: 'steer',
    LIGHT_PIN: 'light',
}


ON = RIGHT = 0
OFF = LEFT = 1


def pubnub_publish(pin, status):
    """ Notify pubnub about the change"""
    cmd = "./pubnub_alarms {} {}".format(PIN_NAMES[pin], status)
    os.system(cmd)


def send_command(pin, state):
    """Send 0 or 1 to a given PIN """
    GPIO.output(pin, state)
    pubnub_publish(pin, state)


@post('/light/on')
def light_on():
    send_command(LIGHT_PIN, ON)
    return {'light': 'on'}


@post('/light/off')
def light_off():
    send_command(LIGHT_PIN, OFF)
    return {'light': 'off'}


@post('/operate/on')
def operate_on():
    send_command(OPERATE_PIN, ON)
    return {'operate': 'on'}


@post('/operate/off')
def operate_off():
    send_command(OPERATE_PIN, OFF)
    return {'operate': 'on'}


@post('/steer/left')
def steer_left():
    send_command(STEER_PIN, LEFT)
    return {'steer': 'left'}


@post('/steer/right')
def steer_right():
    send_command(STEER_PIN, RIGHT)
    return {'steer': 'right'}


@get('/status')
def status():
    return {
    'operate': "on" if GPIO.input(OPERATE_PIN) == 0 else "off",
    'steer': "on" if GPIO.input(STEER_PIN) == 0 else "off",
    'light': "on" if GPIO.input(LIGHT_PIN) == 0 else "off",
    }


if __name__ == "__main__":
    send_command(LIGHT_PIN, ON)
    send_command(LIGHT_PIN, OFF)
    run(host='0.0.0.0', port=80)
