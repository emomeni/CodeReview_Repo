from nornir_utils.plugins.functions import print_result
from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config 
from nornir_utils.plugins.functions import print_result 
from nornir.core.task import Result
from nornir.core.exceptions import NornirExecutionError
import os
from nornir_netmiko.tasks import netmiko_send_config


nr = InitNornir(config_file="config.yaml")

host_name = input("Enter HostName:")
print("Hostname is: " + host_name)

inter_face = input("Enter Interface:")
print("Interface is: " + inter_face)

vlan_num = input("Enter Vlan Number:")
print("VLAN is: " + vlan_num)

command = (f"you want to config {host_name}:\n  interface {inter_face}\n    switchport mode access\n    switchport access vlan {vlan_num}\n    no sh ")
print (command)
mycommand= (f"interface {inter_face}\nswitchport mode access\nswitchport access vlan {vlan_num}\nno sh ")


filenamecfg= (f'{host_name}.cfg')
#    print(filename)
with open(filenamecfg, "w") as modify_back:
    modify_back.write(mycommand)

def config_switch():
    try:
        select_switch = nr.filter(hname=host_name)
        if select_switch.inventory.hosts:
#            print(f"{select_switch.inventory.hosts} reading configuration. Please wait...")
            configport = select_switch.run(
                task=netmiko_send_config,
                config_file=f"{filenamecfg}")
            print_result(configport)
#        for host in configport:
#            if host not in backup_results.failed_hosts:
#                print(backup_results[host][0].result)
        else:
            print("No device found!")
    except NornirExecutionError:
        print("Nornir Error")

def main():
    config_switch()

if __name__ == "__main__":
    main()


