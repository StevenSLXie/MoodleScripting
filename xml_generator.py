from lxml import etree as e


def description_generator(file):
	with open(file) as f:
		lines = f.readlines()
		quiz = e.Element('quiz')

		i = 0
		while i < len(lines)-1:
			question = e.Element('question', type='description')
			name = e.Element('name')
			text = e.Element('text')
			text.text = cdata_wrapper('SL')
			name.append(text)
			question.append(name)
			questiontext = e.Element('questiontext', format="html")
			temp_text = lines[i]
			# print i,lines[i]
			i += 1
			while i< len(lines)-1 and not lines[i].count('item'):
				temp_text += lines[i]
				i += 1
			text = e.Element('text')
			text.text = cdata_wrapper(temp_text)

			questiontext.append(text)
			question.append(questiontext)
			quiz.append(question)

			if i >= len(lines)-1:
				break
			else:
				while lines[i] == '\n':
					i += 1


		s = e.tostring(quiz, pretty_print=True, encoding='UTF-8', xml_declaration=True)
		writer = open('data/x4_desc.xml', 'w')
		writer.writelines(s)
		# print s





def multiple_choice_generator(file):
	with open(file) as f:
		lines = f.readlines()
		#for l in lines:
		#	print l
		ans = find_answer(lines)

		quiz = e.Element('quiz')
		i = 0
		num = 0
		while True:
			question = e.Element('question', type='multichoice')
			name = e.Element('name')
			text = e.Element('text')
			text.text = cdata_wrapper(str(num+1))
			name.append(text)
			question.append(name)
			questiontext = e.Element('questiontext', format="html")
			text = e.Element('text')
			text.text = cdata_wrapper(lines[i].replace('questiontext: ', ''))
			questiontext.append(text)
			question.append(questiontext)
			print i, num, lines[i]
			i += 1
			print i, num, lines[i]
			while lines[i][0] >= 'A' and lines[i][0] <= 'F' and lines[i][1] == '.':
				if lines[i][0] == ans[num]:
					answer = e.Element('answer', fraction='100')
				else:
					answer = e.Element('answer', fraction='0')
				text = e.Element('text')
				text.text = cdata_wrapper(lines[i][2:])
				answer.append(text)
				question.append(answer)
				i += 1

			shuffleanswers = e.Element('shuffleanswers')
			shuffleanswers.text = 'true'
			answernumbering = e.Element('answernumbering')
			answernumbering.text = 'ABCD'
			question.append(shuffleanswers)
			question.append(answernumbering)
			while lines[i].count('hint'):
				# record hint, if any, if multiple
				hint = e.Element('hint')
				text = e.Element('text')
				text.text = cdata_wrapper(lines[i][7:])
				hint.append(text)
				question.append(hint)
				i += 1

			i += 1
			generalfeedback = e.Element('generalfeedback')
			text = e.Element('text')
			text.text = lines[i].replace('gfeed.', '')
			generalfeedback.append(text)

			question.append(generalfeedback)

			quiz.append(question)


			i += 1

			num += 1
			# while lines[i] == '\n':
			#	i += 1

			if i >= len(lines)-1:
				break
			else:
				while lines[i] == '\n':
					i += 1

		s = e.tostring(quiz, pretty_print=True, encoding='UTF-8', xml_declaration=True)
		writer = open('data/x4_mc.xml', 'w')
		writer.writelines(s)
		# print s


def cdata_wrapper(s):
	# return "<![CDATA[" + s + "]]>"
	# currently there is no need to use this, as we do not use HTML.
	return s


def find_answer(lines):
	answer = []
	for l in lines:
		if l.count('Answer:'):
			answer.append(l.replace('Answer:', '').replace('.\n', ''))
	# print answer
	return answer


multiple_choice_generator('data/x4_mc.txt')
description_generator('data/x4_desc.txt')


