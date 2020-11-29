# -*- coding: utf-8 -*-
import socket
import os

socket_path = "/tmp/touchpad_event_socket.sock"

unix_socket = 0
print("Connecting...")
if os.path.exists(socket_path):
    unix_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    unix_socket.connect(socket_path)
    # while True:
    #     try:
    #         x = input("> ")
    #         if "" != x:
    #             print("SEND:", x)
    #             client.send(x.encode('utf-8'))
    #             if "DONE" == x:
    #                 print("Shutting down.")
    #                 break
    #     except KeyboardInterrupt as k:
    #         print("Shutting down.")
    #         client.close()
    #         break
else:
    print("Couldn't Connect!")
    print("Done")
    exit

#-----------------------------------------


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
    # requests.post('http://localhost:60000', json={'code': str(e.code),'type':str(e.type), 'value': e.value, 'time': time.mktime(then.timetuple())*1e3 + then.microsecond/1e3})
    unix_socket.send(bytes(json.dumps({'code': str(e.code),'type':str(e.type), 'value': e.value, 'time': time.mktime(then.timetuple())*1e3 + then.microsecond/1e3}), "utf-8"))

## parse events @depreciated
# listener.subscribe(lambda e: print(e))