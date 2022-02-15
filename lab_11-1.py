# Author: SCT (AMDG) 2/8/22

my_file = open("alma_mater.txt", "r")  # opens text file

while True: # creates while loop
      line = my_file.readline()  # stores info in file as variable 'line'
      if len(line) == 0:  # if no more lines end loop
           break
      print (line, end="")  # prints the lines from file
      print(" ")  # adds space inbetween each line
my_file.close()  # closes the file
