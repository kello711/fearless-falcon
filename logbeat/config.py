from ruamel.yaml import YAML
from ruamel.yaml.scalarstring import DoubleQuotedScalarString

import sys
import ipaddress

# Validate a correct IP address was input
def valid_ip(address):
    try:
        # print(ipaddress.ip_address(address))
        return True
    except:
        return False

beats = {'filebeat', 'winlogbeat', 'metricbeat', 'packetbeat'}

# Start of the program
ipAddr = '1.2.4.5' # Remove the fake IP, only here for testing
port = ''
while not valid_ip(ipAddr):
    ipAddr = input("Enter IP: ")
    port = input("Enter port: ")
if port == '':
    port = '5044'

# Setting up the ruamel.yaml to properly read libbeat configs
yaml = YAML()
yaml.default_flow_style = False
yaml.indent(mapping=2, sequence=4, offset=2)
yaml.preserve_quotes = True

# Read the winlogbeat config
config_doc = open('winlogbeat.yml', 'r')
loaded_config = yaml.load(config_doc)

# Remove default host
loaded_config['output.logstash']['hosts'].pop(0)

# Create logstash hostname:port string and insert into the config map
hostName = DoubleQuotedScalarString(ipAddr + ":" + port)
loaded_config['output.logstash']['hosts'].insert(0, hostName)

# Remove the outpout.elasticsearch section
del loaded_config['output.elasticsearch']

# Output the corrected config to screen, can also dump to a file
# yaml.dump(loaded_config, sys.stdout)
newConfigFile = open('winlogbeat_test.yml', 'w')
yaml.dump(loaded_config, newConfigFile)
