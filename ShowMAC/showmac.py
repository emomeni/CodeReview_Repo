from nornir import InitNornir
from nornir_utils.plugins.functions import print_result, print_title
from nornir_netmiko import netmiko_send_command
from rich import print

nr = InitNornir(config_file="config.yaml")
macaddress = input("write down your mac address here...")
print("                Vlan      MAC_Address     Age_Time(when exists)    Port")


def showmac(task):
   try:
    r = task.run(task=netmiko_send_command, command_string=f"sh mac address-table | inc  {macaddress}")
    task.host["facts"] = r.result
    Devicemac = task.host["facts"]
    if Devicemac != "":
     Devicemac=Devicemac.replace("dynamic","")
     Devicemac=Devicemac.replace("DYNAMIC","")
     Devicemac=Devicemac.replace("F","")
     Devicemac=Devicemac.replace("~~~","")
     Devicemac=Devicemac.replace(" ","-")
     Deviceint=Devicemac[-10:]
     Deviceint=Deviceint.replace("-","")
     r = task.run(task=netmiko_send_command, command_string=f"sh run int {Deviceint}")
     task.host["facts"] = r.result
     intdescription = task.host["facts"]
     if "Invalid" in intdescription:
        intdescription= "That is not physical interface"
     
     
     print(f"{task.host}: [green]{Devicemac}")
     print(f"[blue]{intdescription}")
    else:
       print(f"{task.host}[red]:There is no MAC like this")
   except:
      print(f"{task.host}:[yellow]I can't connect")
   
results = nr.run(task=showmac)
