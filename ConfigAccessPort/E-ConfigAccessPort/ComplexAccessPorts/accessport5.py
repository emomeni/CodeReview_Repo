from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config
from nornir_netmiko.tasks import netmiko_send_command
from nornir_jinja2.plugins.tasks import template_file
from nornir_utils.plugins.functions import print_title, print_result

nr = InitNornir(config_file="config.yaml")

#def hostname_config(task):
#    var = task.run(task=template_file,
#                   name="Switches Hostname Configuration",
#                   template="hostnames.j2",
#                   # current directory
#                   path="templates")
#    task.host["hostname_config"] = var.result
#    task.run(
#        task=netmiko_send_config,
#        name="Configure Hostname on the Device",
#        config_commands=task.host["hostname_config"]
#    )

def interfaces_config(task):
    var = task.run(task=template_file,
                   name="Switches Interfaces Configuration",
                   template="interfaces.j2",
                   # current directory
                   path="templates")
    task.host["interfaces_config"] = var.result
    task.run(
        netmiko_send_config,
        name="Loading Configuration on the Device",
        config_commands=task.host["interfaces_config"].splitlines()
    )

def main():
    print_title("Let's Configure the Network")
    task = nr.run(task=interfaces_config)
    print_result(task)

if __name__ == "__main__":
    main()
