import re
fhand = open('mbox.txt')
di = dict()
lst = list()
for line in fhand:
    line = line.rstrip()
    if re.search('From:',line):
        lst.append(line)
for thing in lst:
    di[thing] = di.get(thing, 0) + 1
count = 0
for k,v in di.items():
    if v > count:
        count = v
        alberto = (k,v)
print(alberto)