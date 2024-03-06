#! /bin/bash
echo "Setting Up Robofleet Packages ..."

# setup
CUR_DIR=$(pwd)
RF_PKG_FILE="rf_pkgs.txt"
RF_PKG_BUILD_FILE=".rf_build_pkgs.txt"

# append _robofleet to caktin build only those files
cp "$RF_PKG_FILE" "$RF_PKG_BUILD_FILE"
sed -i 's/$/_robofleet/' "$RF_PKG_BUILD_FILE"

# cd into current ws src dir
cd $ROSLISP_PACKAGE_DIRECTORIES
if [ -z "$ROSLISP_PACKAGE_DIRECTORIES" ]; then
    echo "Error: Local ROS Workspace is not sourced! Source and try again."
    exit 1
fi
cd ../../../src/
SRC_DIR=$(pwd)

# generate and build
rm -rf robofleet_pkgs
rosrun robofleet_client generate_plugin_pkg.py -o $SRC_DIR/robofleet_pkgs -w $(cat $CUR_DIR/$RF_PKG_FILE)
cd ..
catkin build $(cat $CUR_DIR/$RF_PKG_BUILD_FILE)

# clean up
cd $CUR_DIR
rm $RF_PKG_BUILD_FILE
