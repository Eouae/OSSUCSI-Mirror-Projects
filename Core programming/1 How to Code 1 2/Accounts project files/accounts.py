import unittest
from AccountClass import *
import debtorBool
import joinBranch

# Abstract "removeActs"
# (Accounts -> Bool),Accounts -> Accounts
# Remove accounts that satisfy the pred predicate

def removeActs(predStr,act):
	return(
 		act if act == False 
 		else
 			joinBranch (removeActs(predStr,act.leftaccounts),
 				removeActs(predStr,act.rightaccounts))
 				if predStr(act) == True
 		else
 			Node(act.id,act.name,act.balance,
 				removeActs(predStr,act.leftaccounts),
 				removeActs(predStr,act.rightaccounts))
 			)

#Testing
class Test(unittest.TestCase):
	#removeActs
	#base case - test on the account "False"
	def testRemoveActsbase(self):
		def trueBool(act):
			return True
		self.assertEqual(removeActs(trueBool,False), False)
	#test on ACT42
	def testRemoveACT42(self):
		def trueBool(act):
			return True
		self.assertEqual(removeActs(trueBool,ACT42), False)
	#test on ACT42, not removed
	def testNoRemoveACT42(self):
		def falseBool(act):
			return False
		self.assertEqual(removeActs(falseBool,ACT42), ACT42)
	#test on debtor account, removed
	def testRemoveDebtor(self):
		self.assertEqual(
		removeActs(debtorBool,
				Node(4,"Mrs.Doubtfire",-3,False,
					Node(7,"Mr. Natural",13,False,False))), 
		Node(7,"Mr. Natural",13,False,False))
		
		

if __name__ == '__main__':
	unittest.main()