from turtle import *

S = 'X'
X = 'F+[[X]-X]-F[-FX]+X'
F = 'FF'

teta = 120
del1 = 1

niter = 6

k = 0
while k < niter:
 ss = ''
 for s in S:
  if s == 'X':
   ss = ss + X
  elif s == 'F':
   ss = ss + F
  else:
   ss = ss + s
 k = k+1
 S = ss

print(S)

del1 = 1
teta = 25

tt = []
for s in S:
# print(s)
 if s == 'F':
  forward(del1) 
 elif s == '[':
  w = pos()
  tt.append(w)
 elif s == ']':
  w = tt.pop()
  goto(w)
 elif s == '+':
  left(teta)
 elif s == '-':
  right(teta)
# print(tt)

mainloop()
