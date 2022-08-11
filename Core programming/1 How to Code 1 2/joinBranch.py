import unittest
from accounttree import *

# "joinbranch"
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
		return self.assertEqual(joinBranch(ACT42,False),ACT42)
		
	def testBaseReverse(self):
		return self.assertEqual(joinBranch(False,ACT42),ACT42)
	
	def testACT1andACT4(self):
		return self.assertEqual(joinBranch(ACT1,ACT4),
									Node(4,"Mrs. Doubtfire",-3,ACT1,
											Node(
												7,"Mr. Natural",13,False,False)
										)												
								)
	def testACT3andACT42(self):
		return self.assertEqual(joinBranch(ACT3,ACT42),
									Node (42,"Mr. Mom",-79,
										Node (27,"Mr. Selatcia",40,
											Node(14,"Mr. Impossible",-9,False,False),
											False),
										Node (50, "Miss 604",16,
											#ACT3 starts here
											Node (3,"Miss Marple", 600,
												#ACT1
												Node (1, "Mr. Rogers",22,False,False),
												#ACT4
												Node (4,"Mrs. Doubtfire",-3,False,
													Node (7,"Mr. Natural",13,False,False)
													 )
													),
												False)	
											)
								#Assertion 
								)

if __name__ == '__main__':
	unittest.main()