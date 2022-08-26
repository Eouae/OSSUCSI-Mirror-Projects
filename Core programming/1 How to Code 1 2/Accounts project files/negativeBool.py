# Node -> Bool
# Determine whether the account balance is negative

def negativeBool(act):
 	return(
 		False if act == False
 		else
 			True if act.balance < 0 else False	
 		)