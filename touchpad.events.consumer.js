const bodyParser = require('body-parser');
const express = require('express');
const robot = require('robotjs');
const app = express();
const { Observable, Subject } = require('rxjs');
const { multicast, bufferTime, switchMap, tap, pairwise, filter } = require('rxjs/operators');

let listener;
const events$ = Observable.create((_listener) => {
    listener = _listener;
}).pipe(multicast(new Subject()));
events$.connect();

app.use(bodyParser.json());

app.post('/', function(req, res) {
    listener.next(req.body);
    res.end();
});

app.listen(60000);

// left click
last_positions = [ { x: 0, y: 0 }, { x: 0, y: 0 } ];

CODE_ABX_X = 'ABS_X:0';
CODE_ABX_Y = 'ABS_Y:1';
events$.pipe(filter((e) => e.code === CODE_ABX_X || e.code === CODE_ABX_Y)).subscribe((e) => {
    last_positions[0] = last_positions[1];
    last_positions[1] = { x: last_positions[0].x, y: last_positions[0].y };
    switch (e.code) {
        case CODE_ABX_X:
            last_positions[1].x = e.value;
            break;
        case CODE_ABX_Y:
            last_positions[1].y = e.value;
            break;
    }
});

function distance(pt0, pt1) {
    const dx = pt1.x - pt0.x;
    const dy = pt1.y - pt0.y;
    return Math.sqrt(dx * dx + dy * dy);
}

events$.pipe(filter((e) => !(e.code === CODE_ABX_X || e.code === CODE_ABX_Y))).pipe(pairwise()).subscribe((events) => {
    const dt = events[1].time - events[0].time;
    if (dt > 50 && dt < 200 && distance(last_positions[0], last_positions[1]) < 10) {
        robot.mouseClick('left');
    }
});

// right click
if(false)
events$.pipe(bufferTime(500)).subscribe((events) => {
    if (events.length > 150 && distance(last_positions[0], last_positions[1]) < 10) {
        robot.mouseClick('right');
    }
});
