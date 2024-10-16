from turtle import *
import fractales as frac

width(2)

S = frac.Sierpinski_triangle()

print(S)

del1 = 10
teta = 120

color('red')

for ss in S:
 if ss in ('F', 'G'):
  forward(del1)
 elif ss == '+':
  left(teta)
 else:
  right(teta)

mainloop()
