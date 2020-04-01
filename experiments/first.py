from xmlrpc.client import boolean
x = input('type something:')
l = len(x)
lastindex = l - 1
index = 0
pal = True
while index < l:
    forwardchar = x[index]
    reverseIndex = lastindex - index
    reverseChar = x[reverseIndex]
    index = index+ 1
    if forwardchar != reverseChar:
        pal = False
        break
    
if pal:
    print(x,' is a palindrome')
else:
    print(x,' is not a palindrome')
    