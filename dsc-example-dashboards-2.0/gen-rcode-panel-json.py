import yaml
import sys
import re

y = yaml.load(open(sys.argv[1], 'r'))

have = {}
groupby = []
reducer = []
for k in y['client_addr_vs_rcode']['Rcode']:
    if k == '0':
        continue
    v = y['client_addr_vs_rcode']['Rcode'][k]
    if v in have:
        continue
    have[v] = True
    groupby.append('"%s": {"aggregations": ["sum"],"operation": "aggregate"}' % v)
    reducer.append('"%s (sum)"' % v)

print(",\n".join(groupby))

print()

print(",\n".join(reducer))

