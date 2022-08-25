# Node -> Bool
# Determine whether the account balance is negative

def negativeBool(act):
 	return(
 		False if act == False
 		else
 			True if act.balance < 0 else False	
 		)
	
	
#Testing
import unittest
import AccountClass

class Test(unittest.TestCase):
	def testBase(self):
		return self.assertEqual(negativeBool(AccountClass.ACT0),False)
	def testACT4(self):
		return self.assertEqual(negativeBool(AccountClass.ACT4),True)
	def testACT1(self):
		return self.assertEqual(negativeBool(AccountClass.ACT1),False)
if __name__ == '__main__':
	unittest.main()
