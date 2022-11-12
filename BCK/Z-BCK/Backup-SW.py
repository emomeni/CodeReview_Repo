import requests
import os
import pathlib
import datetime
from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command 
from nornir_paramiko.plugins.tasks import paramiko_sftp
from nornir_utils.plugins.functions import print_result 
from nornir.core.task import Result
from nornir.core.exceptions import NornirExecutionError
import logging


def save_config_to_file(type, hostname, config):
    filename = f"{hostname}_{dateTime}.cfg" 
    config_dir = "Device-Backups"
    BACKUP_DIR = config_dir + "/" + str(hostname)
    pathlib.Path(config_dir).mkdir(exist_ok=True)
    pathlib.Path(BACKUP_DIR).mkdir(exist_ok=True)
    try:
        if type == "ssh":
            with open(os.path.join(BACKUP_DIR, filename), "w", encoding="utf-8") as f:
                f.write(config)
            print(f"{hostname} >>> backup file was created successfully!")
            f.close()
        else:
            print("Host type is unknown!")
    except FileNotFoundError as werror:
        print(werror)

def get_cisco_switch_backup() -> Result:
    print("**************************** Cisco_SW_SSH ****************************")
    try:
        cisco_sw = nr.filter(type="ssh")
        if cisco_sw.inventory.hosts:
            print(f"{cisco_sw.inventory.hosts} reading configuration. Please wait...")
            backup_results = cisco_sw.run(
                task=netmiko_send_command,
                command_string="show running-config", severity_level=logging.DEBUG)
            print_result(backup_results)
            for host in backup_results:
                if host not in backup_results.failed_hosts:
                    save_config_to_file(
                        type="ssh",
                        hostname=host,
                        config=backup_results[host][0].result,)
        else:
            print("No device found!")
    except NornirExecutionError:
        print("Nornir Error")


if __name__ == "__main__":
    nr = InitNornir('config.yaml')
    BACKUP_DIR = "."
    dateTime = datetime.datetime.today().strftime('%Y_%m_%d_%H_%M')
    get_cisco_switch_backup()
