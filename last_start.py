# Program Name: 'Last-to-Start' Activity Selector
# Filename: last_start.def foo():
# Author: Ryan Ellis
# Due Date: 4/29/18

# file handling

def pull_act_list():
	'''pulls list of activities from .txt associated with a file object'''

def print_act_results():
	'''prints out results of activity selection to a .txt file associated with a file object'''

# list preparation

def build_lists():
	'''creates a container that holds the activity set(s)'''

# algorithm

def last_start(act_list):
	'''last-to-start activity selection implementation'''

	# list that will hold optimal activities for the activity list
	act_results = []

	# check to make sure there are activities in list
	if len(act_list) > 0:

		# add last activity to results list
		act_results.append(act_list[0][0])

		# travelers used to iterate through the activity list
		i = 0
		j = 1

		# iterate through list checking i's start time vs. j's finish time
		while(j < len(act_list)):
			if act_list[i][1] >= act_list[j][2]:
				act_results.append(act_list[j][0])
				i = j
			j += 1

	return act_results

def main():
	'''driver code'''
	


main()