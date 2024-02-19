from nornir import InitNornir
from nornir_utils.plugins.functions import print_result, print_title
from nornir_netmiko import netmiko_send_command
from rich import print

nr = InitNornir(config_file="config.yaml")

# user should insert the specific mac address in the correct format, it can be inserted in partial format.
macaddress = input("write down your mac address here...")
print("                Vlan      MAC_Address     Age_Time(when exists)    Port")


# the function is going to find the mac address on all interfaces that it has been learnt and show "device name: vlan number, mac address, age time and configuration of interfaces” as a result.
def showmac(task):
   try:
   # getmac variable will store the result of "show mac address-table" command.
    getmac = task.run(task=netmiko_send_command, command_string=f"sh mac address-table | inc  {macaddress}")
    task.host["facts"] = getmac.result
    
    # devicemac variable will store the facts of getmac variable
    devicemac = task.host["facts"]

    # we will replace the unwanted sections of devicemac variable
    if devicemac != "":
     devicemac=devicemac.replace("dynamic","")
     devicemac=devicemac.replace("DYNAMIC","")
     devicemac=devicemac.replace("F","")
     devicemac=devicemac.replace("~~~","")
     devicemac=devicemac.replace(" ","-")

     # deviceint variable will store the related interfaces that have learnt the mac address.
     deviceint=devicemac[-10:]
     deviceint=deviceint.replace("-","")

     # getint variable will store the configuration of interfaces that have learnt the specific mac address that the user has been inserted.
     getint = task.run(task=netmiko_send_command, command_string=f"sh run int {deviceint}")
     task.host["facts"] = getint.result

     # intdescription variable will store the facts of getint variable.
     intdescription = task.host["facts"]
     if "Invalid" in intdescription:
        intdescription= "That is not physical interface"
     
     print(f"{task.host}: [green]{devicemac}")
     print(f"[blue]{intdescription}")
    else:
       print(f"{task.host}[red]:There is no MAC like this")
   except:
      print(f"{task.host}:[yellow]I can't connect")
   
results = nr.run(task=showmac)
