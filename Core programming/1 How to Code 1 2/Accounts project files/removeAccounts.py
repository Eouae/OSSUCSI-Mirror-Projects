import joinBranch
import AccountClass

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