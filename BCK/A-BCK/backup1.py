import sys
import os
from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result
from rich import print as rprint

nr = InitNornir(config_file="config.yaml")

# check directory and create if not exist
for host in nr.inventory.hosts:
    if not os.path.exists(f"{nr.inventory.hosts[host]}"):
        os.makedirs(f"{nr.inventory.hosts[host]}")


def napalm_get_example(task):
    config=task.run(task=napalm_get, getters=["get_config"])
    rprint(config.result["get_config"]["running"])
    


results=nr.run(task=napalm_get_example)




