di = dict()
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    bigtime = words[5]
    timelist = bigtime.split(':')
    di[timelist[0]] = di.get(timelist[0], 0) + 1
for k,v in sorted(di.items()):
    print(k,v)