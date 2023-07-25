#escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
metros = float(input("digite a medida em metros: "))
km = metros / 1000
hk = metros / 100
dam = metros / 10
m = metros
cm = metros * 10
dec =metros * 100
mm = metros * 1000
print(' A MEDIDA EM KM METROS = {} HK EM METROS = {} DAM EM METROS = {}  '.format(km,hk,dam))
print(" A MEDIDA  EM METROS É = {}".format(m))
print("A MEDIDA EM CM EM METROS É = {} DEC EM METROS É = {} E  MM EM METROS É = {} ".format(cm,dec,mm))
