price = float (input ("Введите цену товара: "))
k_vo = int (input ("Введите кол-во товара: "))
total = price * k_vo
print(f"сумма до скидки: {total}")

if total < 1000:
    discount = 0
elif total <= 5000:
    discount = 5
else:
    discount = 10

S_discount = total * discount / 100
total_after = total - S_discount

print (f"Размер скидки: {discount}")
print (f"Сумма скидки: {S_discount}")
print (f"Итоговая сумма: {total_after}")
