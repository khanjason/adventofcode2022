
def part1():
	pairs=  {'X': 'A', 'Y' :'B', 'Z' : 'C'}
	shape_scores= {'X':1, 'Y' :2, 'Z' :3}
	win_scores = {'loss'  : 0, 'draw' : 3, 'win': 6}
	win_pairs = {'X':'C','Y':'A', 'Z':'B'}
	total_score=0
	f = open('day2.txt')
	inp = []
	for line in f.readlines():
		tmp = line.split()
		inp.append(tmp)

	for li in inp:
		opp = li[0]
		player= li[1]
		total_score+= shape_scores[player]
		if win_pairs[player] == opp:
			total_score += win_scores['win']
		elif pairs[player] == opp:
			total_score += win_scores['draw']
		else:
			total_score+= win_scores['loss']
	print(total_score)

def part2():
	f = open('day2.txt')
	inp=[]
	total_score=0
	outcome_pairs = {'X':'lose','Y':'draw','Z':'win'}
	win_pairs = {'A':'C','B':'A','C':'B'}
	lose_pairs = {'C':'A','A':'B','B':'C'}
	win_scores = {'lose':0, 'draw':3,'win':6}
	shape_scores = {'A':1,'B':2,'C':3}	

	for line in f.readlines():
		tmp = line.split()
		inp.append(tmp)
	for li in inp:
		opp = li[0]
		outcome= li[1]

		
		if outcome_pairs[outcome] == 'draw':
			player= opp
			total_score+=win_scores['draw']
			
		elif outcome_pairs[outcome] == 'lose' :
			player = win_pairs[opp]
			total_score += win_scores['lose']
		else:
			player = lose_pairs[opp]
			total_score += win_scores['win']
		
		total_score += shape_scores[player]
	print(total_score)
part1()
part2()
