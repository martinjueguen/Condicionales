

print("ingrese los valores")
N=int(input("Tipo de calculo: "))
V=int(input("ingrese V: "))
funcion={
1:100*V,
2:100**V,
3:100/V
}
VAL = funcion.get(N,0);
print(VAL)