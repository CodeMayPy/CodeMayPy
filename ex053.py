# Create a program that reads any sentence and says if it is a palindrome, disregarding spaces. Examples of
# palindromes:
# AFTER THE SOUP, THE BALCONY OF THE HOUSE, THE TOWER OF DEFEAT, THE WOLF LOVES THE CAKE, THEY WROTE DOWN THE DATE
# OF THE MARATHON.
sentence = str(input('Enter a sentence:')).strip().upper()
words = sentence.split()
together = ''.join(words)
reverse = ''
for words in range(len(together)-1, -1, -1):
    reverse += together[words]
print(f'The reverse of {together} is {reverse}.')
if reverse == together:
    print('We have a palindrome.')
else:
    print('The sentence is not a palindrome.')
