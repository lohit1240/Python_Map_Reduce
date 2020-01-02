from operator import itemgetter
from heapq import nlargest
import sys

current_name = None
current_count = 0
name = None
namedis={}

for line in sys.stdin:
    line = line.strip()

    name, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue

    if current_name == name:
        current_count += count
	namedis.update({current_name:current_count})
    else:
     #   if current_name:
     #       print '%d\t%s' % (current_count,current_name)
        current_count = count
        current_name = name

#if current_name == name:
 #   print '%d\t%s' % (current_count,current_name)
top_authors=nlargest(10,namedis,key=namedis.get)
print(top_authors)
