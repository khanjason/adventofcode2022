f = open('day5.txt')
stacks=[]
rows=[]
instructions = []
for line in f.readlines():
	
	if ']' in line:
		newli=[]
		st=''
		for ch in line:
			if ch == '[' or ch == ']' or st=='    ':
				if(st != ' ') and (st!='') :
					newli.append(st)
				st =''
			else:
				st=st+ch
		if(st!=' ') and (st!='\n'):
			newli.append(st)
		rows.append(newli)
	if 'move' in line:
		values=[]
		valtmp=''
		for ch in line:
			if ch.isnumeric():
				valtmp=valtmp+ch
			else:
				if(valtmp!=''):
					values.append(int(valtmp))
				valtmp=''
		if(valtmp!=''):
			values.append(int(valtmp))
		instructions.append(values)

number_of_stacks=len(rows[-1])

for i in range(0,number_of_stacks):
	n=[]
	for r in rows:
		
		if len(r[i]) ==1:
			n.append(r[i])
		
	stacks.append(n)

				
print(stacks)

def popcrate(source, dest):
	popped = source[0]
	if len(source) > 1:
		source = source[1:]
	else:
		source = []
	dest = [popped] + dest
	return [source,dest]
#for part2

def multicrate(times,source,dest):
	popped_stack = []
	for t in range(0,times):
		popped = source.pop(0)
		popped_stack.append(popped)	
	
	print(popped_stack,times)
	dest = popped_stack + dest
	return [source,dest]

for ins in instructions:
	print(ins)
	times = ins[0]
	#for t in range(0,times):
	#if len(stacks[ins[1]-1]) > 0:
	#ret = popcrate(stacks[ins[1]-1], stacks[ins[2]-1])
	#stacks[ins[1]-1] = ret[0]
	#stacks[ins[2]-1] = ret[1]
	#if len(stacks[ins[1]-1]) >= times :
	
	ret = multicrate(times,stacks[ins[1]-1],stacks[ins[2]-1])
	stacks[ins[1]-1] = ret[0]
	stacks[ins[2]-1] = ret[1]

print(stacks)
ans = ''
for stack in stacks:
	ans = ans + stack[0]
print(ans)

