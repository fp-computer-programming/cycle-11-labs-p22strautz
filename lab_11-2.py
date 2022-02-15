# Author: SCT (AMDG) 2/8/22

my_file = open("alma_mater.txt", "r")  # Opens file
while True:  # creates while loop
      lines = my_file.readlines()  # stores info in file as variable 'line'
      for lines in reversed(lines):  # reverses each lines order
            print(lines)  # prints the lines in the new order
