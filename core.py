#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import io
import yaml
import wakeonlan
from fabric import Connection

with open("/Users/pablo/.patron/config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

servers = cfg['hosts']

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
            Connection(hostname, connect_timeout=2).sudo('shutdown +0')
            print("Turning off: {}".format(hostname))

#Power.turn_on(servers)
Power.turn_off(servers)


