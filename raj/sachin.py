def my(a,func)
	c=func(a)
	return a*c
n=my(10,lambda d:d*d)
print(n)
class X:
	def __init__(self):
		print("Where are you")
	def m1(self):
		print("here i am")
	def r1(self):
		print("okay be there")
x=X()
x.m1()
x.r1()
