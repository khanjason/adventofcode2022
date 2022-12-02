maxi=0
second=0
third=0
f = open('day1.txt')
counting=0
for line in f.readlines():
	if (line).strip() != '':
		counting=counting+int(line.strip())
	else:
		if (counting) > maxi:
			second = maxi
			maxi = counting
		elif counting > second:
			third = second
			second = counting
		elif counting > third :
			third = counting
		counting=0

print(sum([maxi, second, third]))
