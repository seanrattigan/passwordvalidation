# Insert complete file header here.
# Use http://pep8online.com/ to check PEP8

import sha256
import length
import lower
import num
# declare variable password as data-type string
password = ""

def inputpass(password = input("Please enter a password: ")):
	return password


#def printpassword(password):
#	passwords = inputpass()
#	print(f"Your password is : {passwords}")
tests = [length.password_len, 
          lower.check_lwr,
          num.num_check]


password = inputpass()
# sha256.hashpass(password)
for test in tests:
    if test(password):
        print(f"Passed {test}")
    else:
        print(f"Failed Test: {test}")

