"""
function test
"""


# !/usr/bin/python3



def enroll(name, gender, age, city='Shanghai'):
	"""
	function enroll
	:param name: 名字
	:param gender: 性别
	:param age: 年龄
	:param city: 默认参数 shanghai
	"""
	# 参数检查
	if not isinstance(age, (int, float)):
		# 抛出类型错误
		raise TypeError('bad operand type')
	print('name:', name)
	print('gender:', gender)
	print('age:', age)
	print('city:', city)


def sums(*numbers):
	"""
	:param numbers: 可变参数 numbers
	:return:
	"""
	sum = 0
	for n in numbers:
		sum = sum + n
	return sum


def person(name, age, **kw):
	"""
	:param name:
	:param age:
	:param kw:
	:return:
	"""
	if 'city' in kw:
		# 有city参数
		pass
	if 'job' in kw:
		# 有job参数
		pass
	print('name:', name, 'age:', age, 'other:', kw)


def cat(name, age, *color, sound="meow!"):
	"""
	命名参数
	:param name:
	:param age:
	:param color:
	:param sound:
	:return:
	"""
	if not isinstance(age, (int, float)):
		raise ValueError('wrong argument')
	print("name: ", name)
	print("age: ", age)

	if isinstance(color, list):
		for i in color:
			print("color: ", i)
	else:
		print("color: ", color)

	print(sound)

enroll("Art2cat", 'male', 3)
listA = [1, 2, 3]
print(sums(*listA))
print(sums(1, 2, 1, 3, 4))

person('Art2cat', 3, city='Shanghai', time='adg')

cat("囧爷", 3, *['black', 'white'])
cat("囧爷", 3, 'white', sound="wang!")
