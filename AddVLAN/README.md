# Create a normal vlan or Community vlan on DC Switches
This program adds your switch a new vlan. It can be a normal or community vlan.
## Description
The program uses **"nornir_netmiko"** library. The program assumes that all primary vlans and below Ranges are set up on the swithes.
The program add the vlan in Fabricpath mode on leaf and spine switches and in CE mode on access switches. if a vlan is repititous, the program will warn you, if it has a new name the program adds the vlan with new name. 
### Dependencies
* prerequisites:
  - ubuntu
  - python3 

### Installing and Use:
* run the app and write the right number for normal vlan and community vlan, then write the vlan number and the name of vlan. It adds all the swithes and shows the configuration of vlan on the switch.
* Run the app
   ```bash
     python3 addvlan.py
* choose what you want
   ```bash
     enter 1 for normal vlan and 2 for Community vlan and 0 for exit ...   0 or 1 or 2
     Please enter your new vlan   XXX
     Please enter your description   XXX

