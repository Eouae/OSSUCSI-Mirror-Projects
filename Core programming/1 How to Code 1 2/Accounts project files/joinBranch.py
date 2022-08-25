# (Accounts,Accounts) -> Accounts
# Join one account at first empty leftmost node of the second 
# all id's in act1 < those in act2, thus act1 will join at the leftmost free node of act2

def joinBranch(act1,act2):
	return(
  		AccountClass.Node(
  		act2.id,
  		act2.name,
  		act2.balance,
  		joinBranch(act1,act2.leftaccounts),
  		act2.rightaccounts)
  			 
  			if act2 != False else act1)

#Testing
import unittest
import AccountClass
import accountsDicts

class Test(unittest.TestCase):

	def testBase(self):
		accounts1 = AccountClass.ACT42
		return self.assertEqual(accountsDicts.accountsDicts(joinBranch(accounts1,False)),accountsDicts.accountsDicts(accounts1))
		
	def testBaseReverse(self):
		accounts1 = AccountClass.ACT42
		return self.assertEqual(
			accountsDicts.accountsDicts(joinBranch(False,accounts1)),accountsDicts.accountsDicts(accounts1))
	
	def testACT1andACT4(self):
		accounts2 = AccountClass.ACT1
		accounts3 = AccountClass.ACT4
		return self.assertEqual(accountsDicts.accountsDicts(joinBranch(accounts2,accounts3)),
									accountsDicts.accountsDicts(AccountClass.Node(4,"Mrs. Doubtfire",-3,accounts2,
											AccountClass.Node(
												7,"Mr. Natural",13,False,False)
										))												
								)
	def testACT4andACT1(self):
		accounts2 = AccountClass.ACT1
		accounts3 = AccountClass.ACT4
		return self.assertEqual(accountsDicts.accountsDicts(joinBranch(accounts3,accounts2)),accountsDicts.accountsDicts(AccountClass.Node(1,"Mr. Rogers",22,AccountClass.Node(4,"Mrs. Doubtfire",-3,False,AccountClass.Node(7,"Mr. Natural",13,False,False)),False)))

if __name__ == '__main__':
	unittest.main()