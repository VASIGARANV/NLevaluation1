#Write a regex to extract all the numbers with orange color background from the below text in italics (Output should be a list).
import re
inp = {"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]}
op = re.findall(r': \d+',str(inp))
op = map(lambda x:x.replace(": ",""),op)
op = list(op)
print(op)
#Expected o/p: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '648', '649', '650', '651', '652', '653', '3']

