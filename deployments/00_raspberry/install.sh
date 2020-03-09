# standard updates
sudo apt-get update -y
sudo apt-get upgrade -y

# helpful libraries and stuff
sudo apt-get install -y build-essential cmake pkg-config cdbs ntp sshpass git \
    python3 python3-dev python3-pip python3-virtualenv python3-wheel

sudo apt-get install -y avahi-utils \
    libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev \
    libopenjp2-7-dev libffi-dev libffi-dev libssl-dev \
    libavcodec-dev libavformat-dev libswscale-dev libv4l-dev \
    libtiff5-dev gfortran libatlas-base-dev \
    libxvidcore-dev libx264-dev libatlas-base-dev \
    libzmq-dev xsel xclip python3-h5py \
    libopenblas-dev libhdf5-serial-dev

# Raspberry Pi hardware support
sudo apt-get install -y i2c-tools python3-picamera python3-rpi.gpio

# remove python2
sudo apt-get remove python2.7 -y
sudo apt-get autoremove -y

# create a python virtualenv
sudo apt install virtualenv -y
virtualenv ~/venv --system-site-packages --python python3
echo '#start venv' >> ~/.bashrc
echo 'source ~/venv/bin/activate' >> ~/.bashrc
source ~/venv/bin/activate

# make sure the virtual environment is active
source ~/venv/bin/activate
