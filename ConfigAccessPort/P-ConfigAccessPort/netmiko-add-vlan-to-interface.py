
import requests
import os
from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config
from nornir_utils.plugins.functions import print_result
from nornir.core.task import Result
from nornir.core.exceptions import NornirExecutionError
import logging


nr = InitNornir(config_file="config.yaml")


def insert_vlan():
    try:
        cisco_switch = nr.filter(platform="ios", hostname="192.168.15.202", type="ssh")
        if cisco_switch.inventory.hosts:
            print(f"{cisco_switch.inventory.hosts} reading configuration. Please wait...")
            backup_results = cisco_switch.run(
                task=netmiko_send_config,
                config_commands=["interface Ethernet0/2", "switchport mode access", "switchport access vlan 100", "do wr"])
            print_result(backup_results)
        for host in backup_results:
            if host not in backup_results.failed_hosts:
                print(backup_results[host][0].result)
        else:
            print("No device found!")
    except NornirExecutionError:
        print("Nornir Error")

def main():
    insert_vlan()

if __name__ == "__main__":
    main()

