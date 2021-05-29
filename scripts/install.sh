#!/bin/bash

echo "-- Installing requirements"
echo " "
conda install psutil
conda install requests
conda install flask
conda install paho-mqtt
echo "-- Done"