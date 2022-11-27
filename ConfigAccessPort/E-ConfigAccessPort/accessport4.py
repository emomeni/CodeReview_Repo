from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_configure
from nornir_utils.plugins.functions import print_result
from tqdm import tqdm

nr = InitNornir(config_file="config.yaml")

def accessvlan_test(task, progress_bar):
    task.run(task=napalm_configure, filename="accessvlan.txt", dry_run=False)
    progress_bar.update()

with tqdm(total=len(nr.inventory.hosts)) as progress_bar:
    results = nr.run(task=accessvlan_test, progress_bar=progress_bar)

print_result(results)
