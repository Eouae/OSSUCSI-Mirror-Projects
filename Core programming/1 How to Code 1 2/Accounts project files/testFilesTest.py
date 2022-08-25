
import unittest
import AccountClass
import accountsDicts

class Test(unittest.TestCase):
	def testBase(self):
		return self.assertEqual(accountsDicts(AccountClass.ACT0),False)
	def testIdentity(self):
		return self.assertEqual(accountsDicts(AccountClass.ACT1),AccountClass.ACT1.__dict__)
	def testIdentityDict(self):
		return self.assertEqual(accountsDicts(AccountClass.ACT1),
		{'id': 1, 'name': 'Mr. Rogers', 'balance': 22, 'leftaccounts': False, 'rightaccounts': False})
	
	def testACT4(self):
		return self.assertEqual(accountsDicts(AccountClass.ACT4), {'id': 4, 'name': 'Mrs. Doubtfire', 'balance': -3, 'leftaccounts': False, 'rightaccounts': {'id': 7, 'name': 'Mr. Natural', 'balance': 13, 'leftaccounts': False, 'rightaccounts': False}})

import negativeBool
import AccountClass
import accountsDicts

class Test(unittest.TestCase):
	def testBase(self):
		return self.assertEqual(removeActs(negativeBool.negativeBool,AccountClass.ACT0),AccountClass.ACT0)
	def testBaseIden(self):
		return self.assertEqual(removeActs(negativeBool.negativeBool,AccountClass.ACT0),False)
	def testACT4(self):
		return self.assertEqual(accountsDicts.accountsDicts(removeActs(negativeBool.negativeBool,AccountClass.ACT4)),accountsDicts.accountsDicts(AccountClass.ACT4.rightaccounts))
	def testACT1(self):
		return self.assertEqual(accountsDicts.accountsDicts(removeActs(negativeBool.negativeBool,AccountClass.ACT1)),accountsDicts.accountsDicts(AccountClass.ACT1))


if __name__ == '__main__':
	unittest.main()

