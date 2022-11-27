from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_configure
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def accessvlan_test(task):
    task.run(task=napalm_configure, filename="accessvlan.txt", dry_run=True)

results = nr.run(task=accessvlan_test)
print_result(results)
