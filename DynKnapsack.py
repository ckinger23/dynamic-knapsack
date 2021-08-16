'''
Homework 7 Problem 1: Dynamic Knapsack
Carter King
Dr. Sanders
CS 355 Advanced Algorithms
27 November 2018
Python 3
'''

import sys


'''
Function: knapsack(n, W, weights, values)
 This function uses dynamic programming to find the maximum value of items one can take without exceeding a specific capacity,
 W. The data is stored in a 2-D array utilizing memoization. To discover the exact items to be taken, we retrace the array from 
 the bottom-right corner, and return the array and write the results to a file
 parameters: n: the number of items in consideration
             W: the capacity the knapsack can hold
             weights: an array of the weight of each item
             values: an array of the value of each item
 returns: ouputs results to a file
'''


def knapsack(n, W, weights, values):

    f = open("output2.txt","w+")


    # each row of the table indicates a new item

    # initializing the array to all zeros
    # table = [[0]*(w+1)]*(h+1)  THIS IS THE PART THAT SCREWED UP MY CODE
    # THESE APPEAR TO BE the same but IS NOT A DEEP COPY
    # BE CAREFUL IN PYTHON

    table = [[0 for x in range(W + 1)] for i in range(len(values) + 1)]
    #print(table)

    # First iterate over the items (rows)
    # second iterate over the columns which represent weights

    for i in range(1, n + 1):
        for x in range(1, W + 1):
            currWeight = weights[i - 1]  # did this to make the code more readable
            currValue = values[i - 1]  # as the indices get confusing

            # If the item weights more than the capacity at that column?
            # Take above value, that problem was solved

            if currWeight > x:  # case 1
                table[i][x] = table[i - 1][x]


            else:
                # we can fit the item in the sack and now we have to figure out
                # if it's worth swiping it

                # if the value of the item < capacity
                dont_bring = table[i - 1][x]
                #         val of current item  + val of remaining weight
                do_bring_it = currValue + table[i - 1][x - currWeight]

                table[i][x] = max(dont_bring, do_bring_it)
        #print(table)

    for b in table:
        f.write(repr(b)+ "\n")
        #f.write("%s\n" % b)

    f.write("The Max value that can be stored is:" + repr(max([x for y in table for x in y])) + "\n")

    # Let's try to figure out the result
    result = []
    weightLimit = W

    for i in range(n, 0, -1):
        #print("Going through item", i, "current weight limit", weightLimit)

        if table[i][weightLimit] != table[i - 1][weightLimit]:
            item = (i - 1, weights[i - 1], values[i - 1])
            result.append(item)
            weightLimit -= weights[i - 1]
            #print("Current Result Table:", result)

    f.write("Result is (item number, weight, value)" + repr(result))
    f.close()


'''
Function: parseFile(filename)
 This function takes a .txt file of containing the number of items, the capacity, a line representing the weights, and one
 representing the values  
 parameters: filename - a string of the name of the file 
 returns: n: the number of items in consideration
          W: the capacity the knapsack can hold
          weights: an array of the weight of each item
          values: an array of the value of each item
'''


def parseFile(filename):
    infile = open(filename, 'r')  # read the file and add elements to list
    for i, line in enumerate(infile):
        if i == 0:
            numAndCap = line.split(' ')
            n = int(numAndCap[0])
            W = int(numAndCap[1])
        elif i == 1:
            weights = line.split(' ')
            weights = [int(i) for i in weights]
        else:
            values = line.split(' ')
            values = [int(y) for y in values]

    return n, W, weights, values


def main():
    # Show them the default len is 1 unless they put values on the command line
    print(len(sys.argv))
    if len(sys.argv) == 2:
        fileName = sys.argv[1]
    else:
        fileName = input("Which input file would you like to use? ")
        n, W, weights, values = parseFile(fileName)
        knapsack(n, W, weights, values)


main()
