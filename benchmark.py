import json

# Parameters
POP_RANGE = 0.1   #+/- 10%
POP_FILE = 'static_dic/population92.json'
BUDGET_RANGE = 0.1
BUDGET_FILE = 'static_dic/budgets.json'
LOCATION_RANGE = 1
LOCATION_FILE = 'None'


def similar_pop(code):
	"""Finds similar cities in terms of population"""
	L = []
	reader = open(POP_FILE, 'r')
	dico = json.load(reader)
	ref_pop = dico[code]["pop"]
	for key in dico:
		try :
			comp_pop = dico[key]["pop"]
		except :  #in case no data is available
			comp_pop = 0
		if comp_pop > (1-POP_RANGE)*ref_pop and comp_pop < (1+POP_RANGE)*ref_pop:
			L.append((key, comp_pop))
	reader.close()
	return(L)
	pass 

def similar_budget(code):
	"""Finds similar cities in terms of budget"""
	L = []
	reader = open(BUDGET_FILE, 'r')
	dico = json.load(reader)
	ref_budget = dico[code]["budget"]["2015"]
	for key in dico:
		try :
			comp_budget = dico[key]["budget"]["2015"]
		except :  #in case no budget for year 2015 is available
			comp_budget = 0
		if comp_budget > (1-BUDGET_RANGE)*ref_budget and comp_budget < (1+BUDGET_RANGE)*ref_budget:
			L.append((key, comp_budget))
	reader.close()
	return(L)

def similar_loc(code):
	"""Finds neighbor cities"""
	pass

def benchmark(code, comparator):
	"""Compares indicators of similar cities. Benchmark can be 
	maid on either population, budget or location similarity
	"""
	if comparator=="pop":
		pass
	elif comparator=="budget":
		print(similar_budget(code))
		pass
	elif comparator=="location":
		pass


def valid_answer(string):
	if string in ["pop","location","budget"]:
		return True
	else :
		print("illegal answer")
		return False
		raise Illegal

class Illegal(Exception):
	pass

def main(code):
	answer_is = False
	while not answer_is:
		inp = input("which benchmark basis (pop/budget/location) ? ")
		answer_is = valid_answer(inp)
	benchmark(code, inp)



