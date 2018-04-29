# Program Name: 'Last-to-Start' Activity Selector
# Filename: last_start.py
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
		# reverse the act list so activities are shown in the correct
		# order
		act_list.reverse()
		print('Activities: ' + ' '.join(str(x) for x in act_list))
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

def merge(sub_list, left, middle, right):

    # get the lengths of each half
    left_length = middle - left + 1
    right_length = right - middle

    # make left and right lists to hold the halves
    left_list = [0] * (left_length + 1)
    right_list = [0] * (right_length + 1)

    # load the values from master list into those lists
    for i in range(0, left_length):
        left_list[i] = sub_list[left + i]

    for j in range(0, right_length):
        right_list[j] = sub_list[middle + j + 1]

    i = 0
    j = 0
    k = left

    while i < left_length and j < right_length:
        if left_list[i][1] >= right_list[j][1]:
            sub_list[k] = left_list[i]
            i = i + 1
        else:
            sub_list[k] = right_list[j]
            j = j + 1
        k = k + 1

    # loads all the remaining items still in the left/righ lists back into
    # the main list.
    while i < left_length:
        sub_list[k] = left_list[i]
        i = i + 1
        k = k + 1

    while j < right_length:
        sub_list[k] = right_list[j]
        j = j + 1
        k = k + 1

def merge_sort(a_num_list, left, right):

    if left < right:
        middle = ((left + right) / 2)
        merge_sort(a_num_list, left, middle)
        merge_sort(a_num_list, (middle + 1), right)
        merge(a_num_list, left, middle, right)

    return a_num_list

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

	for act_list in act_lists:
		list_length = len(act_list) - 1
		sorted_act_list = merge_sort(act_list, 0, list_length)
		act_results.append(last_start(sorted_act_list))

	print_act_results(act_results)

main()