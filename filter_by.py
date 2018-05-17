#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import yaml

with open("/Users/pablo/.patron/config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

SERVERS = cfg['hosts']

def host(hostname):
    for server in SERVERS:
        if server == hostname:
            return {hostname : SERVERS[hostname]}

def tag(tag):
    servers_dict = {}
    for server in SERVERS:
        if SERVERS[server]['tag'] == tag:
            servers_dict[server] = SERVERS[server]
    return servers_dict
