import json
data = open("dblp-ref-3.json","r+")
dataf=json.load(data)
for i in dataf['citation']:
  if 'references' in i:
    ref = i ["references"]
    for j in ref:
      refid = j.split(',')
      print "%s\t%s"%(refid,"1")
