#!/usr/bin/env python3
## Moving files with SFTP

## import paramiko so we can talk SSH
import paramiko
import os

# t = paramiko.Transport("10.10.2.3", 22) ## IP and port

## how to connect (see other labs on using id_rsa private/public keypairs)
# t.connect(username="bender", password="alta3")

""" Customization Request 01 """

ip = input('Target IP: ') # Enter target IP address

t = paramiko.Transport(ip, 22) 

un = input('Username: ')  # Enter username
pw = input('Password: ')  # Enter password

t.connect(username=un, password=pw)

sftp = paramiko.SFTPClient.from_transport(t)
""" End of Customization Request 01 """

## Make an sftp connection object
# sftp = paramiko.SFTPClient.from_transport(t)

## iterate across the files within directory
for x in os.listdir("/home/student/filestocopy/"): # iterate on directory contents
  if not os.path.isdir("/home/student/filestocopy/"+x): # filter everything that is NOT a directory
    sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x) # move file to target location

## close the connection
sftp.close() # close the connection

