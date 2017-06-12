#!/usr/bin/env python

import time
from netmiko import ConnectHandler

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

print 'SSH test (execution time approx 30 sec) \n'
for device in devices:
    try:
        net_connect = ConnectHandler(**device)
        net_connect.disconnect()
    except:
        print 'Failed to connect: ', device['ip']

raw_input("Proceed? \n")

for device in devices:
    print 'Resetting', device['ip']
    net_connect = ConnectHandler(**device)
    net_connect.config_mode()
    net_connect.send_command('file prompt quiet')
    net_connect.exit_config_mode()
    net_connect.send_command('copy bootflash:clean_config.txt startup-config')
    net_connect.send_command('reload in 1 \r')
    net_connect.disconnect()
    if device['ip'] != devices[-1]['ip']:
        print 'Waiting 90 sec'
        time.sleep(90)
    else:
        print 'Done\n'
