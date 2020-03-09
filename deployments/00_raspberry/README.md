# Update the Raspberry Pis

Run the following Ansible playbook to update & upgrade the PIs:

```shell
ansible-playbook -i inventory/inventory playbooks/first_install.yaml
```

## Upgarde in a shell

Run the following from the Raspi:

```shell

sudo apt-get update -y
sudo apt-get upgrade -y

sudo apt-get install -y build-essential cmake pkg-config cdbs ntp sshpass git \
    python3 python3-dev python3-pip python3-virtualenv python3-wheel \
    python3-numpy python3-pandas

sudo apt-get install -y avahi-utils \
    libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev \
    libopenjp2-7-dev libffi-dev libffi-dev libssl-dev \
    libavcodec-dev libavformat-dev libswscale-dev libv4l-dev \
    libtiff5-dev gfortran libatlas-base-dev \
    libxvidcore-dev libx264-dev libatlas-base-dev \
    libzmq-dev xsel xclip python3-h5py \
    libopenblas-dev libhdf5-serial-dev

sudo apt-get install -y i2c-tools python3-picamera python3-rpi.gpio

sudo apt-get remove python2.7 -y
sudo apt-get autoremove -y

#create a python virtualenv
sudo apt install virtualenv -y
virtualenv ~/env --system-site-packages --python python3
echo '#start env' >> ~/.bashrc
echo 'source ~/env/bin/activate' >> ~/.bashrc
source ~/env/bin/activate

#make sure the virtual environment is active
source ~/env/bin/activate

```

or

```shell

wget -O - https://raw.githubusercontent.com/mickuehl/cloudpi/master/deployments/00_raspberry/install.sh | bash

```