print("ingrese el sueldo del trabajador")
s=int(input())
if s<1000:
  s= ((15*s)/100)+s

print (s)