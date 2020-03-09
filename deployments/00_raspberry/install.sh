
sudo apt-get update -y
sudo apt-get upgrade -y

sudo apt-get install -y build-essential avahi-utils \
    libopenjp2-7-dev libffi-dev libffi-dev libssl-dev \
    libtiff5-dev gfortran libatlas-base-dev \
    libopenblas-dev libhdf5-serial-dev cdbs git ntp sshpass

sudo apt-get install -y python3 python3-dev \
    python3-pip python3-virtualenv \
    python3-numpy python3-pandas

sudo apt-get install -y i2c-tools python3-picamera python3-rpi.gpio