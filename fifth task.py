income = int(input('Введите выручку компании: '))
costs = int(input('Введите издержки компании: '))
profit = int(income - costs)
profitability = int(profit / income * 100)
if income > costs:
    print(f'Компания отработала с прибылью, которая составила: {profitability} процентов')
    quantity = int(input('Введите количество сотрудников: '))
    print(f'Прибыль в расчете на одного сотрудника составила: {profit / quantity}')
else:
    print('Компания отработала с убытком! ')
