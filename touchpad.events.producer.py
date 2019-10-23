import pyudev
context = pyudev.Context()

## find touchpad device path
touchpad_device = None
for device in context.list_devices(subsystem='input'):
  for key, value in device.items() :
    if 'ID_INPUT_HEIGHT_MM' == key:
      touchpad_device = device

touchpad_device_path = [value for key, value in touchpad_device.items() if key == 'DEVNAME'][0]

## prepare queue @depreciated
# import rx
# from rx import create
# listener = None
# def sub(_):
#   listener = _
# events = create(sub)

## read touchpad device value
import requests
import json
import libevdev
import time
import datetime
fd = open(touchpad_device_path, "rb") 
device = libevdev.Device(fd)
while(True):
  for e in device.events():
    ## @depreciated
    # if listener:
    #   listener.on_next(e)

    ## use http to push device event stream
    # print(e.type)
    # print(e.value)
    # print(e.code)
    print((e))
    then = datetime.datetime.now()
    requests.post('http://localhost:60000', json={'code': str(e.code),'type':str(e.type), 'value': e.value, 'time': time.mktime(then.timetuple())*1e3 + then.microsecond/1e3})

## parse events @depreciated
# listener.subscribe(lambda e: print(e))