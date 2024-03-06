# HRI Cacti :cactus:
Human Robot Interaction (HRI) Command and Control Teammate Interface (CACTI) for Extended Reality (XR) devices.

## Table of Contents
   * [1. Installation](#1-installation)
   * [2. Contributing](#2-contributing)
   * [3. Associated Packages](#3-associated-packages)


## 1. Installation

1. Install [ROS](https://www.ros.org/) & Create a Catkin Workspace
2. Clone Into `catkin_ws/src`
   ```shell
   git clone git@github.com:frank-Regal/hri_cacti_xr.git
   ```
3. Install Dependencies
    <details>
    <summary><a href="https://github.com/dirk-thomas/vcstool">vcstool</a></summary>
    <br>
       
    ```shell
    sudo apt install python3-vcstool
    ```
    </details>
    <details>
    <summary><a href="https://github.com/UTNuclearRobotics/robofleet_client/tree/iron-devel">robofleet_client</a></summary>
    <br>
    a. Change to src directory
       
    ```shell
    cd catkin_ws/src
    ```

    b. Clone robofleet_client recursively
    ```shell
    git clone git@github.com:UTNuclearRobotics/robofleet_client.git
    cd robofleet_client
    git submodule init
    git submodule update
    ```
    c. Build & source your catkin workspace

    ```shell
    catkin build robofleet_client
    ```
    ```shell
    source devel/setup.bash
    ```

    d. Use the bash script in this repo to create required robofleet message types.
    ```shell
    cd hri_cacti_xr/robofleet/ && ./build_rf_pkgs.sh
    ```
    
    e. Build & source your catkin workspace
    ```shell
    caktin build
    ```
    ```shell
    source devel/setup.bash
    ```
    </details>

4. Clone [Associated Packages](#associatedpackages) required for realtime classification of commands and development purposes.
   ```shell
   cd hri_cacti_xr && vcs import < .repos
   ```


## 2. Contributing
### 2-A. Downloading Bags & Raw Data
> **Info:** Raw bag data is saved in a public [Google Drive Directory](https://drive.google.com/drive/folders/1F_q5MIJcItS98ip6DdXzI2j1rtw0_qrB?usp=sharing). To download the raw bags to your machine install ```gdown``` and then run the python script provided in ```hri_cacti_xr/bags``` directory.
1. Install [gdown](https://pypi.org/project/gdown/) dependency.
   ```shell
   pip3 install gdown
   ```
2. Download bag data using a python script placed in the ```bag``` directory. Use the ```--dir``` flag to define specific directories within [this](https://drive.google.com/drive/folders/1F_q5MIJcItS98ip6DdXzI2j1rtw0_qrB?usp=sharing) directory to download. Leave empty to download all directories.
   ```shell
   # change into bag directory
   cd hri_cacti_xr/bags

   # run script to download bags
   python3 .get-bags.py [--dir DIRECTORY_ONE DIRECTORY_TWO]
   ```
3. Extract contents of the downloaded files
   ```shell
   # for example
   cd hri_cacti_xr/bags/stop

   # extract
   tar -xzvf 30x_stop_4mono_mic_10hz.tar.gz
   ``` 
4. (Optional) Write bags to ```.avi``` video files.
   1. Run launch files from [image_writer](https://github.com/frank-Regal/image_writer). See the repo for instructions.
   2. Play bags sequentially.
      ```shell
       # change directory into bags
       cd hri_cacti_xr/bags

       # play continuously
       ./.play-data.sh [DIRECTORY_TO_BAGS]
       ```

### 2-B. Recording HoloLens Sensor Stream Data
> **Info:** To record raw sensor stream data from the hololens and bag it to your machine follow the steps below. You must have a robofleet_server running already that the hololens and your local machine can connect to.

#### Local Machine
1. Ensure [robofleet_client](https://github.com/UTNuclearRobotics/robofleet_client/tree/iron-devel) was installed and configured with the instructions provided in the [Installation](#1-installation) section above.
2. Connect to the same network as the HoloLens and configure the `host_url:` variable in `hri_cacti_xr/robofleet/hl-ss-config.yaml` with the IP address of the [robotfleet_server](https://github.com/ut-amrl/robofleet_server/tree/master)
3. Start a `roscore`
4. Run robofleet_client with provided config file
   ```shell
   rosrun robofleet_client client robofleet/hl-ss-config.yaml
   ```
5. Record bag data to the `hri_cacti_xr/bags/<command_name>` directory
   ```shell
   rosbag record -o <command_name> -a
   ```
#### Headset
1. Ensure you have uploaded the lastest application from `hri_cacti_xr/apps` for the respective device.
2. Open the application
3. When you say the words **"Hey Robot"** the HoloLens will record and send 10 seconds worth of data.

### 2-C. Viewing Bagged Data
> **Info:** We have created a specific RVIZ configuration to view all four VLC camera streams nicely.
1. From a terminal open the saved RVIZ config file. Run the following command from the ```hri_cacti_xr/bags``` directory.
   ```shell
   rviz -d .image-viewer.rviz
   ```
2. From another terminal play the bag data. The four mono cameras from the HoloLens will be viewed.
   
## 3. Associated Packages
- [gesture_recognition](https://github.com/frank-Regal/gesture_recognition) - models & pkgs used to classify non-verbal gestures from XR head-mounted displays
- [speech_recognition](https://github.com/frank-Regal/speech_recognition) - models & pkgs used to classify verbal gestures from XR head-mounted displays
- [image_writer](https://github.com/frank-Regal/image_writer) - ROS package used to write sensor_msgs/Image to images for early data processing
- [speech_to_text_research](https://github.com/frank-Regal/speech_to_text_research) - speech to text development repo.
