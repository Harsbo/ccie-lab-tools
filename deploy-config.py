#!/usr/bin/env python

from netmiko import ConnectHandler
import requests

r1 = {'name': 'R1', 'connect': {'ip': '10.0.0.101', 'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_xe'}}
r2 = {'name': 'R2', 'connect': {'ip': '10.0.0.102', 'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_xe'}}
r3 = {'name': 'R3', 'connect': {'ip': '10.0.0.103', 'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_xe'}}
r4 = {'name': 'R4', 'connect': {'ip': '10.0.0.104', 'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_xe'}}
r5 = {'name': 'R5', 'connect': {'ip': '10.0.0.105', 'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_xe'}}
r6 = {'name': 'R6', 'connect': {'ip': '10.0.0.106', 'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_xe'}}
r7 = {'name': 'R7', 'connect': {'ip': '10.0.0.107', 'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_xe'}}
r8 = {'name': 'R8', 'connect': {'ip': '10.0.0.108', 'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_xe'}}
r9 = {'name': 'R9', 'connect': {'ip': '10.0.0.109', 'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_xe'}}
r10 = {'name': 'R10', 'connect': {'ip': '10.0.0.110', 'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_xe'}}
r11 = {'name': 'R11', 'connect': {'ip': '10.0.0.111', 'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_xe'}}
r12 = {'name': 'R12', 'connect': {'ip': '10.0.0.112', 'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_xe'}}
r13 = {'name': 'R13', 'connect': {'ip': '10.0.0.113', 'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_xe'}}
r14 = {'name': 'R14', 'connect': {'ip': '10.0.0.114', 'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_xe'}}
r15 = {'name': 'R15', 'connect': {'ip': '10.0.0.115', 'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_xe'}}
r16 = {'name': 'R16', 'connect': {'ip': '10.0.0.116', 'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_xe'}}
r17 = {'name': 'R17', 'connect': {'ip': '10.0.0.117', 'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_xe'}}
r18 = {'name': 'R18', 'connect': {'ip': '10.0.0.118', 'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_xe'}}
r19 = {'name': 'R19', 'connect': {'ip': '10.0.0.119', 'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_xe'}}
r20 = {'name': 'R20', 'connect': {'ip': '10.0.0.120', 'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_xe'}}

devices = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20]

baseurl = raw_input("URL to configs: ")

for device in devices:
    exist_check = requests.get(baseurl + device['name'] + '.txt')
    if exist_check.status_code == 200:
        print 'Configuring', device['name']
        net_connect = ConnectHandler(**device['connect'])
        net_connect.config_mode()
        net_connect.send_command('file prompt quiet')
        net_connect.exit_config_mode()
        net_connect.send_command('copy ' + baseurl + device['name'] + '.txt running')
        net_connect.disconnect()
    else:
        print 'Device config not available,', device['name']
