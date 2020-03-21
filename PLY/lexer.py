import ply.lex as lex
import re

class Lexer():

	states = (
		('literal', 'exclusive'),
	)
	# чтобы после '=' воспринимались литералы, а не имена
	tokens = (
		'TYPE', 'EQUAL', 'NAME', 'LITERAL', 'OPERATION', 'NL'
	# равно и пробел куда запихнуть?
	)
	t_ignore = ''

	def t_TYPE(self, t):
		r'^(?:int|short|long)[ ]'
		return t

	def t_literal_EQUAL(self, t):
		r'='
		return t

	def t_NAME(self, t):
		r'[a-zA-Z][a-zA-Z0-9]{0,15}'
		t.lexer.begin('literal')
		return t

	def t_literal_LITERAL(self, t):
		r'(?:[a-zA-Z][a-zA-Z0-9]{0,15}) | (?:[0-9]+)'
		return t

	def t_literal_OPERATION(self, t):
		r'%|\*|/'
		return t

	def t_literal_NL(self, t):
		r'\n'
		t.lexer.lineno += len(t.value)
		t.lexer.begin('INITIAL')
		return t

	def t_ANY_error(self, t):
		#print("Illegal character '%s'" % t.value[0])
		t.lexer.skip(1)
		t.lexer.begin('INITIAL')
		return t

	def input(self, data):
        	return self.lexer.input(data)

	def token(self):
		return self.lexer.token()

	def __init__(self):
		self.lexer = lex.lex(module=self)

#lexer = Lexer()
#lexer.input(input())
#for tok in lexer.lexer:
#	print(tok)
	
	




