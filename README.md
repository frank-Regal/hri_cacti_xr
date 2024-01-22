# HRI Cacti :cactus:
Human Robot Interaction (HRI) Command and Control Teammate Interface (CACTI) for Extended Reality (XR) devices.

## Associated Repos
- [gesture_recognition](https://github.com/frank-Regal/gesture_recognition) - models & pkgs used to classify non-verbal gestures from XR head-mounted displays
- [speech_recognition](https://github.com/frank-Regal/speech_recognition) - models & pkgs used to classify verbal gestures from XR head-mounted displays
- [image_writer](https://github.com/frank-Regal/image_writer) - ROS package used to write sensor_msgs/Image to images for early data processing
- [speech_to_text_research](https://github.com/frank-Regal/speech_to_text_research) - speech to text development repo.

## Getting Started
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
