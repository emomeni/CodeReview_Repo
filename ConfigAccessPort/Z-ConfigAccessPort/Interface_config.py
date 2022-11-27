from nornir import InitNornir
from nornir_utils.plugins.functions import print_result,print_title
from nornir_netmiko import netmiko_send_config,netmiko_send_command

nr = InitNornir(config_file="config.yaml")

def lb_create(lb_task):
    lb_task.run(task=netmiko_send_config,config_file="Interface_config.txt")

result = nr.run(task=lb_create)

print_title("NETMIKO Interface Config")
print_result(result)
