import math
class Monkey():
    def __init__(self,items,operation, divis, trueInd, falseInd):
        self.items=items #[]
        self.operation=operation #string
        self.test = divis # number
        self.true = trueInd # index of monkey
        self.false = falseInd # index of monkey
    def setItems(self,items):
                self.items=items
    def setOperation(self,op):
            self.operation = op
    def setTest(self,test):
            self.test = test
    def setTrue(self,trueind):
            self.true = trueind
    def setFalse(self,falseind):
            self.false = falseind


f = open('day11.txt')
curr=''
monkeys=[]
inspect={}
for line in f.readlines():
        line=line.strip()
        if 'Monkey' in line:
                if curr=='':
                        curr = Monkey([],'',1,1,1)
                else:
                        monkeys.append(curr)
                        curr = Monkey([],'',1,1,1)
        elif 'Starting'in line:
                nli= line.split(' ')
                nli = nli[2:]
                its=[]
                for thing in nli:
                        thing=thing.replace(',','')
                        its.append(int(thing))
                curr.setItems(its)
        elif 'Operation' in line:
                nli = line.split(' ')
                op = ''.join(nli[1:])
                curr.setOperation(op)
        elif 'Test' in line:
                nli = line.split(' ')
                no = int(nli[-1])
                curr.setTest(no)
        elif 'true' in line:
                nli = line.split(' ')
                ind = int(nli[-1])
                curr.setTrue(ind)
        elif 'false' in line:
                nli = line.split(' ')
                ind = int(nli[-1])
                curr.setFalse(ind)

monkeys.append(curr)
for m in range(0,len(monkeys)):
        inspect[m] = 0

def throw(monkeys,monkeyInd,item):
        its = (monkeys[monkeyInd]).items
        its.append(item)
        (monkeys[monkeyInd]).setItems(its)
        #print((monkeys[monkeyInd]).items)
        return monkeys

lcm=1
for t in monkeys:
        lcm = lcm * t.test
print(lcm)
def round(monkeys,lcm):
        for mon in monkeys:
                toremove=[]
                #print('monkey '+str(monkeys.index(mon)))
                for i in mon.items:
                        old = i
                        #print('inspecting item ' +str(i))
                        inspect[monkeys.index(mon)] +=1
                        op = ((mon.operation).split('='))[1]
                        new = eval(op)%lcm
                        #print('new value is '+str(new))
                        if new % mon.test==0:
                                monkeyInd = mon.true

                        else:
                                monkeyInd = mon.false
                        #print('throw to monkey '+ str(monkeyInd))
                        toremove.append(old)
                        monkeys=throw(monkeys,monkeyInd,new)
                for r in toremove:
                        mon.items.remove(r)
        return monkeys

                                
for i in range(0,10000):
        monkeys=round(monkeys,lcm)                
for m in monkeys:
        print(m.items)
sort_ins = {k: v for k, v in sorted(inspect.items(), key=lambda item: item[1])}
max1= list(sort_ins.keys())[-1]
max2 = list(sort_ins.keys())[-2]
print(sort_ins[max1]*sort_ins[max2])
