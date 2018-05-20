# -*- coding: UTF-8 -*-
import os
import sys
import yaml
from pathlib import Path

class PowerConfig:
    def __init__(self):
        config_file = Path(os.path.join(Path.home(), '.power', 'config.yml'))
        if config_file.is_file():
            self.SERVERS = self._config_open(config_file)['hosts']
        else:
            self._config_init(config_file)

    def _ask_input(self, message):
        yes = {'yes','y', 'ye', ''}
        no = {'no','n'}

        choice = input(message).lower()
        if choice in yes:
            return True
        elif choice in no:
            return False
        else:
            print("Please respond with 'yes' or 'no'")
            sys.exit()

    def _config_init(self, config_file):
        example_config = {'hosts': {'example0.domain.tld': {'nic': 'eth0', 'ipv4': '192.168.2.3', 'mac': 'F4:00:30:69:B7:7A', 'tag': 'office'}, 
                                    'example1.domain.tld': {'nic': 'enp3s0', 'ipv4': '192.168.2.4', 'mac': '00:23:18:CC:20:F5', 'tag': 'office'}}}

        print('ERROR: There is no configuration file at {}'.format(config_file))
        if self._ask_input('INFO: Do you want generate a example config? y/n : '):
            if config_file.parent.is_dir():
                with open(config_file, 'w') as yaml_file:
                    yaml.dump(example_config, yaml_file, default_flow_style=False)
                sys.exit()
            else:
                os.makedirs(config_file.parent)
                if config_file.parent.is_dir():
                    with open(config_file, 'w') as yaml_file:
                        yaml.dump(example_config, yaml_file, default_flow_style=False)
                sys.exit()

    def _config_open(self, config_file):
        with open(config_file, 'r') as ymlfile:
            return yaml.load(ymlfile)

    def filter_by_host(self, hostname):
        for server in self.SERVERS:
            if server == hostname:
                return {hostname : self.SERVERS[hostname]}

    def filter_by_tag(self, tag):
        servers_dict = {}
        for server in self.SERVERS:
            if self.SERVERS[server]['tag'] == tag:
                servers_dict[server] = self.SERVERS[server]
        return servers_dict
