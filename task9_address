import re

addresses = [
    "  г. Москва, ул. Ленина, д. 10  ",
    "г.Казань,ул.Баумана,д.15",
    "  г. Санкт-Петербург, ул. Невский, д. 100  "
]

print("=== СРАВНЕНИЕ ===")

for i, address in enumerate(addresses, 1):
    original = address
    
    address = address.strip()
    
    address = re.sub(r'(г\.|ул\.|д\.)(?!\s)', r'\1 ', address)
    
    address = re.sub(r',\s*', ', ', address)
    
    address = re.sub(r'\s+', ' ', address)
    
    address = address.strip()
    
    print(f"#{i}")
    print(f"ДО: '{original}'")
    print(f"ПОСЛЕ: '{address}'")
    print()
    