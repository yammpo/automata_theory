import string
from random import choice, randint

names = []  #пустой список
for _ in range(50):  
	s1 = ''.join(choice(string.ascii_letters))
	s2 = ''.join(choice(string.ascii_letters + string.digits) for _ in range(randint(0,15)))
	names.append(s1 + s2)

def correct_name():
	tmp1 = ''.join(choice(string.ascii_letters))
	tmp2 = ''.join(choice(string.ascii_letters + string.digits) for _ in range(randint(0,15)))
	return (tmp1 + tmp2)

def error_name():
	tmp1 = ''.join(choice(string.digits))
	tmp2 = ''.join(choice(string.ascii_letters + string.digits) for _ in range(randint(0,15)))
	return (tmp1 + tmp2)

def dig():
	return (''.join(choice(string.digits) for _ in range(randint(1,15))))

def name_from_names():
	return choice(names)

def str_one():
	s1 = choice(('int ', 'short ', 'long '))
	rand_func_1 = choice((name_from_names, correct_name, error_name))
	s2 = rand_func_1()
	rand_func_2 = choice((name_from_names, correct_name, dig))
	s3 = rand_func_2()
	return (s1 + s2 + '=' + s3 + '\n')

def str_two():
	s1 = choice(('int ', 'short ', 'long '))
	rand_func_1 = choice((name_from_names, correct_name, error_name))
	s2 = rand_func_1()
	rand_func_2 = choice((name_from_names, correct_name, dig))
	s3 = rand_func_2()
	s4 = choice(('%', '*', '/'))
	rand_func_3 = choice((name_from_names, correct_name, dig))
	s5 = rand_func_3()
	return (s1 + s2 + '=' + s3 + s4 + s5 + '\n')

with open('generated.txt', 'w') as f:
	for _ in range(1000000):
		rand_func = choice((str_one, str_two))
		s = rand_func()
		f.write(s)
f.close()
for i in range(len(names)):
    print(i, names[i])


