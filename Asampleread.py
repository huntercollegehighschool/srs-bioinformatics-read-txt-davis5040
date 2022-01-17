"""
Write a program (doesn't have to be a function, but can be) that reads what's in sample.txt and prints it to the console.
"""
fstream = open("sample.txt", 'r')
line = fstream.readline()
while line:
  print(line);
  line = fstream.readline()

fstream.close()