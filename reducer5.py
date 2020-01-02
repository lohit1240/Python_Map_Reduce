from operator import itemgetter
from heapq import nlargest
import sys

current_id = None
current_count = 0
id = None
iddis={}

for line in sys.stdin:
    line = line.strip()

    id, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue

    if current_id == id:
        current_count += count
	iddis.update({current_id:current_count})
    else:
     #   if current_id:
     #       print '%d\t%s' % (current_count,current_id)
        current_count = count
        current_id = id

#if current_id == id:
 #   print '%d\t%s' % (current_count,current_id)
five_largest=nlargest(5,iddis,key=iddis.get)
print(five_largest)
