# Power

Power, Tool for managing power state of multiples machines using Wakeonlan/SSH

## Installing
```bash
1. git clone https://github.com/p404/power.git
2. cd power
3. pip3 install -r requirements.txt
```
## Usage
```bash
usage: power [-h] [--debug] [--quiet] {off,on} ...

Power, Tool for managing power state of multiples machines using Wakeonlan/SSH

optional arguments:
  -h, --help  show this help message and exit
  --debug     toggle debug output
  --quiet     suppress all output

sub-commands:
  {off,on}
    off     Turn off machines
             optional arguments:
              -h, --help              show this help message and exit
              --hosts [HOSTS [HOSTS ...]], -hosts [HOSTS [HOSTS ...]]
                                      Turn off machines by hostname
              --tag TAG, -t TAG       Turn off machines by tag
    
    on      Turn on machines
             optional arguments:
              -h, --help             show this help message and exit
              --hosts [HOSTS [HOSTS ...]], -hosts [HOSTS [HOSTS ...]]
                                     Turn on machines by hostname
              --tag TAG, -t TAG      Turn on machines by a tag
```
## Configuration example
$HOME/.power/config.yml
```yaml
---
hosts:
  example0.domain.tld:
    ipv4: 192.168.2.3
    mac: F4:00:30:69:B7:7A
    nic: eth0
    tag: office
  example1.domain.tld:
    ipv4: 192.168.2.4
    mac: 00:23:18:CC:20:F5
    nic: enp3s0
    tag: office
```
## License
[MIT](https://github.com/p404/power/blob/master/LICENSE)
