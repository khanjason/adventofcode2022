f= open('day10.txt')
instructs= []
cycle =1
X=1
adding = False
signals={}
full_crt=[]
curr = ''
def doCRT():
    global X
    global curr
    if len(curr)== 40:
        full_crt.append(curr)
        curr=''
    if len(curr) in range(X-1,X+2):
        return curr+'#'
    else:
        return curr+'.'

def addx(num):
    global X
    global cycle
    global adding
    X = X +val
    cycle = cycle + 1
    adding = False

def outputSignal():
        global cycle
        global X
        global signals
        signals[cycle] = X
        
for line in f.readlines():
	line=line.strip()
	instructs.append(line)
count =1
for ins in instructs:
    if cycle == 240:
        curr=doCRT()
        outputSignal()
        break
    if 'noop' in ins:
        curr=doCRT()
        cycle +=1
        outputSignal()
        
    elif 'addx' in ins:
        curr=doCRT()
        cycle +=1
        li=(ins.split(' '))
        outputSignal()
        if cycle == 240:
            break
        val =int(li[1])
        curr=doCRT()
        addx(val)
        outputSignal()
full_crt.append(curr)

#print(signals)
def getRange():
    global signals
    tot=0
    for i in range(20,len(signals.keys())+20,40):
        tot+=(i*signals[i])
        #print(i*signals[i])
    print(tot)
getRange()
for li in full_crt:
    print(li)
print(full_crt)
