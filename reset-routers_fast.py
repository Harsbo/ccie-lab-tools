#!/usr/bin/env python

import sys, requests
from netmiko import ConnectHandler
requests.packages.urllib3.disable_warnings()

r1 = {'ip': '10.0.0.101', 'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_xe'}
r2 = {'ip': '10.0.0.102', 'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_xe'}
r3 = {'ip': '10.0.0.103', 'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_xe'}
r4 = {'ip': '10.0.0.104', 'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_xe'}
r5 = {'ip': '10.0.0.105', 'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_xe'}
r6 = {'ip': '10.0.0.106', 'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_xe'}
r7 = {'ip': '10.0.0.107', 'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_xe'}
r8 = {'ip': '10.0.0.108', 'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_xe'}
r9 = {'ip': '10.0.0.109', 'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_xe'}
r10 = {'ip': '10.0.0.110', 'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_xe'}
r11 = {'ip': '10.0.0.111', 'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_xe'}
r12 = {'ip': '10.0.0.112', 'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_xe'}
r13 = {'ip': '10.0.0.113', 'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_xe'}
r14 = {'ip': '10.0.0.114', 'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_xe'}
r15 = {'ip': '10.0.0.115', 'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_xe'}
r16 = {'ip': '10.0.0.116', 'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_xe'}
r17 = {'ip': '10.0.0.117', 'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_xe'}
r18 = {'ip': '10.0.0.118', 'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_xe'}
r19 = {'ip': '10.0.0.119', 'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_xe'}
r20 = {'ip': '10.0.0.120', 'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_xe'}

devices = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20]

def remove_vrf(device):
    try:
        token = requests.post('https://{h}:55443/api/v1/auth/token-services'.format(h=device),
                              auth=('cisco', 'cisco'), verify=False).json()['token-id']
    except:
        print 'Aborting. \nDevice unreachable {h}'.format(h=device)
        exit()

    vrfs = requests.get("https://{h}:55443/api/v1/vrf".format(h=device),
                        headers={'X-auth-token': token}, verify=False).json()

    for vrf in vrfs['items']:
        if vrf['name'] != 'Mgmt':
            requests.delete("https://{h}:55443/api/v1/vrf/{v}".format(h=device, v=vrf['name']),
                            headers={'X-auth-token': token}, verify=False)


def main():
    #Workaround for IOS crash bug
    print 'Removing all VRFs ... \n'
    for device in devices:
        remove_vrf(device['ip'])

    for device in devices:
        print 'Resetting', device['ip']
        net_connect = ConnectHandler(**device)
        net_connect.send_command('configure replace bootflash:clean_config.txt force')
        net_connect.disconnect()

if __name__ == '__main__':
    sys.exit(main())
