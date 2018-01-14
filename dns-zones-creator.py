#!/usr/bin/pythonimport

#This imports the data listed in a csv file, and correcctly formats it ready for the forward and reverse zone files.
#   #This was inspried by Mike O'Leary in the book "Cyber Operations..." and the script is basically his with minor mods and notes by myself, but was worth learning

#   #Pay especially to the reverse naming syntax for the reverse files, essentially is the address backwards followed by '.in-addr.arpa.' including the trailing period
    #Zone files can be named as desired, but as outlined in your named.conf file, created in the BIND install

#Don't forget to look over the results, and as well, create a loopback zone as needed (e.g. for names like 'localhost')


#By the way, comments in python using """ multi-line comment """ are actually just strings headed for garbage collection :)!
    #Thinkaboutit



#
#----------------------------- example input file-------
#This script reads from a file, here scan.csv, which contains a list of host/results formatted as below (remove leading hash and tabs):
#   Host1,192.168.100.101
#   Host2,192.168.100.1
#   Host3,172.12.1.2
#--------------------------------------------------------

#define your variable setup
#Note that with some planning or in cetain setups, the forward and reverse files could also be correctly named here

input_file_name = "scan.csv"           #Main line-separated file of hostname,ip address for each hosts
forward_file_name = "forward.txt"
reverse_file_name = "reverse.txt"
domain_name = ".desired.domain."       #don't forget the trailing . after the end of the fqdn

# data preparation
# pulls in data ready for import below, open command
input_file = open(input_file_name,'r')
forward_file = open(forward_file_name,'w')
reverse_file = open(reverse_file_name,'w')


#Calls module input_reader and loads csv import using the 
input_reader = csv.reader(input_file)

#Here the files are formatted correctly for forward and reverse zones, showing pythons text processing ease
for line in input_reader:   
    host = line[0]
     ip = line[1]
     fqdn = host +  domain_name
     padding = ' ' * (30 - len(fqdn))
     forward_file.write(fqdn + padding + 'IN A     ' + ip + '\n')
     [i1,i2,i3,i4] = ip.split('.')
     revaddr = i4 + '.' + i3 + '.' + i2 + '.' + i1 + '.in-addr.arpa.'
     padding = ' ' * (30 - len(revaddr))
     reverse_file.write(revaddr + padding + 'IN PTR   ' + fqdn + '\n')
