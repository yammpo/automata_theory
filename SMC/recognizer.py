import AppClass

recognizer = AppClass.AppClass()
f = open('generated_1000.txt', 'r')
res = open('results.txt', 'w')
for line in f.readlines():
	match = recognizer.CheckString(line)
	if match:
		res.write(line + ' OK ')
		check = recognizer.check_conflicts()
		if check is not None:
			res.write(check[0] + ' initial type is ' + check[1] + '\n')
		else:
			res.write('\n')
	else:
		res.write(line + ' NOT OK ' + '\n')
f.close()
