a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
if (a+b<=c or b+c<=a or c+a<=b):
  print("no")
else:
  print("yes")
