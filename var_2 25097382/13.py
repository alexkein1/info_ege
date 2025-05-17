from ipaddress import *

net = ip_network('98.81.154.195/255.252.0.0', False)
for ip in net:
    print(ip)  # 9883255254 (98.83.255.255 - широковещательный)
