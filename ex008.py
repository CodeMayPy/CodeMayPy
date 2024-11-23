# Escreva um programa que leia um valor em metros e o exiba convertido em centímetro e milímetros.
m = int(input('Digite um valor em metros:'))
print(f'''Se o valor é {m}, convertendo ele:
{m/1000} km,
{m/100} Hm,
{m/10} Dam,
{m*10} Dm,
{m*100} Cm,
{m*1000} Mm.''')
