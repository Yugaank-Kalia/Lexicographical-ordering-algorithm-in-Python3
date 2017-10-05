
'''     									Lexical ordering algorithm 											'''
# importing dependencies 

import math

def swap(array,i,j):
	
	array[i],array[j] = array[j],array[i]

value = list()
total = list()

def permutations(n):

	value = [1,2,3]

	# STEP 1

	for z in range(math.factorial(len(value))):

		print (value)

		for k in range(math.factorial(len(value))):
			
			largestX = -1
			
			for i in range(len(value)-1):
			
				if (value[i]<value[i+1]):
			
					largestX = i

			# STEP 2

			largestY = -1
			
			for j in range(len(value)): 
			
				if (value[largestX] < value[j]): 
			
					largestY = j

			# STEP 3

			swap(value,largestX,largestY)

			# STEP 4

			
			endArray = value[largestX+1:]
			
			value = value[:largestX+1]
			
			endArray.reverse()
			
			value.extend(endArray)