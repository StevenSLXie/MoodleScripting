def preprocess(origin):
	# preprocess the original Latex file
	clean_lines = []

	with open(origin) as file:
		lines = file.readlines()
		for l in lines:
			if not is_formatting_line(l) and not is_empty_line(l):
				l = l.replace('Choice ', '')
				l = l.replace('~', '')
				#l = l.replace('hint 1:', 'feedback:')
				#l = l.replace('hint 2:', 'feedback:')
				l = l.replace('Feedback:', 'gfeed.')
				l = l.replace('\\vspace{.3cm}\\underline', '')
				clean_lines.append(l)
				if l.count('gfeed') or l.count('\\item'):
					clean_lines.append('\n')
	#for line in clean_lines:
	#	print line
	# print clean_lines
	return clean_lines


def is_formatting_line(line):
	words = ['\\input', '\\begin{document}', '\\end{document}', '\\thispage', 'itemize','wrongly']

	for w in words:
		if line.count(w):
			return True
	return False


def is_empty_line(line):
	line_is = ['', '\n']

	for l in line_is:
		if line == l:
			return True
	return False


def categorize(lines):
	# description
	desc = []
	# multiple-choice
	mc = []
	# numerical response
	num = []

	writer_mc = open('data/x4_mc.txt', 'w')
	writer_desc = open('data/x4_desc.txt', 'w')

	i = 0
	while True:
		if i >= len(lines)-1:
			break
		print i, lines[i]
		if lines[i].count('{subquestion}'):
			# sub-sequestion
			#print '1:'+str(i)
			if lines[i+1].count('multiple-choice'):
				mc.append('questiontext:' + lines[i].replace('{subquestion}:', ''))
				i += 2
				while lines[i] != '\n':
					mc.append(lines[i])
					i += 1
				mc.append('\n')
			else:
				i += 1
		elif lines[i].count('item'):
			#print '2:' + str(i)
			# description
			desc.append(lines[i])
			i += 1
			while not lines[i].count('item') and not lines[i].count('{subquestion}'):
				desc.append(lines[i])
				i += 1
			desc.append('\n')

		else:
			i += 1

	writer_mc.writelines(mc)
	writer_desc.writelines(desc)


clean_lines = preprocess('data/x4.txt')
categorize(clean_lines)


