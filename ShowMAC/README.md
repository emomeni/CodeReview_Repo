# Find a mac Address in the Network
This program searches a mac address in the network and finds all the ports that learn already the mac address.
## Description
The program uses **"nornir_netmiko"** library. It showes you the ports and the configuration of Physical ports that learn your given mac address.
if the progrm could'nt find the mac address or connect to the switch, lets you know with a message.
### Dependencies
* prerequisites:
  - ubuntu
  - python3 

### Installing and Use:
* Nothing to do , Just run the app and write apart or whole of your desired Mac address. The Program gives you what you want
   ```bash
     python3 showmac.py
