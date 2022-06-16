#!/bin/bash

if [ $# -eq 0 ]
  then
    echo "Usage: ./connect.sh <ip>"
    exit
fi

while :
do
ALIVE="$(ping -c 1 "$1" | grep "bytes from" | wc -l )"
  if [ $ALIVE -eq 1 ]
  then
    ssh $1
    sleep 10
  else
    echo "${1} not reachable right now"
    sleep 30
  fi
done
