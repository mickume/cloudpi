# Install software

## Setup the Raspberry Pi

### Preapre the boot disk

```shell
diskutil list

diskutil unmountDisk /dev/disk2

sudo diskutil eraseDisk FAT32 FOO MBRFormat /dev/disk2

sudo dd bs=1m if=2019-09-26-raspbian-buster-lite.img of=/dev/disk2 conv=sync

diskutil unmountDisk /dev/disk2
```

### Setup Wifi for first boot

```shell
country=DE
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="<your network name>"
    psk="<your password>"
}
```

Save this file to the root of boot partition with the filename `wpa_supplicant.conf`.

### Enable SSH for first boot

Put a file named **ssh** in the root of your **boot** partition.

### Find your Raspberry Pi on the network

```shell
ping rasberrypi.local
```

### Connect to your Raspberry Pi

```shell
ssh pi@raspberrypi
```

### Update the boot image

```shell
sudo apt-get update
sudo apt-get upgrade
```

### Config the Raspberry Pi

```shell
sudo raspi-config
```

Change the following:

* change default password for pi
* change hostname
* enable Interfacing Options | I2C
* enable Interfacing Options | Camera
* Advanced Options | Exapand Filesystem

Choose and hit enter. Reboot.

### Install dependencies

```shell
sudo apt-get install -y build-essential i2c-tools avahi-utils joystick libopenjp2-7-dev \
  libtiff5-dev gfortran libatlas-base-dev libopenblas-dev libhdf5-serial-dev git ntp \
  python3 python3-dev python3-pip python3-virtualenv \
  python3-numpy python3-picamera python3-pandas python3-rpi.gpio \
  libffi-dev libffi-dev sense-hat
```

### Setup virtual env

```shell
python3 -m virtualenv -p python3 env --system-site-packages
echo "source env/bin/activate" >> ~/.bashrc
source ~/.bashrc
```

### Install python libs

```shell
sudo pip3 install astro-pi
sudo pip3 install paho-mqtt
sudo pip3 install cryptography
sudo pip3 install pyjwt
```

### 