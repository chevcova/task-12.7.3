per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = input("Введите сумму:")
deposit1= int(per_cent['ТКБ'] * int(money) / 100)
deposit2= int(per_cent['СКБ'] * int(money) / 100)
deposit3= int(per_cent['ВТБ'] * int(money) / 100)
deposit4= int(per_cent['СБЕР'] * int(money) / 100)
list_desposit=[deposit1, deposit2,deposit3, deposit4]
print(list_desposit)

print("Максимальная сумма, которую вы можете заработать — [%i]" % max(list_desposit))
