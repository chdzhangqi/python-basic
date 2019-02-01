"""
python中的三元运算符不同于a>b?a:b，格式为:a if a > b else b

"""

if __name__ == '__main__':
	"""求两个数的最大值"""

	a = input("请输入第一个整数:")
	b = input("请输入第二个整数:")

	res = a if a > b else b
	print(res)

