# Programa para calcular la nota definitiva de una asignaturaen la Especialidad de Sistemas.

print("-------------------------------------")
print("EL RESULTADO DE LAS OPERACIONES SON:-")
print("-------------------------------------")

# input
nc = int(input("Digite el valor de la nota cognitiva: ") )
np = int(input("Digite el valor de la nota procedimental: "))
na = int(input("Digite el valor de la nota actitudinal: "))
au = int(input("Digite el valor de la auto evaluacion: "))
bi = int(input("Digite el valor de la bimestral: "))

# proccesing

nd = (0.3*nc) + (0.3*np) + (0.1*na) + (0.1*au) + (0.2*bi)

# output

print("------------------------------")
print("----------RESULTADO-----------")
print("------------------------------")
print("NOTA DEFINITIVA " + str(nd))
