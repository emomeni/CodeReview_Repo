import requests
import os
from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config, netmiko_send_command
from nornir_utils.plugins.functions import print_result, print_title
from nornir.core.task import Result
from nornir.core.exceptions import NornirExecutionError
from nornir_napalm.plugins.tasks import napalm_get, napalm_configure
from nornir.core.filter import F
import logging


nr = InitNornir(config_file="config.yaml")


def insert_vlan():
    try:
        host = input("Please enter switch name:")
        check_switch = nr.filter(platform="ios")
        if host in  check_switch.inventory.hosts:
            vlan = input("Please enter vlan number:")
            if vlan.isnumeric():
                port = input("Please enter the port number:Ethernet")
                x = nr.inventory.hosts[host].data["interfaces"]
                for entry in x:
                    if port == entry['port_slot']:
                       name= nr.inventory.hosts[host].hostname
                       res=nr.filter(hostname=name)
                       backup_results = res.run(
                            task=netmiko_send_config,
                            config_commands=['interface Ethernet' + port, "switchport mode access", 'switchport access vlan ' + vlan, "do wr"])
                       print_result(backup_results)
            else:
                print("The vlan number is not valid")
        else:
            print("Device not found")

    except NornirExecutionError:
        print("Nornir Error")

def main():
    insert_vlan()

if __name__ == "__main__":
    main()
