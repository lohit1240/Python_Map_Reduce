import re
import json
data = open("dblp-ref-3.json","r+")
dataf=json.load(data)
for i in dataf['citation']:
 if 'authors' in i:
  auths = i ["authors"]
  for j in auths:
    author = j.split(',')
    print '%s\t%s'%(author,"1")
    #auth=u'\t'.join((author,1)).encode('utf-8').strip()
    #print (auth)
