# Perform the Required Imports
from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result
from nornir_utils.plugins.tasks.files import write_file
import pathlib
import datetime

# Perform the Nornir Initialization
nr = InitNornir(config_file="config.yaml")

config_directory = "backups"
now = datetime.datetime.now().replace(microsecond=0)

# Create a Nornir Task
def backup_config(task):
    # Task 1. Run the NAPALM Config Getter to Collect the Config
    config_result = task.run(task=napalm_get, getters=["config"])

    # Task 2. Write the Device Config to a File using the Nornir, Write_File Task
    running_config = config_result.result["config"]["running"]
    pathlib.Path(config_directory).mkdir(exist_ok=True)
    task.run(task=write_file, content=running_config, filename=f"backups/{task.host}_{now}.txt")

# Run our backup_config task against all of our devices.
results = nr.run(task=backup_config)

# Finally, we print the results of running our task against all the devices.
print_result(results)
