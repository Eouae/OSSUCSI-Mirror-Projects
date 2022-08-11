import unittest
# __eq__
# (Node,Node) -> Bool
# sets the comparison conditions for two instances of a userdefined class

class Struct():
	def __init__(self,a,b):
		self.a=a
		self.b=b
	# 
# def __eq__(self,other):
# if type(self)!=type(other):return Falseelse:
# 	return self==other
# 		#Attribute list cannot be empty
# 		# if ls == []:
# 		# 	return (...)
# 		# else:
# # 		if not isinstance(othernode,Node):
# # 			return False
# # 		else:
# 		return (
# 			(...) if ls[0].(...)(...) else 
# 			fnForList(ls[1:]))
# 		return(
# 			)
Struct1 = Struct(None,None)
Struct2 = Struct(None,None)
Struct3 = Struct([None],None)










class Test(unittest.TestCase):
	def testBaseCase(self):
		self.assertEqual(Struct1,Struct1)
	def testEqual(self):
		self.assertEqual(Struct1,Struct2)
	def testNonEqual(self):
		self.assertEqual(Struct2,Struct3)


if __name__ == '__main__':
	unittest.main()