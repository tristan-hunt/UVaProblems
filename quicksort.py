# https://www.youtube.com/watch?v=4IvYaOY8Pxw
# http://stackoverflow.com/questions/3755136/pythonic-way-to-check-if-a-list-is-sorted-or-not
import sys
import math
import numpy

# def issorted(x):
#     """Check if x is sorted"""
#     return (numpy.diff(x) >= 0).all() # is diff between all consecutive entries >= 0?

def merge_and_count_split(b, c):
	"""
	Use merge-sort to count inversions
	"""
	#sys.stdout.write("merging: b: {} and c: {}\n".format(b, c))

	d = list() # merged b and c
	i = 0 # index for b
	j = 0 # index for c
	z = 0  # amount of splits
	n = len(b)

	while (i < len(b) and j < len(c)):
		if b[i] < c[j]:
			d.append(b[i])
			i = i + 1
		else: #c[j] < b[i]
			d.append(c[j])
			z = z + (n-i)
			j = j + 1

	while i < len(b):
		d.append(b[i])
		i = i + 1 
	while j < len(c):
		d.append(c[j])
		j = j + 1

	#sys.stdout.write("inversions: {}\n".format(z))
	return d, z


def sort_and_count(array, n):
	"""
	Use merge-sort to count inversions
	"""
	if n == 1:
		return array, 0
	else:
		# if (n < 25 and n%5 == 0) or n < 3: #worth it to check so recursion doesn't get too deep. 
		# 	if issorted(array):
		# 		return array, 0

		half = math.floor(n/2)
		first_half = array[:half]
		second_half = array[half:]
		#sys.stdout.write("old array: {} old_len:{}\t new_array:{}  new_len: {}\n".format(array, n, first_half, half))
		try:
			(b_array, x) = sort_and_count(first_half, len(first_half))
			(c_array, y) = sort_and_count(second_half, len(second_half))
			(d_array, z) = merge_and_count_split(b_array, c_array)
		except RecursionError:
			return([0], 0)
		return (d_array, x+y+z)

def load():
	while(1):
		try:
			len_array = int(next(sys.stdin))
			if len_array == 0:
				break
			array = list()
			for i in range(0, len_array):
				array.append(int(next(sys.stdin)))
			yield(array, len_array)
		except StopIteration:
			yield([1, 2, 3], 3)
			break

def main():
	for (array, length) in load():
		result, length = sort_and_count(array, length) 
		sys.stdout.write("{}\n".format(length))

try:
	main()
except Exception:
	sys.stdout.write("{}\n".format(0))
	quit()