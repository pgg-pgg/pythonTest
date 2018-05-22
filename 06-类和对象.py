class SweetPotato:
	
	def __init__(self):
		self.cookedString="生的"
		self.cookedLevel=0
	
	def cook(self,cooked_time):
		if cooked_time>=0 and cooked_time<3:
			self.cookedString="生的"
		elif cooked_time>=3 and cooked_time<5:
			self.cookedString="半生不熟"
		elif cooked_time>=5 and cooked_time<8:
			self.cookedString="熟了"
		elif cooked_time>9:
			self.cookedString="糊了"
	
	def __str__(self):
		return "地瓜 状态：%s(%d)"%(self.cookedString,self.cookedLevel)


class A(SweetPotato):
	def test(self):
		print("sda")

di_gua=SweetPotato()

di_gua.cook(1)
print(di_gua)
