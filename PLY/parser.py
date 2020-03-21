import ply.yacc as yacc
from lexer import Lexer
import sys
from ply.lex import LexError
import re
import generator
import time

class Parser():

	tokens = Lexer.tokens

	def __init__(self):
		self._lexer = Lexer()
		self._parser = yacc.yacc(module=self)
		self._from_file = False
		self._vocab = dict() #имя - ключ, тип - значение

	def set_from_file(self):
		self._from_file = True
		self._res = open('results.txt', 'w')

	#def set_from_console(self):
	#	self._from_file = False

	def check_string(self, s):
		try:
			res = self._parser.parse(s)
			return res
		except LexError:
			if self._from_file == False:
				sys.stderr.write('NOT OK') # вроде даже не вызывается
			else:
				self._res.write('NOT OK' + '\n')

	def check_lit(self, p, i):
		check_letters = re.search(r'\D', p[i]) # проверяем есть ли что-то кроме цифры
		if check_letters is None or p[i] == p[2] or p[i] in self._vocab:
			return True
		else:
			return False
			
	def check_vocab_long(self, p):
		if self.check_lit(p, 4) and self.check_lit(p, 6):
			if not p[2] in self._vocab:
				self._vocab[p[2]] = p[1]
			return True
		else:
			return False

	def check_vocab_short(self, p):
		if self.check_lit(p, 4):
			if not p[2] in self._vocab:
				self._vocab[p[2]] = p[1]
			return True
		else:
			return False

	def check_conflicts(self, p):
		if self._vocab[p[2]] != p[1]:
			return True
		else:
			return False

	# либо длинная строка либо короткая - первое правило
	# мб как-то 'string : TYPE NAME EQUAL LITERAL NL | OPERATION LITERAL NL'

	def p_string(self, p):
		'''string : long_string
		| short_string'''
		p[0] = p[1]

	def p_long_string(self, p):
		'long_string : TYPE NAME EQUAL LITERAL OPERATION LITERAL NL'
		p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6]
		if self._from_file == False:
			if p[0] is not None and self.check_vocab_long(p):
				print('OK')
				if self.check_conflicts(p):
					print('conflict: ' + p[2] + ' initial type is ' + self._vocab[p[2]])
			else:
				print('NOT OK')
		else:
			if p[0] is not None and self.check_vocab_long(p):
				self._res.write('OK ')
				if self.check_conflicts(p):
					self._res.write('conflict: ' + p[2] + ' initial type is ' + self._vocab[p[2]] + '\n')
				else:
					self._res.write('\n')
			else:
				self._res.write('NOT OK' + '\n')

	def p_short_string(self, p):
		'short_string : TYPE NAME EQUAL LITERAL NL'
		#print (p[2])
		p[0] = p[1] + p[2] + p[3] + p[4]
		if self._from_file == False:
			if p[0] is not None and self.check_vocab_short(p):
				print('OK')
				if self.check_conflicts(p):
					print('conflict: ' + p[2] + ' initial type is ' + self._vocab[p[2]])
			else:
				print('NOT OK')
		else:
			if p[0] is not None and self.check_vocab_short(p):
				self._res.write('OK ')
				if self.check_conflicts(p):
					self._res.write('conflict: ' + p[2] + ' initial type is ' + self._vocab[p[2]] + '\n')
				else:
					self._res.write('\n')
			else:
				self._res.write('NOT OK' + '\n')

	def p_error(self, p):
		if self._from_file == False:
			print('NOT OK')
		else:
			self._res.write('NOT OK' + '\n')

def from_file():
	f = open('generated_10000.txt', 'r')
	start = time.time()
	for line in f.readlines():
		parser._res.write(line)
		parser.check_string(line)
	end = time.time()
	with open('time.txt', 'w') as f:
		f.write(str(end-start))

parser = Parser()
print('which text to recognize?(f - from file, c - from consol)')
flag = input()
if flag == 'f':
	parser.set_from_file()
	print('generate new file or use early generated?(n - new, o - old)')
	flag_two = input()
	if flag_two == 'n':
		detector = generator.Generator()
		detector.full_the_names()
		detector.generate('generated_10000.txt', 10000)
		from_file()
	elif flag_two == 'o':
		from_file()
	else:
		print('error input, try again')

elif flag == 'c':
	for line in sys.stdin: # Ctrl + D to stop
		parser.check_string(line)
else:
	print('error input, try again')



