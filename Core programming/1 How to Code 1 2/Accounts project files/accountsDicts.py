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