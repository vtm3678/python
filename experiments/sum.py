fname = input ('Enter file name:')
fhand = open(fname, 'w')
numlist = list()
while True:
    inp = input('Enter a number:')
    if inp == 'done':break
    try:
        value = float(inp)
    except:
        print('not a number')
        continue
    numlist.append(value)
    total = sum(numlist)
    count = len(numlist)
    avg = total/count
print('Total:',total)
print(count,'values typed.')
print('Average:',avg)
numlist.append(total)
numlist.append(count)
numlist.append(avg)
for item in numlist:
    fhand.write("%s\n" % item)
fhand.close()
fleg = open(fname, 'r')
x = input('Would you like to view your file?')
if x.lower() == 'yes':
    for cheese in fleg:
        print(cheese)
    fleg.close()
