# ths is open book test model 1

fopen=open("running-config.cfg",'r')
fopen=fopen.read()
fopen=fopen.split("\n")
final_list = []
interface_list = []

intdict = dict()

def list_ifname_ip():

  for v in fopen:
    if "ip address" in v:
      v=v.split()
      interface_list.append(v)
      print(interface_list)

list_ifname_ip()
