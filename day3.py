f = open('day3.txt')
rucksacks = []
def getpriority(ch):
    if (ch.lower() == ch):
        number = ord(ch) - 96
    else:
        number = (ord(ch.lower()) - 96) +26
    return number

for line in f.readlines():
    rucksacks.append(line.strip())
print(rucksacks)
total = 0 
for r in rucksacks:
    mid = int(len(r)/2)
    first = set(r[:mid])
    second = set(r[mid:])
    share = first.intersection(second)
    #print(''.join(share))
    priority = getpriority(''.join(share))
    #print(priority)
    total += priority
print(total)    
  
# part 2
groups = []
newli = []
counter = 0
for r in rucksacks:
    if counter == 3:
        groups.append(newli)
        newli = []
        counter = 0
    newli.append(r)
    counter += 1
groups.append(newli)
#print(groups)
total_2 = 0
for group in groups:
    share = set(group[0]) & set(group[1]) & set(group[2])
    priority = getpriority(''.join(share))
    total_2 += priority
print(total_2)


