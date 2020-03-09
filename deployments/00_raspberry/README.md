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

sudo apt-get install -y build-essential avahi-utils \
    libopenjp2-7-dev libffi-dev libffi-dev libssl-dev \
    libtiff5-dev gfortran libatlas-base-dev \
    libopenblas-dev libhdf5-serial-dev cdbs git ntp sshpass

sudo apt-get install -y python3 python3-dev \
    python3-pip python3-virtualenv \
    python3-numpy python3-pandas

sudo apt-get install -y i2c-tools python3-picamera python3-rpi.gpio
```

or

```shell

wget -O - https://raw.githubusercontent.com/mickuehl/cloudpi/master/deployments/00_raspberry/install.sh | bash

```
