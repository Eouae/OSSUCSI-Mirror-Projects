# import unittest
# from AccountClass import *

# (Accounts,Accounts) -> Accounts
# Join one account at first empty leftmost node of the second 
# all id's in act1 < those in act2, thus act1 will join at the leftmost free node of act2

def joinBranch(act1,act2):
	return(
  		Node(
  			act2.id,
  			act2.name,
  			act2.balance,
  			joinBranch(act1,act2.leftaccounts),
  			act2.rightaccounts)
  			 
  			if act2 != False else act1)


class Test(unittest.TestCase):
	def testBase(self):
		return self.assertEqual(accountsDicts(joinBranch(ACT42,False)),accountsDicts(ACT42))
		
	def testBaseReverse(self):
		return self.assertEqual(
			accountsDicts(joinBranch(False,ACT42)),accountsDicts(ACT42))
	
	def testACT1andACT4(self):
		return self.assertEqual(accountsDicts(joinBranch(ACT1,ACT4)),
									accountsDicts(Node(4,"Mrs. Doubtfire",-3,ACT1,
											Node(
												7,"Mr. Natural",13,False,False)
										))												
								)
	def testACT4andACT1(self):
		return self.assertEqual(accountsDicts(joinBranch(ACT4,ACT1)),accountsDicts(Node(1,"Mr. Rogers",22,Node(4,"Mrs. Doubtfire",-3,False,Node(7,"Mr. Natural",13,False,False)),False)))

if __name__ == '__main__':
	unittest.main()