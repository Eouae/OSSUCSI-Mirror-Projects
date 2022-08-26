import unittest
import AccountClass

import accountsDicts
import joinBranch
import negativeBool
import removeAccounts
import removeDebtors


class Test(unittest.TestCase):

	#accountsDicts
	def testDictsBase(self):
		return self.assertEqual(accountsDicts.accountsDicts(AccountClass.ACT0),False)
	def testDictsIdentity(self):
		return self.assertEqual(accountsDicts.accountsDicts(AccountClass.ACT1),AccountClass.ACT1.__dict__)
	def testDictsIdentityDict(self):
		return self.assertEqual(accountsDicts.accountsDicts(AccountClass.ACT1),
		{'id': 1, 'name': 'Mr. Rogers', 'balance': 22, 'leftaccounts': False, 'rightaccounts': False})
	def testDictsACT4(self):
		return self.assertEqual(accountsDicts.accountsDicts(AccountClass.ACT4), {'id': 4, 'name': 'Mrs. Doubtfire', 'balance': -3, 'leftaccounts': False, 'rightaccounts': {'id': 7, 'name': 'Mr. Natural', 'balance': 13, 'leftaccounts': False, 'rightaccounts': False}})
	
	#joinBranch
	def testJoinBase(self):
		accounts1 = AccountClass.ACT42
		return self.assertEqual(accountsDicts.accountsDicts(joinBranch.joinBranch(accounts1,False)),accountsDicts.accountsDicts(accounts1))
		
	def testJoinBaseReverse(self):
		accounts1 = AccountClass.ACT42
		return self.assertEqual(
			accountsDicts.accountsDicts(joinBranch.joinBranch(False,accounts1)),accountsDicts.accountsDicts(accounts1))
	
	def testJoinACT1andACT4(self):
		accounts2 = AccountClass.ACT1
		accounts3 = AccountClass.ACT4
		return self.assertEqual(accountsDicts.accountsDicts(joinBranch.joinBranch(accounts2,accounts3)),
									accountsDicts.accountsDicts(AccountClass.Node(4,"Mrs. Doubtfire",-3,accounts2,
											AccountClass.Node(
												7,"Mr. Natural",13,False,False)))												
								)
	def testJoinACT4andACT1(self):
		accounts2 = AccountClass.ACT1
		accounts3 = AccountClass.ACT4
		return self.assertEqual(accountsDicts.accountsDicts(joinBranch.joinBranch(accounts3,accounts2)),accountsDicts.accountsDicts(AccountClass.Node(1,"Mr. Rogers",22,AccountClass.Node(4,"Mrs. Doubtfire",-3,False,AccountClass.Node(7,"Mr. Natural",13,False,False)),False)))

#negativeBool
	def testNegBase(self):
		return self.assertEqual(negativeBool.negativeBool(AccountClass.ACT0),False)
	def testNegACT4(self):
		return self.assertEqual(negativeBool.negativeBool(AccountClass.ACT4),True)
	def testNegACT1(self):
		return self.assertEqual(negativeBool.negativeBool(AccountClass.ACT1),False)

#removeAccounts
	def testRemAccountsBase(self):
		return self.assertEqual(removeAccounts.removeActs(negativeBool.negativeBool,AccountClass.ACT0),AccountClass.ACT0)
	def testRemAccountsBaseIden(self):
		return self.assertEqual(removeAccounts.removeActs(negativeBool.negativeBool,AccountClass.ACT0),False)
	def testRemAccountsACT4(self):
		return self.assertEqual(accountsDicts.accountsDicts(removeAccounts.removeActs(negativeBool.negativeBool,AccountClass.ACT4)),accountsDicts.accountsDicts(AccountClass.ACT4.rightaccounts))
	def testRemAccountsACT1(self):
		return self.assertEqual(accountsDicts.accountsDicts(removeAccounts.removeActs(negativeBool.negativeBool,AccountClass.ACT1)),accountsDicts.accountsDicts(AccountClass.ACT1))

if __name__ == '__main__':
	unittest.main()

