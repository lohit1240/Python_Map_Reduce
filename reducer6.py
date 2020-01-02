import sys
import re
current_name=None
current_count=0
author=None
for name in sys.stdin:
	name = name.strip()
	author,count=name.split('\t',1)
	try:	
		count = int(count)
	except:
		continue	
	if current_name==author:
		#print ("Author matched--")		
		current_count+=count
	else:
		if current_name:
			print '%s\t%s' % (current_name,current_count)
		current_count=count
		current_name=author
if current_name==author:
	print '%s\t%s' % (current_name,current_count)

