buffer = ''
f = open('day6.txt')
for line in f.readlines():
	buffer = line.strip()

p0=0
p1=1
p2=2
for i in range(3,len(buffer)):
	if len(set(buffer[i]+buffer[p0]+ buffer[p1] +buffer[p2]))==4:
		#print(i+1)
		break
	else:
		p0 +=1
		p1 +=1
		p2 +=1

# part2
hold = []
for i in range(0,len(buffer)):
	hold = buffer[i:i+14]
	#print((hold))
	if len(set(hold)) ==14:
		print(i+14)
		break
print('done')

