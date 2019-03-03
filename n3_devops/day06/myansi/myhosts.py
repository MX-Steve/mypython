#!/usr/bin/env python3
import json

hostlist = {}
hostlist['web']=['es1', 'es2']
hostlist['db']=['es3', 'es4']
hostlist['other']=['192.168.1.30']
hostlist['app']= ['es1', 'es3', '192.168.1.30']
print(json.dumps(hostlist))
