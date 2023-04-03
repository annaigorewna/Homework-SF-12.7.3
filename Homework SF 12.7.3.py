per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму, которую планируете положить на вклад: '))
deposit = []
for i in per_cent:
    print('Накопленные средства в банке {} за год - '.format(i), int(per_cent[i] * money/100), 'руб.')
    deposit.append(per_cent[i] * money / 100)
print()
deposit_max = max(deposit)
print('Максимальная сумма, которую вы можете заработать - '+ str(int(deposit_max)), 'руб.')
