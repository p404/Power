#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import os
import io
import nmap
import pprint
import socket
import wakeonlan
from pathlib import Path
from paramiko import Transport, SSHClient, SSHConfig, ProxyCommand

HOME_PATH = str(Path.home())

def ssh_config(hostname):
    config = SSHConfig()
    config.parse(open('{}/.ssh/config'.format(HOME_PATH)))
    return config.lookup(hostname)

def ping(hostname):
	response = os.system("ping -c 1 -w2 " + hostname + " > /dev/null 2>&1")
	if response == 0 : return True
	else : return False

def nmap_host(hostname):
    nmap_obj = nmap.PortScanner()
    port = ssh_config(hostname)['port']
    host_scan = nmap_obj.scan(hostname, str(port))
    if host_scan['scan'][socket.gethostbyname(hostname)]['status']['state'] == 'up':
        return True

def host_is_up(hostname):
    if ping(hostname) or nmap_host(hostname):
        return True

def ssh_connection(hostname):
    host = ssh_config(hostname)
    ssh_client = SSHClient()
    ssh_client.load_system_host_keys()

    try:
        ssh_client.connect(host['hostname'], username=host['user'], sock=ProxyCommand(host.get('proxycommand')))
        return ssh_client  
    except:
        ssh_client.connect(host['hostname'], username=host['user'])
        return ssh_client

class Power():
    @staticmethod
    def turn_on(hosts):
        for host in hosts:
            if not host_is_up(host):
                wakeonlan.send_magic_packet(hosts[host]['mac'])
                print("{}".format(host))
            else:
                print("Host {} already turned on".format(host))

    @staticmethod
    def turn_off(hosts):
        for hostname in hosts:
            if host_is_up(hostname):
                ssh_client = ssh_connection(hostname)
                ssh_client.exec_command('sudo poweroff')
                ssh_client.close()
                print("{}".format(hostname))
            else:
                print("Host {} already turned off".format(hostname))

