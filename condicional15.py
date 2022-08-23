x=int(input("ingrese un numero entre el 0 y el 10"))
par_Impar={
0: "par",1: "impar",2: "par",3: "impar",4:"par",5: "impar",6:"par",7: "impar",8:"par",9: "impar",10:"par",}
print(par_Impar.get(x,"numero fuera de rango"))