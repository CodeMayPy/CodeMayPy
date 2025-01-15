#Analyzing Triangles v2.0
#42- Redo triangle challenge 35, adding the feature of showing what type of triangle will be formed:
# – EQUILATERAL: all sides equal
# – ISOSCELES: two sides equal, one different
# – SCALENE: all sides different
'''first_segment = float(input('Enter thr first segment:'))
second_segment = float(input('Enter the second segment:'))
tirdh_segment = float(input('Enter the tirdh segment:'))
if first_segment < second_segment + tirdh_segment and second_segment < first_segment + tirdh_segment and tirdh_segment < first_segment + second_segment:
    print('The segments above CAN form a triangle!', end=' ')
    if first_segment == second_segment == tirdh_segment:
        print('Equilateral!')
    elif first_segment != second_segment != tirdh_segment != first_segment:
        print('Scalene!')
    else:
        print('Isosceles.')
else:
    print('The segments above CAN NOT form a triangle!.')'''


#Analisando Triângulos v2.0
#42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
# ESCALENO: todos os lados diferentes
primeiro = float(input('Qual o primeiro valor?'))
segundo = float(input('Qual o segundo valor?'))
terceiro = float(input('Qual o terceiro valor?'))
if primeiro < segundo + terceiro and segundo < primeiro + terceiro and terceiro < primeiro + segundo:
    print('Os dadod informados podem formar um triângulo, ' ,end=' ')
    if primeiro == segundo == terceiro:
        print('Equilátero.')
    elif primeiro != segundo != terceiro != primeiro:
        print('Escaleno')
    else:
        print('isósceles.')
else:
    print('Os dados informados não formaram um triângulo.')


#PT- Condições aninhadas.
#EN- Aligned conditions.