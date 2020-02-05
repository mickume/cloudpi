## Setup the Raspberry Pi

### Prepare the boot disk

#### Step 1: Create a bootable image

```shell
diskutil list

diskutil unmountDisk /dev/disk2

sudo diskutil eraseDisk FAT32 FOO MBRFormat /dev/disk2

sudo dd bs=1m if=2019-09-26-raspbian-buster-lite.img of=/dev/disk2 conv=sync

diskutil unmountDisk /dev/disk2
```

#### Step 2: Setup Wifi for first boot (verify this !)

```shell
country=DE
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="<your network name>"
    psk="<your password>"
}
```

Save this file to the root of boot partition with the filename `/boot/wpa_supplicant.conf`.

#### Step 3: Enable SSH for first boot

Put a file named **ssh** in the root of your **boot** partition.

```shell
touch /boot/ssh
```


#### Step 4: Find your Raspberry Pi on the network

```shell
ping rasberrypi.local
```

#### Step 5: Connect to your Raspberry Pi

```shell
ssh pi@raspberrypi
```

Password is `raspberry` initially.

#### Step 6: Update the boot image

```shell
sudo apt-get update
sudo apt-get upgrade
```

#### Step 7: Config the Raspberry Pi

```shell
sudo raspi-config
```
 
Change the following:

* change the default password for pi
* change the hostname

Enable

* Interfacing Options | ssh
* Interfacing Options | I2C
* Interfacing Options | Camera
* Advanced Options | Exapand Filesystem

Choose and hit enter. Reboot.

### Install basic dependencies

```shell
sudo apt-get install -y build-essential i2c-tools avahi-utils joystick libopenjp2-7-dev \
  libtiff5-dev gfortran libatlas-base-dev libopenblas-dev libhdf5-serial-dev git ntp \
  python3 python3-dev python3-pip python3-virtualenv \
  python3-numpy python3-picamera python3-pandas python3-rpi.gpio \
  libffi-dev libffi-dev sense-hat
```

### Setup a python virtual env

```shell
python3 -m virtualenv -p python3 venv --system-site-packages
echo "source venv/bin/activate" >> ~/.bashrc
source ~/.bashrc
```
