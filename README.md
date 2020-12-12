# ELAN061B-touchpad-driver

## Background
- ELAN061B-touchpad is does not have clickable pad for left or right clicks but buttons at the bottom of the touchpad, which makes it difficult to use, so I custom make this driver to simulate left click and right click by double tapping and keep touching the pad.
- wanna try some cool libraries like [RxJS](https://rxjs-dev.firebaseapp.com/guide/overview), [RobotJs](https://github.com/octalmage/robotjs)
## Dependencies
- yarn
- node
- pm2
- python
  - pyudev
  - libevdev

## Install
```sh
yarn install
```

## Config
- config your sudo pwd in start.sh for reading touchpad events from /dev/input/event{??} directory

## Start
```sh
./start.sh
```

## Notes
At first, I wanna do it all in python, but rxpy library seems to be difficult to use in python, so I decide to forward the event for rxjs to process, which I have thought to use fifo or http to let them communicate. I finally choose http for ease.

## Pending
- will use machine learning techniques to increase precision of multiple click detection
