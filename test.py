import sys

sum = 0

for i in range(1, 11):
	sum = sum + i

print (sys.version)
print ('sum is {0}'.format(sum))


def sum (a, b):
	return a + b

print ('Function sum is {0}'.format(sum(1, 2)))
