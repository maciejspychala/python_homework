#!/bin/bash

array=($(ls *.wav))
for item in ${array[*]}
do
    python voice.py $item
done
