class Test(object):

	def __init__(self):
		self._a = 10
		self.__b = 20


if __name__ == '__main__':
	t = Test()
	print(t._a)  # ok
	print(t.__dict__)  # ok
	print(t.__b)  # error


"""
单下划线：不能通过from module import *导入，其他和公有一样访问。
双下划线：无法直接像公有成员一样随便访问，通过对象名._类名__xxx这样访问
"""