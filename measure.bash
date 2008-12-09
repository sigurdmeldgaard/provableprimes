#!/usr/bin/env bash
TIMEFORMAT=$'%3lU'
for i in 100 200 300 400 500 600 700 800 900 1000 1100 1200 1300 1400 ; do
    echo $i
    for j in 1 2 3 4 5 6 7 8 9 0 ; do
	(time python mauer.py $i) 3>&1 1>&2 2>&3 | python timeconvert.py
    done
done