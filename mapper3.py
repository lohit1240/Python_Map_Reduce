import json
data = open("dblp-ref-3.json","r+")
dataf=json.load(data)
print("Original paper ID","->","Referenced paper ID")
for j in dataf['citation']:
  mid = j["id"]
  #print ("inside first loop-",mid)
  for i in dataf['citation']:
    cid=i["id"]
    if 'references' in i:
      #print("inside second loop-",cid)
      ref = i ["references"]
      if mid in ref:
        print (mid,"->",cid)