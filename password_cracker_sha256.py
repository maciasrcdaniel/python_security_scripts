#!/usr/bin/env python3

# Import pwn module and sys modules
from pwn import *
import sys

# Verify the input is 1 as an arguement
if len(sys.argv) != 2:
	print("Invalid Arguement")
	print(">> {} <sha256sum>".format(sys.argv[0]))
	exit()

# Assign the coverted input has to a variable
required_hash = sys.argv[1]
# Include the path or password file
password_file = "rockyou.txt"
attempts = 0

# Place holder for progress
with log.progress("Attempting to crack: {}!\n".format(required_hash)) as p:
	# Open the password file
	with open(password_file, "r", encoding='latin-1') as password_lists:
		# Iterate through all the passwords in the rockyou.txt file
		for password in password_lists:
			# Strip the password and remove new line
			password = password.strip("\n").encode('latin-1')
			# Convert all the passwords to sha256 hex format
			new_password_hash = sha256sumhex(password)
			# Print out the number of attempts, the decoded password and the decoded password sha256
			p.status("[{}] {} == {}".format(attempts, password.decode('latin-1'), new_password_hash))

			# If statement to verify the hashes match
			if new_password_hash == required_hash:
				p.success("Password hash found. It took {} attempts. Password hash {} lines up with {}".format(attempts, new_password_hash, password.decode('latin-1')))
				# Exit the program
				exit()
			# Increment attempts variable by 1
			attempts += 1 
		# Log the password failure
		p.failure("Password not found.")