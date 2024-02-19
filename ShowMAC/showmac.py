from nornir import InitNornir
from nornir_utils.plugins.functions import print_result, print_title
from nornir_netmiko import netmiko_send_command
from rich import print

nr = InitNornir(config_file="config.yaml")

# user will insert the specific mac address in the correct format, it can be inserted in partial format
macaddress = input("write down your mac address here...")
print("                Vlan      MAC_Address     Age_Time(when exists)    Port")


# the function that want to find the mac address on all ports that it has been learned
def showmac(task):
   try:
   # getmac variable will store the result of "show mac address-table" command
    getmac = task.run(task=netmiko_send_command, command_string=f"sh mac address-table | inc  {macaddress}")
    task.host["facts"] = getmac.result
    
    # devicemac variable will store the facts of getmac variable
    devicemac = task.host["facts"]

    # here we will replace the unwanted sections
    if devicemac != "":
     devicemac=devicemac.replace("dynamic","")
     devicemac=devicemac.replace("DYNAMIC","")
     devicemac=devicemac.replace("F","")
     devicemac=devicemac.replace("~~~","")
     devicemac=devicemac.replace(" ","-")

     # deviceint variable will store the related interfaces that has been learned the mac address
     deviceint=devicemac[-10:]
     deviceint=deviceint.replace("-","")

     # getint variable will store the interfaces' configurations that has learned the specific mac address that the user has been inserted
     getint = task.run(task=netmiko_send_command, command_string=f"sh run int {deviceint}")
     task.host["facts"] = getint.result

     # intdescription will store the facts of getint variable
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
