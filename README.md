# HRI Cacti :cactus:
Human Robot Interaction (HRI) Command and Control Teammate Interface (CACTI) for Extended Reality (XR) devices.

## Associated Repos
- [gesture_recognition](https://github.com/frank-Regal/gesture_recognition) - models & pkgs used to classify non-verbal gestures from XR head-mounted displays
- [speech_recognition](https://github.com/frank-Regal/speech_recognition) - models & pkgs used to classify verbal gestures from XR head-mounted displays
- [image_writer](https://github.com/frank-Regal/image_writer) - ROS package used to write sensor_msgs/Image to images for early data processing
- [speech_to_text_research](https://github.com/frank-Regal/speech_to_text_research) - speech to text development repo.

## Workspace Setup
1. Install [vcstool](https://github.com/dirk-thomas/vcstool) dependency
```
sudo apt install python3-vcstool
```
2. Clone this repo and associated repos
```
git clone git@github.com:frank-Regal/hri_cacti_xr.git
```
```
cd hri_cacti_xr && vcs import < .repos
```

## Raw Bag Data
### Clone
Raw bag data is saved in a [Google Drive Directory](https://drive.google.com/drive/folders/1F_q5MIJcItS98ip6DdXzI2j1rtw0_qrB?usp=sharing). To download the raw bags to your machine install ```gdown``` and then run the python scrip in ```bags``` directory.
1. Install [gdown](https://pypi.org/project/gdown/) dependency
```
pip3 install gdown
```
2. Download bag data using a python script placed in the ```bag``` directory. Use the ```--dir``` flag to define specific directories within [this](https://drive.google.com/drive/folders/1F_q5MIJcItS98ip6DdXzI2j1rtw0_qrB?usp=sharing) directory to download. Leave empty to download all directories.
```
cd bags && python3 get-data.py [--dir DIRECTORY_ONE DIRECTORY_TWO]
```
### View
1. From a terminal open the saved RVIZ config file
```
cd bags && rviz -d image-viewer.rviz
```
2. From another terminal play the bag data. The four mono cameras from the HoloLens will be viewed.

