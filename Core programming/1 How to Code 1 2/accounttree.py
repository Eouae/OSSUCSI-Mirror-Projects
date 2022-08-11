import unittest
import attribList
import dunderEqual

class Node:
	def __init__(self,id,name,bal,l,r):
		self.id=id
		self.name=name
		self.balance=bal
		self.leftaccounts=l
		self.rightaccounts=r
			
#Accounts is one of: 
# 	- False
# 	- Node(Natural,String,Integer,Accounts,Accounts)
# interp. a collection of bank accounts
# False represents an empty collection of bank accounts.
# Node(id,name,bal,l,r) is a nonempty collection of accounts such that
# 	- id is an account id number (and BST key)
# 	- name is the accountholder's name
# 	- bal is the account balance in CAD
# 	- l and r are further collections is accounts
# INVARIANT: for a given node:
# 	id > all id's in its left child; id < all id's in its right child
# 	the same id never appears twice in the tree

ACT0 = False
ACT1 = Node(1,"Mr. Rogers",22,False,False)
ACT4 = Node(4,"Mrs. Doubtfire",-3,False,Node(7,"Mr. Natural",13,False,False))
ACT3 = Node(3,"Miss Marple",600,ACT1,ACT4)
ACT42 = Node (42,"Mr. Mom",-79, 
			Node (27,"Mr. Selatcia",40, 
				Node(14,"Mr. Impossible",-9,False,False),
				False),
			Node (50,"Miss 604",16,False,False))
ACT10 = Node (10,"Dr. No", 84, ACT3, ACT42)

#Template
#  def fnForAct (act):
#  	return(
#  		(...)if act == False
#  		else
#  			(...)	act.id,						...such as Node()
#  					act.name,
#  					act.balance,
#  					fnForAct(act.leftaccounts),
#  					fnForAct(act.rightaccounts)	
#  		)

#__eq__
	def testBase(self):
		return self.assertEqual(ACT0==ACT0,True)
	def testACT0ACT1(self):
		return self.assertEqual(ACT0==ACT1,False)
	def testACT42True(self):
		return self.assertEqual(ACT42== 
		Node (42,"Mr. Mom",-79, 
			Node (27,"Mr. Selatcia",40, 
				Node(14,"Mr. Impossible",-9,False,False),
				False),
			Node (50,"Miss 604",16,False,False))
			,True)