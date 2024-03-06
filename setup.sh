#!/bin/bash

HRI_CACTI_XR_DIR=$(pwd)

echo $HRI_CACTI_XR_DIR

echo " " >> ~/.bashrc
echo "# HRI Cacti XR Workspace Path" >> ~/.bashrc
echo "export HRI_CACTI_XR_PATH=$HRI_CACTI_XR_DIR" >> ~/.bashrc

$(source ~/.bashrc)

