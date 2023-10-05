#crie um rpograma que leia o comprimento do cateto oposto e do adjacente de um triângulo retângulo e mostre
# o comprimento da hipotenusa
#formula = a²= b²+c² a=hipotenusa
'''co =float(input("digite o comprimento do cateto oposto: "))
adj =  float(input("digite o comprimento do cateto adjacente: "))
hipot =  co**2 + adj**2
raizhipot = hipot**(1/2)
print("\n O comprimento da hipotenusa é:{:.2f}".format(raizhipot))'''
import math
co = float(input("Digite o comprimento do cateto oposto: "))
adj = float(input("diigte o comprimento do cateto adjacente: "))
hipo = math.hypot(co,adj)
print('A hipotenusa dos catetos digitados são: {:.2f} '.format(hipo))