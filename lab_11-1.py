# Author: SCT (AMDG) 2/8/22

my_file = open("alma_mater.txt", "r")
while True:
     line = my_file.readline()
     if len(line) == 0:
           break
     print (line, end="")
     print(" ")
my_file.close()