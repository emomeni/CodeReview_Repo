import requests
import os
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
    try:
        if type == "ssh":
            with open(os.path.join(BACKUP_DIR, filename), "w", encoding="utf-8") as f:
                f.write(config)
            print(f"{hostname} >>> backup file was created successfully!")
            f.close()
        elif type == "http":
            with open(os.path.join(BACKUP_DIR, filename), "wb") as f:
                f.write(config.content)
            print(f"{hostname} >>> backup file was created successfully!")
            f.close()
        else:
            print("Host type is unknown!")
    except FileNotFoundError as werror:
        print(werror)

    
def get_fortinet_backups() -> Result:
    print("**************************** Fortinet_HTTP ****************************")
    try:
        fortinet_http = nr.filter(platform="fortinet", type="http")
        if fortinet_http.inventory.hosts:
            for host in fortinet_http.inventory.hosts:
                print(host)
                hostname = fortinet_http.inventory.hosts[host].hostname
                port = fortinet_http.inventory.hosts[host].port
                access_token = fortinet_http.inventory.hosts[host].password
                requests.packages.urllib3.disable_warnings()
                apiUrl = f"http://{hostname}:{port}/api/v2/monitor/system/config/backup?scope=global&access_token={access_token}"
                payload = {}
                data = requests.request("GET", apiUrl, verify=False, data=payload)
                save_config_to_file(type="http", hostname=host, config=data)
        else:
            print("No device found!")
    except NornirExecutionError:
        print("Nornir Error")
    except requests.exceptions.RequestException as httpGetError:
        raise SystemExit(httpGetError)


def get_fortinet_ssh_backup() -> Result:
    print("**************************** Fortinet_SSH ****************************")
    try:
        fortinet_ssh = nr.filter(platform="fortinet", type="ssh")
        if fortinet_ssh.inventory.hosts:
            print(f"{fortinet_ssh.inventory.hosts} reading configuration. Please wait...")
            backup_results = fortinet_ssh.run(
                task=netmiko_send_command,
                command_string="show", severity_level=logging.DEBUG)
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
    get_fortinet_backups()
    get_fortinet_ssh_backup()
