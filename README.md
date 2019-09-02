# EXO-Server


## Requirments
1. Ubuntu 16.04+
2. Python 2.7

## Modulas needed 
1. numpy: ```pip install numpy```
2. Matplotlib: ```pip install matplotlib```
3. PySerial: ```pip install pyserial```
4. PyQt5 ```sudo apt install python-pyqt5```
5. pyyaml: ```pip install pyyaml```


## setup

```
git clone http://nagoldfarb@fischerlab2.wpi.edu:7990/scm/exo/exoserver.git
cd exoserver
git submodule init
git submodule update
```

## Quick Start

1. Connect the device to the computer
2. From the root of the exoserver folder: ```python Main/Starting_GUI.py```
3. If you want to create a subject
    - enter subject information in the text boxes
    - if you do not all data will be saved with a blank subject name
4. Enter the port ID (example: /dev/ttyACM0)
5. Hit **Connect to Exo** to connect to the exoskeleton
6. To view the sensors hit **open monitor**
7. It you want to record data hit **Start Session**
    - This will generate a yaml file with subject information
8. To start recording hit **Record**
    - This will start recording data into a CSV file
9. To stop recording  hit **Stop**
    - This will stop the recording
    - Update the yaml file with trial information
    - open up a text box to write notes, they will be saved into a txt file
