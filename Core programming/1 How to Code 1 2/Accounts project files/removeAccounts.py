import unittest
from AccountClass import *
import predBool

# Abstract "removeActs"
# (Accounts -> Bool),Accounts -> Accounts
# Remove accounts that satisfy the pred predicate

def removeActs(predBool,act):
	return(
 		act if act == False 
 		else
 			joinBranch (removeActs(predBool,act.leftaccounts),
 				removeActs(predBool,act.rightaccounts))
 				if predBool(act) == True
 		else
 			Node(act.id,act.name,act.balance,
 				removeActs(predBool,act.leftaccounts),
 				removeActs(predBool,act.rightaccounts))
 			)

#Testing
class Test(unittest.TestCase):
	#removeActs
	#base case - test on the account "False"
	def testRemoveActsbase(self):
		self.assertEqual(removeActs(True,False), False)
	#test on ACT42
	def testRemoveACT42(self):
		self.assertEqual(removeActs(True,ACT42), False)
	#test on ACT42, not removed
	def testNoRemoveACT42(self):
		self.assertEqual(removeActs(False,ACT42), ACT42)
	#test on debtor account, removed
	def testRemoveDebtor(self):
		self.assertEqual(
		removeActs(debtorBool,
				Node(4,"Mrs.Doubtfire",-3,False,
					Node(7,"Mr. Natural",13,False,False))), 
		Node(7,"Mr. Natural",13,False,False))
		
		

if __name__ == '__main__':
	unittest.main()