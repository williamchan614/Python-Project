import copy
from queue import *
import sys
import numpy as np


def check_semigroup(L):
  hashmap = {}

  first = L[0]
  second = L[1]
  q = Queue(0)
  count = 2
  # hash right away
  for matrix in L:
    v = hash(str(matrix))
    if v in hashmap:
      vv = hashmap[v]
      vv.append(matrix)
      hashmap[v] = matrix
    else:
      hashmap[v] = [matrix]

  for matrix in L:
    q.put(matrix)

  while (not q.empty()):
    A = q.get()
    for matrix in L:
      B = A.dot(matrix)
      if not ((B > -3).all() and (B < 3).all()):
        return None

      hashed = hash(str(B))

      if hashed in hashmap:
        # it could already be in there
        found = False
        allHashed = hashmap[hashed]

        for every in allHashed:
          if (B == every).all():
            found = True
            break
        if (not found):
          hashmap[hashed] = allHashed.append(B)
          count += 1
          q.put(B)
      else:
        hashmap[hashed] = [B]
        count += 1
        q.put(B)

  print("this semigroup is finite and is has " + str(count) + " elements")

  file = open("log.txt", "a")
  file.write("----------------------\n")
  file.write("current queue size:" + str(q.qsize()) + " elements\n")
  file.write("this semigroup is finite\n")
  file.write("current size:" + str(count) + " elements\nA:\n")
  file.write(str(first))
  file.write(str("\nB:\n"))
  file.write(str(second))
  file.write("\n")
  file.close()

  return count


L = [np.matrix('0 0 0 0 0;'
               ' 1 1 1 1 1;'
               '0 0 0 0 0;'
               ' 1 1 1 1 1;'
               '0 0 0 0 0'),

     np.matrix('0 0 0 0 0;'
               '-1 -1 -1 -1 -1;'
               '0 0 0 0 0;'
               '-1 -1 -1 -1 -1;'
               '0 0 0 0 0')]

'''




[[ 1  0  0 -1  0]
 [ 0  0  0  1  0]
 [ 0  0  0  1 -1]
 [ 0  0 -1  0  0]
 [ 0 -1  0  0  0]]
 
[[ 0  1 -1  0  0]
 [-1 -1  0  0  0]
 [-1 -1  0  0  0]
 [ 0  0 -1  0  0]
 [-1  0 -1  0  1]]
'''

check_semigroup(L)

P = copy.deepcopy(L[:])
N = copy.deepcopy(P[:])
prevSize = 0
failed = 0
while (prevSize < 100000):

  newSize = check_semigroup(N)
  if (newSize == None or newSize <= prevSize):  # did not improve / no progress
    #print("Skipped")
    failed += 1
    if failed > 15:
      N = copy.deepcopy(P[:])
      kevin = np.random.randint(low=8, high=25, size=1)[0]
      for i in range(kevin):
        r = np.random.randint(50, size=1)[0]
        t = np.random.randint(3, size=1)[0]
        if 0 <= r and r <= 24:
          row = r // 5
          colum = r % 5
          N[0][row, colum] = t - 1
        else:
          r = r - 25
          row = r // 5
          colum = r % 5
          N[1][row, colum] = t - 1
    else:
      r = np.random.randint(50, size=1)[0]
      t = np.random.randint(3, size=1)[0]
      N = copy.deepcopy(P[:])
      if 0 <= r and r <= 24:
        row = r // 5
        colum = r % 5
        N[0][row, colum] = t - 1
      else:
        r = r - 25
        row = r // 5
        colum = r % 5
        N[1][row, colum] = t - 1


  else:  # it did improve
    prevSize = newSize
    failed = 0
    print(prevSize)
    P = copy.deepcopy(N[:])
    r = np.random.randint(50, size=1)[0]
    t = np.random.randint(3, size=1)[0]
    if 0 <= r and r <= 24:
      row = r // 5
      colum = r % 5
      N[0][row, colum] = t - 1
    else:
      r = r - 25
      row = r // 5
      colum = r % 5
      N[1][row, colum] = t - 1
    file = open("log.txt", "a")
    file.write("----------------------\n")
    file.write(str(P[0]))
    file.write("\n")
    file.write(str(P[1]))
    file.write("\n")
    file.write(str(prevSize))
    file.write("\n")
    file.close()

for each in P:
  print(each)