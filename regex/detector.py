import re
import sys
import time

vocab = dict() #имя - ключ, тип - значение

tmpl_name = r'([a-zA-Z][a-zA-Z0-9]{0,15})'
tmpl_lit = r'(?:' + tmpl_name + r'|(?:[0-9]+))'

#'^(int|short|long)[ ][a-zA-Z][a-zA-Z0-9]{0,15}[=](([a-zA-Z]{1}[a-zA-Z0-9])|([0-9]+))(%|(\*)|/)(?=(([a-zA-Z]{1}[a-zA-Z0-9])|([0-9]+)))$\n'

#positive lookahead кажется не получится использовать, т.к. он не принимает последующую часть, а мне надо чтоб принимал

tmpl = r'^(int|short|long)[ ]' + tmpl_name + r'[=]' + tmpl_lit + r'(?:(?:(?:%|\*|/)' + tmpl_lit + r')|$)'

def check_lit(rex, i):
	if rex[i] is None or rex[i] == rex[2] or rex[i] in vocab:
		return True
	else:
		return False

def check_vocab(rex):
	if check_lit(rex, 3) and check_lit(rex, 4):
		if not rex[2] in vocab:
			vocab[rex[2]] = rex[1]
		return True
	else:
		return False

def check_conflicts(rex):
	if vocab[rex[2]] != rex[1]:
		return True
	else:
		return False

def from_file():
	f = open('generated_1000.txt', 'r')
	res = open('results.txt', 'w')
	start = time.time()
	for line in f.readlines():
		rex = re.fullmatch(tmpl, line[:-1])
		if rex is not None and check_vocab(rex):
			res.write(line + ' OK ')
			if check_conflicts(rex):
				res.write('conflict: ' + rex[2] + ' initial type is ' + vocab[rex[2]] + '\n')
			else:
				res.write('\n')
		else:
			res.write(line + ' NOT OK ' + '\n')
	end = time.time()
	with open('time.txt', 'w') as tm:
		tm.write(str(end-start))
	f.close()
	
def from_console():# Ctrl + D to stop
	start = time.time()
	for line in sys.stdin:
		rex = re.fullmatch(tmpl, line[:-1])
		if rex is not None and check_vocab(rex):
			print('OK')
			if check_conflicts(rex):
				print('conflict: ' + rex[2] + ' initial type is ' + vocab[rex[2]])
		else:
			print('NOT OK')
	end = time.time()
	with open('time.txt', 'w') as f:
		f.write(str(end-start))

print('which text to recognize?(f - from file, c - from consol)')
flag = input()
if flag == 'f':
	from_file()
elif flag == 'c':
	from_console()
else:
	print('error input, try again')
	
