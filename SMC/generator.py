import string
from random import choice, randint

class Generator:
	def __init__(self):
		self._names = []  #пустой список

	def full_the_names(self):
		for _ in range(50):  
			s1 = ''.join(choice(string.ascii_letters))
			s2 = ''.join(choice(string.ascii_letters + string.digits) for _ in range(randint(0,15)))
			self._names.append(s1 + s2)

	def correct_name(self):
		tmp1 = ''.join(choice(string.ascii_letters))
		tmp2 = ''.join(choice(string.ascii_letters + string.digits) for _ in range(randint(0,15)))
		return (tmp1 + tmp2)

	def error_name(self):
		tmp1 = ''.join(choice(string.digits))
		tmp2 = ''.join(choice(string.ascii_letters + string.digits) for _ in range(randint(0,15)))
		return (tmp1 + tmp2)

	def dig(self):
		return (''.join(choice(string.digits) for _ in range(randint(1,15))))

	def name_from_names(self):
		return choice(self._names)

	def str_one(self):
		s1 = choice(('int ', 'short ', 'long '))
		rand_func_1 = choice((self.name_from_names, self.correct_name, self.error_name))
		s2 = rand_func_1()
		rand_func_2 = choice((self.name_from_names, self.correct_name, self.dig))
		s3 = rand_func_2()
		return (s1 + s2 + '=' + s3 + '\n')

	def str_two(self):
		s1 = choice(('int ', 'short ', 'long '))
		rand_func_1 = choice((self.name_from_names, self.correct_name, self.error_name))
		s2 = rand_func_1()
		rand_func_2 = choice((self.name_from_names, self.correct_name, self.dig))
		s3 = rand_func_2()
		s4 = choice(('%', '*', '/'))
		rand_func_3 = choice((self.name_from_names, self.correct_name, self.dig))
		s5 = rand_func_3()
		return (s1 + s2 + '=' + s3 + s4 + s5 + '\n')

	def generate(self, file_name, number):#file_name string, number int
		with open(file_name, 'w') as f:
			for _ in range(number):
				rand_func = choice((self.str_one, self.str_two))
				s = rand_func()
				f.write(s)
		f.close()

	def show_names(self):
		for i in range(len(self._names)):
    			print(i, self._names[i])

#detector = Generator()
#detector.full_the_names()
#detector.generate('generated_1000.txt', 1000)
#detector.show_names()



