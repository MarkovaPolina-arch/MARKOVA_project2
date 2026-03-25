warehouse = {
    "Кирпич": {"quantity": 5000, "price": 12.50, "min_quantity": 1000},
    "Цемент": {"quantity": 120, "price": 450.00, "min_quantity": 50},
    "Песок": {"quantity": 8, "price": 800.00, "min_quantity": 10},
    "Арматура": {"quantity": 30, "price": 48000.00, "min_quantity": 20},
    "Бетон": {"quantity": 45, "price": 4200.00, "min_quantity": 15}
}

print("=" * 80)
print("СИСТЕМА УЧЁТА СКЛАДА")
print("=" * 80)


print("\nМатериал | Кол-во | Цена | Мин. | Стоимость")
print("-" * 80)

total_cost = 0  
most_expensive = None  
max_price = 0  
critical_items = []  

for material, data in warehouse.items():
    quantity = data["quantity"]
    price = data["price"]
    min_qty = data["min_quantity"]
    cost = quantity * price  
    
    total_cost += cost  
    
    if price > max_price:
        max_price = price
        most_expensive = material
    
    is_critical = quantity < min_qty
    if is_critical:
        critical_items.append({
            "material": material,
            "quantity": quantity,
            "min": min_qty
        })
    

    line = f"{material} | {quantity} | {price:.2f} | {min_qty} | {cost:.2f}"
    if is_critical:
        line += " КРИТИЧ!"
    
    print(line)

print("\n" + "=" * 80)
print(f"ОБЩАЯ СТОИМОСТЬ: {total_cost:.2f} руб")
print(f"Самый дорогой: {most_expensive} ({max_price:.2f} руб)")

if critical_items:
    print(f"\n КРИТИЧЕСКИЕ ОСТАТКИ ({len(critical_items)}):")
    for item in critical_items:
        print(f"  - {item['material']}: {item['quantity']} < {item['min']}")

print("\n=== ВЫДАЧА МАТЕРИАЛА ===")

material_to_issue = "Цемент"
quantity_to_issue = 25

if material_to_issue in warehouse:
    current_qty = warehouse[material_to_issue]["quantity"]
    

    if current_qty >= quantity_to_issue:
        
        warehouse[material_to_issue]["quantity"] -= quantity_to_issue
        new_qty = warehouse[material_to_issue]["quantity"]
        
        print(f" Выдано {quantity_to_issue} единиц '{material_to_issue}'")
        print(f" Остаток: {current_qty} → {new_qty}")
    else:
        print(f" Недостаточно '{material_to_issue}' на складе!")
        print(f" Требуется: {quantity_to_issue}, есть: {current_qty}")
else:
    print(f" Материал '{material_to_issue}' не найден!")