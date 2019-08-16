'''
Problem: Fibre Cabling
A big internet infrastructure company in New Zealand has been tasked with wiring up homes with
fibre optic broadband cables. However, since this is a business for profit, not all homes will need to
be hooked up. The company Circus has asked you to help them determine which homes they should
connect cables, ready for sale. The main constraint of this problem is that if two homes on a street is
cabled then all intermediate homes on the path between them must also be, irrespective if they sign-
up for an internet plan or not. The company makes a certain amount of prot based on which plan
customers purchase; it also losses money if a complicated connection is done without any plan purchase.

An input scenario is a sequence A1, A2, .... An of n <= 100000 integers on one line, denoting the profit/loss
for connecting each house on a street of length n. The entry at position i, 1 <= i <= n, is positive for
profit and negative for loss. We have many streets of data to process and a single line containing only
one integer denotes the end of input (this scenario is not processed). We can assume each scenario has
at least one positive house value ai, since otherwise Circus would not even consider cabling that street.
The output of your program, one line per each scenario, is the maximum prot obtainable for that
street.

Solution: Dynamic Programming approach
'''

stringOut = ""          #output string
while True:
	line = input()          #get input from console
	if len(line) > 1:
		total = 0               #setting up variables for the maximum for some length in the iteration
		currentMax = 0          #variable for the current max for the row
		streets = line.split()	
		for i in streets:       #iterating through houses
			number = int(i)
			total = max(number + total, 0)  #if total profit at current point is a negative, reset total profit to 0
			if currentMax < total:
				currentMax = total      #current maximum is replaced the total profit for the new length of houses is higher
			else:
				pass
		stringOut += str(currentMax) + "\n"     
	else:
		break

print(stringOut[:len(stringOut)-1])

'''
test cases:

fibreDP.py
10 -4 5
3 -4 5
3 -10 4 41 -1
10 0 20 -4 -3 8 -7 4
4 4 -3 1 0 0 -4 1 3 -4 7 -2 -2 3
1
'''
