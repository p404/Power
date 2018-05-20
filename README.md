# Power

Power, Tool for managing power state of multiples machines using Wakeonlan/SSH

## Installing
```bash
1. git clone https://github.com/p404/power.git
2. cd power
3. pip3 install .
```
## How to use
```bash
usage: si-ip.py [-h] -c CONFIG

SI-IP Minimal Dynamic DNS for AWS Route 53

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG, --config CONFIG
                        Loads configuration
```
## Configuration example
config.yml
```bash
[global]
aws_access_key_id     = <AWS KEY>
aws_secret_access_key = <AWS KEY SECRET>
[records]
refresh_interval      = <REFRESH INTERVAL IN SECONDS>
hosted_zone_id        = <AWS ZONE ID>
record_name           = <AWS RECORD NAME>
```
## License
[MIT](https://github.com/p404/power/blob/master/LICENSE)
