def func(functionName):
	def func_in(*args,**kwargs):
		ret=functionName()
		return ret
	return func_in


@func
def test():
	print("----test---")
	return "haha"

@func
def test2():
	print("---test2---")

@func
def test3(a):
	print("---test3 %s"%a)

ret=test()
	print("---test3 %s"%ret)

