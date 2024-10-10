#Simple
a=33
b=200

if b>a:
    print(b,"es mayor que: ",a)

#Doble
c=200
d=333

if c>d:
    print(c,"es mayor que: ",d)
else:
    print(d,"no es mayor que: ",c)

#Multiple

e=200
f=200

if e>f:
    print(e,"es mayor que: ",f)
elif e<f:
    print(e,"es ,menor que: ",f)
else:
    print(e,"es igual que: ",f)


x=28

if x>10:
    print("Por encima de diez,")
    if x<20:
        print("y tambien por encima de 20!")
    else:
        print("pero no por encima de 20.")


print("Estudiar los sabados ",end='')
print("es genial")

#print("Estudiar los sabados")
#print("es genial")

print("Daniela","Luis","Carlos","Camila") #agrega un espacio por defecto
print("Daniela","Luis","Carlos","Camila",sep="")#quita el espacio
print("Daniela","Luis","Carlos","Camila",sep=",")#agrega una coma

print("Daniela","Luis","Carlos","Camila",sep="_",end='_Curso_python')#Implementacion de end y sep