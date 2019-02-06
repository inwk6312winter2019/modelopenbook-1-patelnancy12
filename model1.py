# ths is open book test model 1

fopen=open("running-config.cfg",'r')
fopen=fopen.read()
fopen=fopen.split("\n")
final_list = list()
interface_list = list()
intdict=dict()
access_list =  list()
transit_access_in = list()
fw_management_access_list = list()


def list_ifname_ip():

	for v in fopen:
		if "interface" in v:
			v=v.split()
			interface_list.append(v[1])
		if "nameif" in v:
			v=v.split()
			if "no" in v[0]:
				interface_list.append("null")
			else:
				interface_list.append(v[1])
		return intdict
print(list_ifname_ip())
