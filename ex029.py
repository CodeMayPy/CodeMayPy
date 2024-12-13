# Write a program that reads the speed of a car. If it exceeded 80km/h, show a message saying that it
# was fined. The fine will cost R$7.00 for each km above the limit.
speed = float(input('Enter the speed of your car:'))
if speed > 80:
    print('FINED!!!! You have exceeded the 80Km/h limit.')
    fined = (speed - 80) * 7
    print(f'You will need for a fine of R${fined}.')
print(f'Have a nice day! Drive safely!')
