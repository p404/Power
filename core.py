#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import io
import yaml
import socket
import wakeonlan
from pathlib import Path
from paramiko import Transport, SSHClient, SSHConfig, ProxyCommand

HOME_PATH = str(Path.home())

with open("/Users/pablo/.patron/config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

servers = cfg['hosts']

def ssh_connection(hostname):
    config = SSHConfig()
    config.parse(open('{}/.ssh/config'.format(HOME_PATH)))
    host = config.lookup(hostname)

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
            try:
                wakeonlan.send_magic_packet(hosts[host]['mac'])
                print("Turning on: {}".format(host))
            except:
                pass
    @staticmethod
    def turn_off(hosts):
        for hostname in hosts:
            ssh_client = ssh_connection(hostname)
            ssh_client.exec_command('sudo poweroff')
            print("Turning off: {}".format(hostname))


#Power.turn_on(servers)
Power.turn_off(servers)


