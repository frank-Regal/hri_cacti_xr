#!/bin/bash

# Loop through all .avi files that contain 'lh_'
for file in *stop*.avi; do
    # Check if the file name actually contains 'lh_'
    if [[ $file == *"stop"* ]]; then
        # Construct new file name by removing 'lh_'
        newname="${file//lh_/}"
        # Rename the file
        mv "$file" "$newname"
        echo "Renamed $file to $newname"
    fi
done

