# HRI Cacti :cactus:
Human Robot Interaction (HRI) Command and Control Teammate Interface (CACTI) for Extended Reality (XR) devices.

## Associated Repos
- [gesture_recognition](https://github.com/frank-Regal/gesture_recognition) - models & pkgs used to classify non-verbal gestures from XR head-mounted displays
- [speech_recognition](https://github.com/frank-Regal/speech_recognition) - models & pkgs used to classify verbal gestures from XR head-mounted displays
- [image_writer](https://github.com/frank-Regal/image_writer) - ROS package used to write sensor_msgs/Image to images for early data processing
- [speech_to_text_research](https://github.com/frank-Regal/speech_to_text_research) - speech to text development repo.

## Get Started

1. Install [ROS](https://www.ros.org/) and setup a catkin workspace
2. Clone repo into `catkin_ws/src` directory of catkin workspace
```
git clone git@github.com:frank-Regal/hri_cacti_xr.git
```
3. Install Dependencies
   
    a. [vcstool](https://github.com/dirk-thomas/vcstool)
   
    ```sudo apt install python3-vcstool```
   
    b. [robofleet_client](https://github.com/UTNuclearRobotics/robofleet_client/tree/iron-devel)

   ```cd catkin_ws/src```
   
   ```git clone --recursive git@github.com:UTNuclearRobotics/robofleet_client.git```

   ```cd hri_cacti_xr/robofleet/ && ./build_rf_pkgs.sh```
   

## Getting Started
3. Build packages required for running in realtime
4. Install robofleet to stream sensor data to your machine (optional)

## Contributing
6. Clone required repos to contribute and get started with development (optional)
```
cd hri_cacti_xr && vcs import < .repos
```


## Raw Bag Data
### Recording
To record raw sensor stream data from the hololens and bag it to your machine:
1. Ensure this repo is cloned and a robofleet client is setup in your workspace. See 
```

```

### Downloading
Raw bag data is saved in a [Google Drive Directory](https://drive.google.com/drive/folders/1F_q5MIJcItS98ip6DdXzI2j1rtw0_qrB?usp=sharing). To download the raw bags to your machine install ```gdown``` and then run the python scrip in ```bags``` directory.
1. Install [gdown](https://pypi.org/project/gdown/) dependency
```
pip3 install gdown
```
2. Download bag data using a python script placed in the ```bag``` directory. Use the ```--dir``` flag to define specific directories within [this](https://drive.google.com/drive/folders/1F_q5MIJcItS98ip6DdXzI2j1rtw0_qrB?usp=sharing) directory to download. Leave empty to download all directories.
```
cd bags && python3 get-data.py [--dir DIRECTORY_ONE DIRECTORY_TWO]
```
3. Play bags sequentially (to have [image_writer](https://github.com/frank-Regal/image_writer) write to video files).
```
cd bags && ./play-data.sh [DIRECTORY_TO_BAGS]
```
### Viewing
1. From a terminal open the saved RVIZ config file
```
cd bags && rviz -d image-viewer.rviz
```
2. From another terminal play the bag data. The four mono cameras from the HoloLens will be viewed.

