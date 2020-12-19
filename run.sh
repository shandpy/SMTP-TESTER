#!/bin/bash
# @author : shandpy
# @tested : Ubuntu 20.04
# @name : SMTP TESTER
# cat smtp_live.txt | cut -d '[' -f 2 | cut -d ']' -f 1
mkdir -p Results
read -p " # Input your list SMTP => " LIST
read -p " # Input your email => " EMAIL
clear 
for SMTP in $(cat $LIST);
do
	HOST=$(echo $SMTP | cut -d '|' -f 1)
	PORT=$(echo $SMTP | cut -d '|' -f 2)
	USER=$(echo $SMTP | cut -d '|' -f 3)
	PASS=$(echo $SMTP | cut -d '|' -f 4)
	python main.py $HOST $PORT $USER $PASS $EMAIL
done
