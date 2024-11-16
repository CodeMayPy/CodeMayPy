# Crie um programa que leia um número em metros e de seu valor em Km, hm, dam, dm, cm e mm.
m = int(input('Digite um valor em metros:'.strip()))
print(f'''Se o valor é {m}, convertendo ele:
{m*1000} km,
{m*100} Hm,
{m*10} Dam,
{m/10} Dm,
{m/100} Cm,
{m/1000} Mm.''')
