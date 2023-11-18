from nornir import InitNornir
from nornir_utils.plugins.functions import print_result, print_title
from nornir_netmiko import netmiko_send_command
from rich import print
import csv
import re
import os
import time

nr = InitNornir(config_file="config.yaml")

# creating the csv with the appropriate headers
with open('Show_Version_Output.csv', 'w', encoding='utf8', newline='') as csvfile:
    headers = ['Hostname', 'IP Address', 'Province', 'Device Role', 'Platform', 'OS Model', 'OS Version', 'Mobinnet', 'Irancell', 'Media Type', 'Connection Type']
    header = csv.DictWriter(csvfile, fieldnames=headers)
    header.writeheader()
    csvfile.close()

# indicates the Province name in csv
Province = input("Province Name? ")

# default value for Connection Type in csv
ConnectionType = 'SSH'

# time string that is used for logging output, e.g. 11-15-2023_09-15-46_results.txt
srv_time = time.localtime()
time_string = time.strftime("%m-%d-%Y_%H-%M-%S", srv_time)

# gathering device facts
def Device_Facts(task):
    try:
# "show version" section
        r = task.run(task=netmiko_send_command, command_string="show version", use_genie=True)
        task.host["facts"] = r.result
        DeviceHostFact = task.host["facts"]
        DeviceHost = task.host['facts']['version']['hostname']
        DeviceOSFact = task.host["facts"]
        DeviceOS = task.host['facts']['version']['os']
        DeviceVersionFact = task.host["facts"]
        DeviceVersion = task.host['facts']['version']['version_short']
        DevicePlatformFact = task.host["facts"]
        DevicePlatform = task.host['facts']['version']['platform']

# "show ip interface brief" section
        r = task.run(task=netmiko_send_command,command_string="show ip interface brief", use_genie=True)
        task.host["facts"] = r.result
        IntStatus = task.host['facts']['interface']
        MobinNet_SP = Irancell_SP = 'Null'
        MediaType = 'Ethernet'
        for keys, values in IntStatus.items():
            if  "Tunnel31" in keys or "Tunnel32" in keys:
                Irancell_SP = f"Irancell"
            if  "Tunnel41" in keys or "Tunnel42" in keys:
                MobinNet_SP = f"MobinNet"
            if "Serial" in keys:
                MediaType = f"Serial"

# extracting the IP Address from the hosts.yml
        IP = task.host.dict()
        IPAddress = IP['hostname']

# indicating the device role; branch or hq
        DeviceRole = 'Branch'
        if "192.168.15.2" in IPAddress:
            DeviceRole = f"HQ"

# appending the appropriate values to the csv that has been created before
        with open('Show_Version_Output.csv', 'a', encoding='utf8') as csvfile:
            writer = csv.writer(csvfile)
            csvdata = (DeviceHost, IPAddress, Province, DeviceRole, DevicePlatform, DeviceOS, DeviceVersion, MobinNet_SP, Irancell_SP, MediaType, ConnectionType)
            writer.writerow(csvdata)
            csvfile.close()

# check that the connection has been established or not
        check_connection= (f'/home/network-ent/Ehsan_Codes/{time_string}_results.txt')
        with open(check_connection,"a") as wr_status_summary:
            wr_status_summary.write(f"{task.host} Is OK \n\n")

    except:
        check_connection= (f'/home/network-ent/Ehsan_Codes/{time_string}_results.txt')
        with open(check_connection,"a") as wr_status_summary:
            wr_status_summary.write(f"{task.host} Is Not OK \n\n")

# results
results = nr.run(task=Device_Facts)
