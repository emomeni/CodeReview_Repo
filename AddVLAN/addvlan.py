from nornir import InitNornir
from nornir_utils.plugins.functions import print_result, print_title
from nornir_netmiko import netmiko_send_command
from nornir_netmiko import netmiko_send_config
from rich import print
import sys
from nornir.core.filter import F 

nr = InitNornir(config_file="config.yaml")

try:
 choosenum = int(input("enter 1 for normal vlan and 2 for Community vlan and 0 for exit ...   "))
except:
  print('[red]write the right number, run the app again')
  quit()
if (choosenum == 0):
  quit()
  
elif(choosenum <=2):
  uservlan = input("Please enter your new vlan   ")
  desvlan= input("Please enter your description   ")

else:
    print('[red]write the right number, run the app again')
    quit()
def addvlanfp(task):
    normalcommands=[f"vlan {uservlan}", f"name {desvlan}","mode fabricpath","end"]
    communitycommands=[f"vlan {uservlan}", f"name {desvlan}","mode fabricpath","private-vlan community","end"]
    try:
      r = task.run(task=netmiko_send_command, command_string=f"sh vlan id {uservlan}")
      devreply=r.result
      if "Invalid" in devreply:
       print(f"[b]{task.host}:[red]Vlan is not in range")
       quit()
    except:
      print(f"[b]{task.host}:[red]No respond from device\n[yellow]****************************************************************************************")
      quit()
    if (desvlan not in devreply):
        try: 
          
           if (choosenum == 1) :
            task.run(task=netmiko_send_config,config_commands=normalcommands)
            print(f"[green][b]{task.host}: \nnormal vlan is configured\n[yellow]****************************************************************************************")
           elif (choosenum == 2) :
            task.run(task=netmiko_send_config,config_commands=communitycommands)
            print(f"[green][b]{task.host}:  \ncommunity vlan is configured\n[yellow]****************************************************************************************")
           x = task.run(task=netmiko_send_command, command_string=f"sh vlan id {uservlan}")
           devreply=x.result
           print(f"[b]{devreply}""\n[yellow]****************************************************************************************")
        except:
          print('[red]Couldnt add the vlan or description')
    else:
        print(f"[b]{task.host}:[red] The Vlan has been already defined")
    
    
def addvlance(task):
    normalcommands=[f"vlan {uservlan}", f"name {desvlan}","end"]
    communitycommands=[f"vlan {uservlan}", f"name {desvlan}","private-vlan community","end"]
    try:
      r = task.run(task=netmiko_send_command, command_string=f"sh vlan id {uservlan}")
      devreply=r.result
      if "Invalid" in devreply:
       print(f"[b]{task.host}:[red]Vlan is not in range")
       quit()
    except:
      print(f"[b]{task.host}:[red]No respond from device\n[yellow]****************************************************************************************")
      quit()
    if (desvlan not in devreply):
        try: 
          
           if (choosenum == 1) :
            task.run(task=netmiko_send_config,config_commands=normalcommands)
            print(f"[green][b]{task.host}: \nnormal vlan is configured\n[yellow]****************************************************************************************")
           elif (choosenum == 2) :
            task.run(task=netmiko_send_config,config_commands=communitycommands)
            print(f"[green][b]{task.host}:  \ncommunity vlan is configured\n[yellow]****************************************************************************************")
           x = task.run(task=netmiko_send_command, command_string=f"sh vlan id {uservlan}")
           devreply=x.result
           print(f"[b]{devreply}""\n[yellow]****************************************************************************************")
        except:
          print('[red]Couldnt add the vlan or description')
    else:
        print(f"[b]{task.host}:[red] The Vlan has been already defined")
        


# results = nr.run(task=addvlan)
nr_filter= nr.filter(F(has_parent_group="datacenter")&F(has_parent_group="nexus")&~F(has_parent_group="access"))
results= nr_filter.run(task=addvlanfp)

nr_filter= nr.filter(F(has_parent_group="datacenter")&F(has_parent_group="nexus")&F(has_parent_group="access"))
results= nr_filter.run(task=addvlance)
