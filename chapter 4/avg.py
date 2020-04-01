x = input('type something: ')
l = len(x)
lastindex = l - 1
index = 0
pal = True
while index < l:
    forwardchar = x[index]
    reverseindex = lastindex - index
    reversechar = x[reverseindex]
    index = index + 1
    if forwardchar != reversechar:
        pal = False
        print(x,'is not a palindrome')
        break
if forwardchar == reversechar:
    print(x, 'is a palindrome')
        