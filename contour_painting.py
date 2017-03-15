import sys

def paint_after_first(line):
	new_line = ""
	painted = False
	seen_nonwhite = False
	for char in line:
		if char == ' ' :
			if seen_nonwhite == True and painted == False:
				new_line = new_line + '#'
				painted = True
			else:
				new_line = new_line + char
		else:
			new_line = new_line + char
			seen_nonwhite = True

	
	return(new_line)


def cont(new_line):
	try:
		first_char = new_line[0]
	except IndexError:
		first_char = " "
	if first_char != '_':
		return True
	else:
		return False		


def load(num_cases):
	for i in range(0, num_cases):
		lines = list()
		star_found = False
		new_line = next(sys.stdin).strip('\n')
		lines.append(new_line)		
		contin = cont(new_line)
		while (contin):
			new_line = list(next(sys.stdin).strip('\n'))
			if star_found:
				new_line = paint_after_first(new_line)
				print("".join(new_line))
				#new_line = paint(new_line, side)
				 
			lines.append(new_line)
			if '*' in new_line:
				# check if inside or outside
				# modify previous lines. 
				print("".join(new_line))
				star_found = True
				#side = 0 # inside
			# 	open_contour = False
			# 	for char in new_line:
			# 		if char == '*' and open_contour == False:
			# 			side = 'INSIDE'
			# 		elif char == '*' and open_contour == True: 
			# 			side = 'OUTSIDE'
			# 		elif char != ' ' and open_contour == False:
			# 			open_contour = True
			# 		elif char != ' ' and open_contour == True:
			# 			open_contour = False	

			contin=cont(new_line)

		yield(lines)

def main():
	num_cases = int(next(sys.stdin))
	for (grid) in load(num_cases):
		for g in grid:
			print("".join(g))
		print("\n")

main()