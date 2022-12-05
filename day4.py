f = open('day4.txt')
inp=[]
for line in f.readlines():
    line = line.strip()
    inp.append(line.split(','))
def isContainingOverlap(first,second):
    first = first.split('-')
    second = second.split('-')
    if (int(first[0])) <= (int(second[1])):
        if(int(first[0])) >= (int(second[0])):
            if(int(first[1])) <= (int(second[1])):
                return True
    return False

def containsAnyOverlap(first,second):
    first = first.split('-')
    second = second.split('-')
    if (int(first[0])) >= (int(second[0])):
        if (int(first[0])) <= (int(second[1])):
            return True
    if (int(first[1])) >= (int(second[0])):
        if (int(first[1])) <= (int(second[1])):
            return True
    return False


overlaps = 0 
for pair in inp:
    first= pair[0]
    second = pair[1]
    if (containsAnyOverlap(first,second)) or (containsAnyOverlap(second,first)):
            overlaps += 1
print(overlaps)
