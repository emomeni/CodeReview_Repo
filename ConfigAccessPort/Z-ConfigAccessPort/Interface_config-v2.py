from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config
from nornir_utils.plugins.functions import print_title, print_result
from nornir_jinja2.plugins.tasks import template_file

nr = InitNornir(config_file="config.yaml")

def interfaces_config(task):
    var = task.run(task=template_file,
                   name="Switches interface configuration",
                   template="Interfaces.j2",
                   # current directory:
                   path="Templates")
    task.host["interfaces_config"] = var.result
    task.run(
    netmiko_send_config, 
    name="Loading Configuration on the device",
    config_commands=task.host["interfaces_config"].splitlines()
    )
def main():
    print_title("Config Switch Interfaces")
    task = nr.run(task=interfaces_config)
    print_result(task)

if __name__ == "__main__":
    main()
