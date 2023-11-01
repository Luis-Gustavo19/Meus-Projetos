valor = int(input("Informe o valor a ser sacado: "))
cedulas = [50, 20, 10, 1]

print("\nSerão entregues:")
for cedula in cedulas:
    quantidade = valor // cedula
    if quantidade > 0:
        print(f"{quantidade} cédulas de R${cedula}")
        valor = valor % cedula
