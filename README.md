# SMTP-TESTER
[![Version](https://img.shields.io/badge/Version-1.0-brightgreen.svg?maxAge=259200)]()
[![Stage](https://img.shields.io/badge/Release-beta-green.svg)]()
[![Scripting](https://img.shields.io/badge/-%23!%2Fbin%2Fbash-1f425f.svg)]()
[![Scripting](https://img.shields.io/badge/-%23!%2Fbin%2Fpython-1f425f.svg)]()

SMTP Tester Email using the python module is smtplib [Read more](https://cpython-test-docs.readthedocs.io/en/latest/library/smtplib.html)


#### Usage 
```
$ cat list-smtp.txt
smtp.gmail.com|PORT|username@gmail.com|PASS
$ chmod +x run.sh
$ ./run.sh 
 # Input your list SMTP => list-smtp.txt
 # Input your email => youremail@outlook.com
```
#### Results 
```
$ cat Results/cat smtp_live.txt
SMTP WORKED [ smtp.gmail.com |PORT | username@gmail.com | PASS ]
SMTP WORKED [ smtp.zoho.com | PORT | domainx@domain.com | PASS ]
```
You can filter using the following command
```
$ cat Results/cat smtp_live.txt | cut -d '[' -f 2 | cut -d ']' -f 1
 smtp.gmail.com |PORT | username@gmail.com | PASS
 smtp.zoho.com | PORT | domainx@domain.com | PASS
```

Donate :

BTC : 35hoQ5QyEHYAgNw8C52vyD9jHkyyPTUNRg
