# Find a MAC Address in the Network
This code is going to find if a mac address exists on mac address table of devices and which ports have learnt it. When a user runs this code, it will take the mac address as an input and show the result.

## Description
This code uses "nornir_netmiko" library, also the rich library is used for rich text and beautiful formatting in the terminal.

A function called "showmac" contains two main variables "getmac" and "getint". getmac uses the "netmiko_send_command" module to send the "show mac address-table" command to the inventory for finding the mac address that we are searching for and stores the facts of it to the "devicemac" variable.

Since we need the configuration of interfaces that have learnt the mac address to show in the result, so we use the getint variable to send the "show run interface {name of interface}" command to retrieve the configuration and store it in intdescription variable.

The "showmac" function will take the mac address as input and show the result in below format:
* If the mac address is found, the result will be shown in green color in order of: “device name: VLAN number, mac address, age time and configuration of interfaces which have learnt it”.
* If the mac address is not found, the result will be shown in red color: “device name: There is no MAC like this”.
* If the connection to the device is not established, the result will be shown in yellow color: “device name: I can't connect".

Since the result of the "show mac address-table" command contains extra information which is not necessary to show as a result, in the "showmac" function, we use the "Replace" module to replace the extra sections with white spaces.

For Error Handling, we use the "try/except". We have placed the code that might generate an exception inside the try block. every try block is followed by an except block.

## Dependencies
* Prerequisites:
  - Ubuntu
  - Python3

## How to Run
to reach the final output, you need to follow the orders that will be mentioned in the following:

#### Clone Repo
   ```bash
    git clone https://github.com/emomeni/CodeReview_Repo/tree/main/ShowMAC
    cd ShowMAC
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
* To find the specific MAC Address, you need to run the **showmac.py**:
   ```bash
    python3 showmac.py
