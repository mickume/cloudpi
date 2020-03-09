
## Install

Copy all code to the RaspberryPi

```shell
scp drive.py vehicle.py requirements.txt pi@cloudpi<number>:/home/pi/
```

## Run the example

python src/remote_pilot.py -e a36ob0439j5iyd-ats.iot.eu-central-1.amazonaws.com -r certs/root-CA.crt -c certs/cloudpi00.cert.pem -k certs/cloudpi00.private.key




pip install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.12.0-py3-none-any.whl