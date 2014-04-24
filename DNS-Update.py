#!/usr/bin/python

import urllib2
import os.path

OLDIP_FILE = '/var/lib/misc/oldip' #hard coded file path as global variable

def updatedns(ip): #function to update the DNS & file
    print urllib2.urlopen("xxxxxxxx").read().strip() #Open the website to register DNS .read() reads file, .strip() removes leading and trailing whitespace
    f = open(OLDIP_FILE, 'w') #Open file as writable
    f.write(ip) # write the value of IP address to the file
    f.close() # Close the file

newip = urllib2.urlopen("http://ip.dnsexit.com/").read().strip() #Gets IP address from this website - this function runs first!!

if not os.path.exists(OLDIP_FILE): # Check if file doesn't (not) exists, if not, create it
    updatedns(newip) # Calls the updatedns function
else:
    f = open(OLDIP_FILE, 'r') # Opens the file to read only
    oldip = f.read() # Reads IP address contained within
    f.close() # Closes file
    if oldip != newip: # compares the values
        updatedns(newip) # calls updatedns function using the newip address as the variable
