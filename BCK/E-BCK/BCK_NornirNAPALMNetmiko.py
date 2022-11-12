# Perform the Required Imports:
# OS: used to help interact with the local environment and build the backup directory and file names for the configurations.
# InitNornir: object used to provide the configuration file containing system defaults.
# netmiko_send_command: netmiko function used to send arbitrary commands to networking devices.
# napalm_get: function to get facts from the device, here we will use to retreive the device configuration.
import os
from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_napalm.plugins.tasks import napalm_get
import datetime

# global variable, that is the directory name used to store the backed up files
BACKUP_DIR = "Backups/"

# global variable, that is used to store the time and date
TNOW = datetime.datetime.now().replace(microsecond=0)

# perform the Nornir initialization
nr = InitNornir(config_file="config.yaml")

# create a local directory, using the OS library to create a directory with name stored in the BACKUP_DIR variable
def create_backups_dir():
    if not os.path.exists(BACKUP_DIR):
        os.mkdir(BACKUP_DIR)

# create the backed up device configuration files inside the directory
# parameters (method, hostname, config) will get their data from the following functions.
def save_config_to_file(method, hostname, config):
    filename = f"{hostname}-{method}_{TNOW}.txt"
    with open(os.path.join(BACKUP_DIR, filename), "w") as f:
        f.write(config)

# will run the netmiko_send_command module to send a "show run" command
def get_netmiko_backups():
    backup_results = nr.run(
        task=netmiko_send_command,
        command_string="show run"
        )
    
    for hostname in backup_results:
        save_config_to_file(
            method="netmiko",
            hostname=hostname,
            config=backup_results[hostname][0].result,
        )

# will be built the same way, it will be using the napalm_get module to extract the device configuration
def get_napalm_backups():
    backup_results = nr.run(task=napalm_get, getters=["config"])

    for hostname in backup_results:
        config = backup_results[hostname][0].result["config"]["startup"]
        save_config_to_file(method="napalm", hostname=hostname, config=config)

# will execute all the functions and the code entry point is added to start the script when executed.
def main():
    create_backups_dir()
    get_netmiko_backups()
    get_napalm_backups()

if __name__ == "__main__":
    main()
