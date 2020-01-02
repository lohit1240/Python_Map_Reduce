from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None
maxc=0
cid=None
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    if current_word == word:
	current_count += count
	if current_count>maxc:
		maxc=current_count
		cid=current_word
		#print '%d times %s is cited' % (maxc,current_word)
    else:
	current_count = count
       	current_word = word

print '%d times %s is cited' % (maxc,current_word)


