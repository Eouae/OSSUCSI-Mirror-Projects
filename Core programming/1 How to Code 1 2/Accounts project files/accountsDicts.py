# (Accounts) -> Dict or False
# Return the dict of a given account or return False if account is False

def accountsDicts(act):
 	return(
		False if act == False
			else
			{"id":act.id,					
  			"name":act.name,
  			"balance":act.balance,
  			"leftaccounts":accountsDicts(act.leftaccounts),
  			"rightaccounts":accountsDicts(act.rightaccounts)}	
  		)	

#Testing
import unittest
import AccountClass

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

if __name__ == '__main__':
	unittest.main()
