#!/bin/bash

while :
do
ALIVE="$(ping -c 1 "$1" | grep "bytes from" | wc -l )"
  if [ $ALIVE -eq 1 ]
  then
    ssh $1
    sleep 10
  else
    echo "${1} is not reachable right now"
    sleep 180
  fi
done
