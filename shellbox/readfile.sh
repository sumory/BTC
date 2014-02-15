#!/bin/sh

IFS="
"

to_read_file=$1

while read -r line
do
    echo $line
    done < $to_read_file
