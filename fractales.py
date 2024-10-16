def Sierpinski_triangle():
 S = 'F-G-G'

 F = 'F-G+F+G-F' 
 G = 'GG'

 teta = 120
 del1 = 20

 niter = 5

 k = 0
 while k < niter:
  ss = ''
  for s in S:
   if s == 'F':
    ss = ss + F
   elif s == 'G':
    ss = ss + G
   else:
    ss = ss + s
  k = k+1
  S = ss

 return S


def dragon_curve():
 S = 'F'

 F = 'F+G'
 G = 'F-G'

 teta = 90
 del1 = 20

 niter = 5

 k = 0
 while k < niter:
  ss = ''
  for s in S:
   if s == 'F':
    ss = ss + F
   elif s == 'G':
    ss = ss + G
   else:
    ss = ss + s
  k = k+1
  S = ss

 return S


def fractal_plant():
 S = 'X'
 X = 'F+[[X]-X]-F[-FX]+X'
 F = 'FF'

 

