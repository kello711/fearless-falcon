import yaml

stream = open('winlogbeat.yml', 'r')
doc = yaml.load(stream)

print(str(doc) + '\n')

print(yaml.dump(doc, indent=3))
