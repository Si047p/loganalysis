# Log Analysis

Description
The code is written in Python3.5.  It accesses a sql database and provides answers to 3 provided questions.  The project is designed to test understanding of using postgresql to retrieve filter and/or calculated data from  database tables.

Requirements
PostgreSQL
Pythno3  3.5
Vagrant
VirtualBox

Database Set-Up
Install VirtualBox
Install Vagrant
Use the following configuration file https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f73b_vagrantfile/vagrantfile
newsdata.sql database is required.
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

Running command
With the database properly setup
Start vagrant using vagrant up
Log into vagrant using vagrant ssh
change directory into folder containing loganlaysis.py
Type python3 loganalysis.py to run
When the command is run it will provide the response to the following 3 questions about the news database.
1. Most popular articles in the database of all time
2. Most popular article authors of all time
3. Any days where more than 1% of requests lead to errors.
