# Program Name: 'Last-to-Start' Activity Selector
# Filename: last_start.def foo():
# Author: Ryan Ellis
# Due Date: 4/29/18

# file handling

def pull_act_list(file_name):
	'''pulls list of activities from .txt associated with a file object'''

	# dump contents of file into file object
	input_file = open(file_name, 'r')

	# read that out into a list
	input_list = input_file.readlines()

	# close out the input file
	input_file.close()

	return input_list

def print_act_results(act_lists):
	'''prints out results of activity selection to the terminal'''

	for i, act_list in enumerate(act_lists):
		print('*' * 40)
		print('Set %d' % (i + 1))
		print('Number of activities selected = %d' % len(act_list))
		print('Activities: ' + ''.join(str(act_list)))
		print('*' * 40)

# list preparation

def build_lists(string_list):
	'''creates a container that holds the activity set(s)'''

	# list to hold activity lists
	act_lists = []
	# holds values after they are converted to integer
	converted_list = []

	for line in string_list:
		converted_line = []
		temp_line = line.split(' ')
		for item in temp_line:
			converted_line.append(int(item))
		converted_list.append(converted_line)

	# traveler to read through the lines from converted list
	i = 0

	while(i < len(converted_list)):

		# lines with 1 item define how many activities in set.
		if(len(converted_list[i]) == 1):

			# list that holds the activites for current activity set
			act_list = []

			# holds number of activities
			num_acts = converted_list[i][0]

			# start reading in the activities. k is traveler through converted_list
			# lines, and l is used as traveler to load those lines into act_list
			k = i + 1
			l = 0

			while(l < num_acts):
				act_list.append(tuple(converted_list[k]))
				k += 1
				l += 1

			i = k

			act_lists.append(act_list)

	#print act_lists

	return act_lists

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

	# will hold the act_results lists from each set
	act_results = []

	string_list = pull_act_list('act.txt')

	act_lists = build_lists(string_list)

	#print act_lists[0]

	#act_lists[0].sort(key = lambda activity: activity[1], reverse = True)

	#print act_lists[0]

	for act_list in act_lists:
		act_list.sort(key = lambda activity: activity[1], reverse = True)
		act_results.append(last_start(act_list))

	print_act_results(act_results)

main()