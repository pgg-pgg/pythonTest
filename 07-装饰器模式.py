def w1(func):
	def inner():
		print("正在验证权限。。")
		if True:
			func()
		else:
			print("没有权限")
	return inner

@w1
def f1():
	print("===F1")


@w1
def f2():
	print("====f2")

f1()
f2()
