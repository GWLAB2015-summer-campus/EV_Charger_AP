#!/bin/bash

sudo apt update
apt-get -y install build-essential git make autoconf automake libtool \
      pkg-config cmake ninja-build libasound2-dev libpulse-dev libaudio-dev \
      libjack-dev libsndio-dev libsamplerate0-dev libx11-dev libxext-dev \
      libxrandr-dev libxcursor-dev libxfixes-dev libxi-dev libxss-dev libwayland-dev \
      libxkbcommon-dev libdrm-dev libgbm-dev libgl1-mesa-dev libgles2-mesa-dev \
      libegl1-mesa-dev libdbus-1-dev libibus-1.0-dev libudev-dev fcitx-libs-dev

apt-get install xorg wget libxrender-dev lsb-release libraspberrypi-dev raspberrypi-kernel-headers

# If we're on Debian buster, we need to install cmake from backports as the cmake version
# in buster is too old to build sdl2
if [ "$(lsb_release -cs)" = "buster" ]; then \
    echo "deb http://deb.debian.org/debian buster-backports main" >> /etc/apt/sources.list; \
    apt-get update; \
    apt-get -y install -t buster-backports cmake; \
fi