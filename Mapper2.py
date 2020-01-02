import json
import sys
#data =open("citation.json","r+")
data = json.load(sys.stdin)
#dataf=json.load(data)
jstr = json.dumps(data, indent=4)
print(jstr)
