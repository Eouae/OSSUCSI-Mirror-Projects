import AccountClass

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
  			 
  			if act2 != False else act1
  			)