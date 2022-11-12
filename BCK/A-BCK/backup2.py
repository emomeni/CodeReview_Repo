import sys
import time
import os
from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result
from rich import print as rprint

nr = InitNornir(config_file="config.yaml")

# create time string
srv_time = time.localtime() # get struct_time
time_string = time.strftime("%m-%d-%Y_%H-%M-%S", srv_time)
# print(time_string)


# check directory and create if not exist
for host in nr.inventory.hosts:
    if not os.path.exists(f"backup/{nr.inventory.hosts[host]}"):
        os.makedirs(f"backup/{nr.inventory.hosts[host]}")
        print(f'New directory {nr.inventory.hosts[host]} is created')


def get_bck_napalm(task):
    config=task.run(task=napalm_get, getters=["get_config"])
    dev_bck=(f'{config.result["get_config"]["running"]}')
#    devbck=rprint(config.result["get_config"]["running"])
    devicepath= (f'backup/{task.host["hname"]}')
    filename= (f'{devicepath}/{task.host["hname"]}_{time_string}.cfg')
#    print(filename)
    with open(filename, "a") as modify_back:
       modify_back.write(dev_bck)
    print(f'New backup file from {task.host["hname"]} is created')

results=nr.run(task=get_bck_napalm)
# print_result(results)




