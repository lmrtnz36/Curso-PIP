Peso = input("Ingrese su peso:")
peso_total = int(Peso) 

Altura = input("Ingrese su altura:")
altura_total = float(Altura)

imc = peso_total / altura_total**2

print("Tu indice de masa corporal:",imc)