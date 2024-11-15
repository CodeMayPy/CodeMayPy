print('-=-' * 20)
print('Analisador de triângulos...')
print('-=-' * 20)
r1 =  float(input('Primeiro segmento:'))
r2 = float(input('Segundo seguimento:'))
r3 = float(input('Terceiro segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar um triângulo.')
else:
    print('Os seguimentos acima NÂO PODEM formar triângulo.')
