materials = {
    "Стекло": 500,
    "Железобетон": 1500,
    "Газобетон": 1000,
    "Керамзитобетон": 1200,
    "Стекловата": 700
}
print ("Список:", materials)

materials["Кирпич"] = 1100
materials["Дерево"] = 900
print ("Обновленный список:", materials)

materials["Кирпич"] *= 1.10

del materials["Стекло"]

print("Итог:", materials)
print("Средняя цена:", sum(materials.values()) / len(materials))
