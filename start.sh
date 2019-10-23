#/usr/bin/sh
ROOT_PWD=

pm2 start /home/edward/ELAN061B-touchpad-driver/touchpad.events.consumer.js
echo $ROOT_PWD | sudo -S bash -c 'chmod o+r /dev/input/event11'
echo $ROOT_PWD | sudo -S bash -c 'sudo pm2 start /home/edward/ELAN061B-touchpad-driver/touchpad.events.producer.py --interpreter python3 --interpreter-args -u'