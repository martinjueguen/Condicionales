A=int(input("ingrese A: "));
B=int(input("ingrese B: "));
C=int(input("ingrese C: "));
if A>B and A>C:
    if B>C:
        print(A,B,C)
    else:
        print(A,C,B)

if B>A and B>C:
    if A>C:
        print(B,A,C)
    else:
        print(B,C,A)

if C>B and C>A:
    if B>A:
        print(C,B,A)
    else:
        print(C,A,B)