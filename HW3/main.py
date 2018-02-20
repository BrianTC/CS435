#!/usr/bin/python3
"""
	Brian Chickey
	For CS 435 02
	2.19.18
"""

import sys
import Stack 

'''
Check chars, add to stack if char is ({[< then recurse
othwerwise check if the next character is )}]> closing brace and if it is
check if it matches to what is on top of the stack, then remove that from the stack
if it doesnt match then its an error. 
return sucess/error
'''

testString="(<((()))>)"
stk=Stack.Stack()
openers='({[<'
closers=')}]>'
def validateString(string):
	if(len(string)==0):
		if(not stk.empty()):
			return False
		return True

	if(string[0] in openers):
		stk.push(string[0])

	elif(string[0] in closers):
		if(stk.empty()):
			return False
		curIdx=closers.find(string[0])
		stacksIdx='({[<'.find(stk.pop())
		if(curIdx!=stacksIdx):
			return False

	return validateString(string[1:])

'''
#actually running the program
'''	

print("Enter a series of parens to validate their order: ")
for line in sys.stdin:
	if(line=="no\n"):
		break

	if(validateString(line)):
		print("Well formed: "+line)
	else:
		print("Ill-formed: "+line)
	stk.clear()
	print("Enter annother? (type no to end)")



"""
Here a set of tests I used to test this if you want to pipe them in
( )(( )){([(< >)])}
<((( )(( )){([( )])}))>
)(( )){([( )])}
({[ ])}
<(>
()))
(<{{}}>)(((){})[][]{{}[]})
(strings dont affect it)
(<{{}}>)((({})[][]{{}[]})
no
"""
