from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config, netmiko_send_command
from nornir_utils.plugins.functions import print_result, print_title
from nornir_jinja2.plugins.tasks import template_file
from nornir.core.filter import F
from nornir_napalm.plugins.tasks import napalm_get
from nornir_napalm.plugins.tasks import napalm_configure
from nornir.core.task import Result
#from nornir.plugins.tasks import text
import os

nr = InitNornir(config_file="config.yaml")

#we define a group of tasks
def interfaces_config(task, vlans_to_find):
    #Find interesting interfaces to configure
    r1 = task.run(task=netmiko_send_command, command_string="show interfaces switchport", use_textfsm=True)
    interesting_interfaces = [ i['interface'] for i in r1.result if ((i['access_vlan'] in vlans_to_find) and (i['admin_mode'] == 'static access'))]
    print(interesting_interfaces)
    if interesting_interfaces:
        #Generate config for inventoried host
        r = task.run(task=template_file, template='interfaces_config.j2', path='templates', interface_list=interesting_interfaces)

        #Save config in a host variable
        task.host["intconfig"] = r.result

        #Deploy the interface configuration usin napalm
        task.run(task=napalm_configure, name="Loading config to device", replace=False, configuration=task.host["intconfig"])

res=nr.run(task=interfaces_config, vlans_to_find=['200',])
print_result(res)
