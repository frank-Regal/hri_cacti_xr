#!/bin/bash

# Check if an argument was provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 /path/to/bag/files"
    exit 1
fi

# Directory containing the bag files
BAG_DIR="$1"

# Loop through each .bag file in the directory
for BAG_FILE in "$BAG_DIR"/*.bag
do
    echo "Playing $BAG_FILE"
    rosbag play "$BAG_FILE"
    echo "$BAG_FILE playback finished"
done

echo "All bag files have been played."

