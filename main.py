#!/bin/python
# @author : shandpy <icq : @shandpy>
# @tested : Ubuntu 20.04
# @name : SMTP TESTER
#
import smtplib
import sys
def SENDe(HOST,PORT,USER,PASS,M_TO):
	try:
		HEADER = 'To:' + M_TO + '\n' + 'From: ' + USER + '\n' + 'MIME-Version: 1.0\n' + 'Content-Type: text/html; charset=UTF-8\n' + 'Content-Transfer-Encoding: 7bit\n' + 'X-Priority: 3\n' + 'Subject: SMTP Worked\n'
		MESS = HEADER + '\n<h3>SMTP Worked</h3> <a href="https://www.github.com/shandpy">Coded by SHandPY</a>'
		server = smtplib.SMTP(HOST,PORT,timeout=5)
		server.ehlo()
		server.starttls()
		server.ehlo()
		server.login(USER, PASS)
		server.sendmail(USER, M_TO, MESS)
		server.quit()
		print "SMTP WORKED [ " + HOST + " | " + PORT + " | " + USER + " | " + PASS + " ]"
		results = open("Results/smtp_live.txt","a")
		results.write("SMTP WORKED [ " + HOST + " | " + PORT + " | " + USER + " | " + PASS + " ]" + "\n")
		results.close()
	except Exception as e:
		print "SMTP NOT WORKED [ " + HOST + " | " + PORT + " | " + USER + " | " + PASS + " ]"
		results = open("Results/smtp_dead.txt","a")
		results.write("SMTP NOT WORKED [ " + HOST + " | " + PORT + " | " + USER + " | " + PASS + " ]" + "\n")
		results.close()

if __name__ == "__main__":
	HOST = sys.argv[1]
	PORT = sys.argv[2]
	USER = sys.argv[3]
	PASS = sys.argv[4]
	M_TO = sys.argv[5]
	SENDe(HOST,PORT,USER,PASS,M_TO)
