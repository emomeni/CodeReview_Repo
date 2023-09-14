import sys
import time
import os
from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result
from rich import print as rprint

nr = InitNornir(config_file="config.yaml")

# create time string for create file name the you can print time for testing 
srv_time = time.localtime() # get struct_time
time_string = time.strftime("%m-%d-%Y_%H-%M-%S", srv_time)
#print(time_string+"\r")


# check directory and create if not exist and you can print it if you want
for host in nr.inventory.hosts:
    if not os.path.exists(f"/home/backup/{nr.inventory.hosts[host]}"):
        os.makedirs(f"/home/backup/{nr.inventory.hosts[host]}")
        print(f'New directory {nr.inventory.hosts[host]} is created\r')

#create file for task's summary resault every day.
resultbckfile= (f'/home/backup/summaries/{time_string}_results.txt')
with open(resultbckfile,"a") as printresults:
    printresults.write(f"{time_string}: \n\n")

#read running config and save config and resaults
def get_bck_napalm(task):
    try:
        config=task.run(task=napalm_get, getters=["get_config"])
        dev_bck=(f'{config.result["get_config"]["running"]}')
        devicepath= (f'/home/backup/{task.host}')
        filename= (f'{devicepath}/{task.host}_{time_string}.cfg')
        with open(filename, "a") as modify_back:
           modify_back.write(dev_bck)
        checkfile=os.stat(filename)
        filesize=checkfile.st_size
        resultbckfile= (f'/home/backup/summaries/{time_string}_results.txt')
        with open(resultbckfile,"a") as printresults:
           printresults.write(f"{task.host} backup is created in this file: {devicepath}/{task.host}_{time_string}.cfg  (file size = {filesize})\n\n")
    except :
        resultbckfile= (f'/home/backup/summaries/{time_string}_results.txt')
        with open(resultbckfile,"a") as printresults:
           printresults.write(f"backup from '{task.host}' is not ok \n\n")

results=nr.run(task=get_bck_napalm)
#print_result(results)
