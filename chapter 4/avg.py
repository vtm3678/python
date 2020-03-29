count = 0
sum = 0
print('Before', count, sum)
for value in [1,24,675,35753,3477]:
    count = count + 1
    sum = sum + value
    print(count, sum ,value)
average = sum / count
print('after',count, sum, average)