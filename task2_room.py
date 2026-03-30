length = 7
width = 3.5
height = 3.2
S_floor = length * width
S_wall = length * height * 2 + width * height * 2
V = length * width * height
Cost = S_wall * 125
print(f"== ПАРАМЕТРЫ ПОМЕЩЕНИЯ ==\n"
      f"Длинна: {length}\n"
      f"Ширина: {width}\n"
      f"Высота: {height}\n"
      f"Площадь пола: {S_floor:.2f}\n"
      f"Площадь стен: {S_wall:.2f}\n"
      f"Объем: {V:.2f}\n"
      f"Стоимость: {Cost:.2f}\n")
