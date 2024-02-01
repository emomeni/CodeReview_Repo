# Find a MAC Address in the Network
This program searches for a MAC address in the network and finds all the ports that already learn the MAC address.
## Description
The program uses **"nornir_netmiko"** library. It shows you the ports and the configuration of Physical ports that learn your given MAC address.
if the program can't find the MAC address or connect to the switch, let you know with a message.
### Dependencies
* Prerequisites:
  - Ubuntu
  - python3 

### Installing and Use:
* Nothing to do, Just run the app and write apart or the whole of your desired MAC address. The Program gives you what you want
   ```bash
     python3 showmac.py
