FROM ubuntu:20.04

SHELL ["/bin/bash", "-c"]

# install many dependencies and convenience packages with the apt package manager
RUN apt update && apt upgrade -y && apt install -y \
    sudo build-essential clang cmake git x11-apps\
    cmake-curses-gui cmake-qt-gui \
    dotnet-sdk-7.0 \
    wget apt-utils curl \
    nano vim tmux \
    libx11-dev libxrandr-dev libxinerama-dev libxcursor-dev libxi-dev \
    libboost-all-dev \
    libtbb-dev \
    libssl-dev \
    libzmq3-dev \
    libjemalloc-dev \
    doxygen \
    pkg-config \
    python3 \
    python3-pip \
    python3-setuptools \
    python3-wheel \
    apt-utils \
    python3-catkin-tools \
    python-is-python3 \
    libqt5websockets5-dev \
    qt5-default

# install ros packages
# see ../docs/installing_ros_packages.md for alternatives
RUN DEBIAN_FRONTEND=noninteractive apt install -y \
    ros-${ROS_DISTRO}-rviz \
    && rm -rf /var/lib/apt/lists/*

RUN rosdep update

# switch to home dir
WORKDIR /root

# setup a package from github
RUN git clone https://github.com/frank-Regal/hri_cacti_xr # where does this get installed?
# RUN source /opt/ros/${ROS_DISTRO}/setup.bash \
#     && cd amrl_msgs \
#     && export ROS_PACKAGE_PATH=`pwd`:$ROS_PACKAGE_PATH \
#     && make -j

SHELL ["/bin/bash", "-l", "-c"]

# copy the entrypoint into the image
COPY ./entrypoint.sh /entrypoint.sh

# run this script on startup
ENTRYPOINT /entrypoint.sh
