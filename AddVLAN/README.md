# Create a normal VLAN or Community VLAN on DC Switches
This program adds a new VLAN to your switch. It can be a normal or community VLAN.
## Description
The program uses **"nornir_netmiko"** library. The program assumes all primary VLANs and below Ranges are set up on the switches.
The program adds the VLAN in Fabricpath mode on leaf and spine switches and in CE mode on access switches. if a VLAN is repetitious, the program will warn you, if it has a new name the program adds the VLAN with a new name. 
### Dependencies
* Prerequisites:
  - Ubuntu
  - python3 

### Installing and Use:
* run the app and write the right number for the normal VLAN and community VLAN, then write the VLAN number and the name of the VLAN. It adds all the switches and shows the VLAN configuration on the switch.
* Run the app
   ```bash
     python3 addvlan.py
* choose what you want
   ```bash
     enter 1 for normal VLAN, and 2 for Community VLAN and 0 for exit ...   0 or 1 or 2
     Please enter your new VLAN   XXX
     Please enter your description   XXX

