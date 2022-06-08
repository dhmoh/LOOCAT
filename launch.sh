#!/bin/bash
echo "roscore start!"
cd ~/catkin_ws/src/byvision && 
gnome-terminal -- roscore & sleep 1

echo "detect node start!"
cd ~/catkin_ws/src/byvision/src/yolov5_detection &&
gnome-terminal -- rosrun byvision detect_main.py & sleep 18

echo "track node start!"
cd ~/catkin_ws/src/byvision/src && 
gnome-terminal -- rosrun byvision track_main.py 
