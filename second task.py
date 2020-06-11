number = int(input('Введите время в секундах: '))
hour = (number//3600)
minute = (number - hour * 3600)//60
seconde = number - (hour * 3600 + minute * 60)
print(f"{hour} : {minute} : {seconde}")