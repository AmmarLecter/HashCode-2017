#!/bin/bash

fs=*.in

for f in $fs; do
    echo $f
    out=$1_$f.out
    python main.py < $f > $out
done
