#faça um programa que leia a largura e altura de uma parede em metos,calcule sua área
# e a quantidade de tinta necessária para pinta-lá,sabendo que a cada litro de tinta,
#pinta uma área de 2m²
larg = float(input("qual largura da parede: "))
alt = float(input("qual altura da parede:  "))
are = (alt * larg)
print("sua parede tem uma dimensão {} x {} e sua área é: {} m²".format(larg,alt,are))
tinta = (are / 2)
print("para pintar essaa parede você precisará de {} litros de tinta".format(tinta))