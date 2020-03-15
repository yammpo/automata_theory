import AppClass
import sys
import time

def from_file():
	recognizer = AppClass.AppClass()
	f = open('generated_1000.txt', 'r')
	res = open('results.txt', 'w')
	start = time.time()
	for line in f.readlines():
		match = recognizer.CheckString(line)
		if match:
			res.write(line + ' OK ')
			check = recognizer.check_conflicts()
			if check is not None:
				res.write('conflict: ' + check[0] + ' initial type is ' + check[1] + '\n')
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
	recognizer = AppClass.AppClass()
	for line in sys.stdin:
		match = recognizer.CheckString(line[:-1])
		if match:
			print('OK')
			check = recognizer.check_conflicts()
			if check is not None:
				print('conflict: ' + check[0] + ' initial type is ' + check[1])
			
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

