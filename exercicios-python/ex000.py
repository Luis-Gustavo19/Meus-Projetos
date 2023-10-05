nota1 = float(input("digite sua nota da ap1: "))
nota2 = float(input("digite sua nota da ap2: "))
media = float( (nota1 + nota2) /2)
print("sua média foi: %s"%(media))
if (media >=7):
    print("parabéns, você passou =P")
elif (media <=6.9):
    print("sinto muito,você está de recuperação =c")
cadastrar = str(input("deseja cadastrar outra nota ? Responda com ''s ou n'' "))

