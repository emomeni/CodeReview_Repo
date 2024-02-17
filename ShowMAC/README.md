# Find a MAC Address in the Network
This Code will search for a MAC address in the network and find all the ports that already learn the MAC address.

## Description
The program uses **"nornir_netmiko"** library. It shows you the ports and the configuration of Physical ports that learn your given MAC address.
if the program can't find the MAC address or connect to the switch, it will let you know with a message.

### Dependencies
* Prerequisites:
  - Ubuntu
  - Python3

### How to Run
to reach the final output, you need to follow the orders that will be mentioned in the following:

#### Clone Repo
   ```bash
    git clone https://github.com/emomeni/CodeReview_Repo/blob/main/ShowMAC/showmac.py
    cd showmac
```
#### Create venv
   ```bash
    python3 -m venv venv
```
#### Activate venv
   ```bash
    source venv/bin/activate
```
#### Install Requirements
   ```bash
    pip3 install -r requirements.txt
```
#### Run the Code!
* for finding the specific MAC Address, you need to run the **showmac.py**:
   ```bash
    python3 showmac.py
