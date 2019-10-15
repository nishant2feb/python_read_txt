
# read line from input.txt
with open('input.txt') as infile:

    # loop through each line
    for line in infile:
        # separate line into list
        splitted = line.split(' ')

        # find last str of list
        last = splitted[-1]

        # cast above into int
        value = int(last)

        # print out the value
        print(value)
