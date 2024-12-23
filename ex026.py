#26- Write a program that reads a sentence from the keyboard and shows how many times the letter "a" appears and in what position it is
# appears the first time and in what position it appears last time.
sentence = input('Enter a sentence:').upper()
print(f'The letter A shows {sentence.count('A')} times.')
print(f'The first letter A shows in position {sentence.find('A')+1}.')
print(f'The last letter A shows in position {sentence.rfind('A')+1}.')
