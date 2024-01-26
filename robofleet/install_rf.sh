#! /bin/bash

# clone the correct version of robofleet_client
vcs import < .repos

# move robofleet_client to src directory
mv robofleet_client ./../../

# cd into src directory
cd ../../..

# build robofleet_client
catkin build robofleet_client