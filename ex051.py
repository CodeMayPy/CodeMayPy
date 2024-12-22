#Develop a program that reads the first term and the ratio of an AP. At the end, show the first 10 terms
# of this progression.
first = int(input('First term:'))
ratio = int(input('Ratio:'))
tenth = first +(10-1) * ratio
for c in range(first,tenth + ratio, ratio):
    print(f'{c}', end=' -> ')
print('He finished')
