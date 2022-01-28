class Human :
	def __init__(self, name, height, weight, mantra):
		self._name = name
		self._height = height
		self._weight = weight
		self._mantra = mantra
	def say_mantra(self):
		print(self._mantra)

Teacher = Human("Chen-Chia-Lee",160,60,"AAAAAAAA")
Teacher.say_mantra()
