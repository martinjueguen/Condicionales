print ("ingrese el año")
año=int(input())
if (año%4==0) or (año%400==0) and (año%100!=0):
    print("el año es bisiesto")
else:
    print("el año no es bisiesto")




