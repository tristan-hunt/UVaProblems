#https://interactivepython.org/courselib/static/pythonds/Trees/SearchTreeImplementation.html
import time



def main():
	first_dict = set()	

	with open('sample-input.txt') as file:

		# Read in a line of the file
		for line in file:

			# Seperate into words
			words = line.rstrip('\n').split(' ')
			for word in words:
				word = word.rstrip('.')
				word = word.rstrip('"')
				word = word.rstrip("'")
				word = word.rstrip(',')
				word = word.rstrip(';')
				
				word.lower
				print(word)
				first_dict.add(word)


			# Store alphabetically
	
	andys_dic = sorted(first_dict)
	print(andys_dic)


start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))