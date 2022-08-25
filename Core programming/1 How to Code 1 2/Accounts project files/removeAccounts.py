import joinBranch

# Abstract "removeActs"
# (Accounts -> Bool),Accounts -> Accounts
# Remove accounts that satisfy a given predicate

def removeActs(pred,act):
	return(
 		act if act == False 
 		else
 			joinBranch.joinBranch(removeActs(pred,act.leftaccounts),
 				removeActs(pred,act.rightaccounts))
 				if pred(act)
 		else
 			AccountClass.Node(act.id,act.name,act.balance,
 				removeActs(pred,act.leftaccounts),
 				removeActs(pred,act.rightaccounts))
 			)
 			
#Testing
import unittest
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