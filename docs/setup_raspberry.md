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
    scan_ssid=1
    psk="<your password>"
}
```

Save this file to the root of boot partition with the filename `/Volumes/boot/wpa_supplicant.conf`.

#### Step 3: Enable SSH for first boot

Put a file named **ssh** in the root of your **boot** partition.

```shell
touch /Volumes/boot/ssh
```

#### Step 4: Find your Raspberry Pi on the network

```shell
ping rasberrypi.local
```

### Boot the Raspberry and finalize the setup

#### Step 5: Connect to your Raspberry Pi

```shell
ssh pi@raspberrypi
```

Password is `raspberry` initially.

#### Step 6: Change the password

Once logged in, change the password for the `pi` user:

```shell
passwd
```

#### Step 7: Change the hostname

```shell
sudo vi /etc/hostname
```

#### Step 8: Config the Raspberry Pi hardware and other OS settings

```shell
sudo raspi-config
```
 
Enable HW interfaces

* Interfacing Options | ssh
* Interfacing Options | I2C
* Interfacing Options | Camera
* Interfacing Options | Remote GPIO
* Advanced Options | Exapand Filesystem

Choose and hit enter. Reboot.

#### Step 9: Create a key-pair

```shell
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

#### Step 10: Install your public key

Finally, install you public key to enable login without a password.

```shell
cat ~/.ssh/cloudpi_rsa.pub | ssh <USERNAME>@<IP-ADDRESS> 'mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys'
```