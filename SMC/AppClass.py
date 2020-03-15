import AppClass_sm

vocab = dict() #имя - ключ, тип - значение
class AppClass:
	def __init__(self):
		#self._conflict = False
		self._fsm = AppClass_sm.AppClass_sm(self)
		self._is_acceptable = False
		self._fsm.enterStartState()
		self._name = ''
		self._type = ''
		self._tmp_name = ''
		self._counter = 0
		self._lit_flag = False
		self._op_flag = False

	def Acceptable(self):
		self._is_acceptable = True

	def Unacceptable(self):
		self._is_acceptable = False

	def CheckString(self, string):
		self._fsm.start()
		for c in string:
			if c.isalpha():
				self._fsm.letter(c)
			elif c.isdigit():
				self._fsm.digit(c)
			elif c == ' ':
				self._fsm.space()
			elif c == '=':
				self._fsm.equal()
			elif c == '%' or c == '/' or c == '*':
				self._fsm.operation()
			elif c == '\n':
				self._fsm.EOS()
				break
			else:
				self._fsm.unknown()
		self._fsm.EOS()
		return self._is_acceptable

	def is_valid_type(self):
		return self._counter <= 5

	def check_type(self):
		return self._type == "int" or self._type == "short" or self._type == "long"

	def counter_inc(self):
		self._counter += 1

	def counter_zero(self):
		self._counter = 0

	def add_to_type_string(self, c):
		self._type += c

	def add_to_name_string(self, c):
		if self._lit_flag == False:
			self._name += c
		else:
			self._tmp_name += c

	def clear_tmp_name_string(self):
		self._tmp_name = ''

	def is_valid_name(self):
		return self._counter < 16

	def check_lit_flag_false(self):
		return not self._lit_flag

	def check_lit_flag_true(self):
		return self._lit_flag

	def set_lit_flag(self):
		self._lit_flag = True

	def check_op_flag_false(self):
		return not self._op_flag

	def check_op_flag_true(self):
		return self._op_flag

	def set_op_flag(self):
		self._op_flag = True

	def check_vocab(self):
		if self._tmp_name == self._name or self._tmp_name in vocab:
			return True
		else:
			return False

	def add_to_vocab(self):
		if not self._name in vocab:
			vocab[self._name] = self._type

	def check_conflicts(self):
		if self._name in vocab and self._type != vocab[self._name]:
			return self._name, vocab[self._name]
		else:
			return None

	def ClearSMC(self):
		self._is_acceptable = True
		self._name = ''
		self._type = ''
		self._tmp_name = ''
		self._counter = 0
		self._lit_flag = False
		self._op_flag = False

