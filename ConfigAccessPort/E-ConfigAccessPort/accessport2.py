from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def config_test(task):
    task.run(task=netmiko_send_config, config_file="accessvlan.txt")

results = nr.run(task=config_test)
print_result(results)
