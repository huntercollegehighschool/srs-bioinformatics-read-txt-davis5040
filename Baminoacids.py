"""
Define a function weightedstring that takes a string input protein. The function returns the weighted string of that protein based on masstable.txt.

weightedstring should read from masstable.txt. It's helpful to have those masses in a dictionary.
"""

def weightedstring(protein):
  fstream = open("masstable.txt", 'r')
  contents = fstream.readlines()
  dic = {}
  d = 0
  cur = 'A'
  for line in contents:
    for c in line.split():
      #print(c)
      #print(d)
      #print(cur)
      if d == 1:
        dic[cur] = c
        d = 0
      else:
        cur = c
        d = 1
  ans = 0
  for x in protein:
    k = dic[x]
    intk = float(k)
    ans = ans + intk
  print(ans)