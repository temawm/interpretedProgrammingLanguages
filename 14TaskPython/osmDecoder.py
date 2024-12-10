import xml.etree.ElementTree as ET
import re
from collections import defaultdict

# Функция для извлечения времени открытия
def extract_opening_hour(opening_hours):
    match = re.search(r'(\d{1,2}):', opening_hours)
    return int(match.group(1)) if match else None

# Функция для извлечения ресторанов из OSM-файла
def extract_restaurants_with_hours_lxml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    restaurants = []
    for node in root.findall("node"):
        tags = {tag.attrib['k']: tag.attrib['v'] for tag in node.findall("tag")}
        if tags.get("amenity") == "restaurant" and "opening_hours" in tags:
            restaurants.append({
                "name": tags.get("name", "Unknown"),
                "opening_hours": tags["opening_hours"]
            })
    return restaurants

# Группировка ресторанов по времени открытия
def group_restaurants_by_opening_hour(restaurants):
    grouped = defaultdict(list)
    for restaurant in restaurants:
        opening_hour = extract_opening_hour(restaurant["opening_hours"])
        if opening_hour is not None:
            grouped[opening_hour].append(restaurant["name"])
    return grouped

# Загрузка и обработка данных
file1 = "12.osm"
file2 = "12 -2.osm"

restaurants_file1 = extract_restaurants_with_hours_lxml(file1)
restaurants_file2 = extract_restaurants_with_hours_lxml(file2)

# Группируем рестораны по времени открытия
grouped_file1 = group_restaurants_by_opening_hour(restaurants_file1)
grouped_file2 = group_restaurants_by_opening_hour(restaurants_file2)

# Объединяем данные
final_grouping = defaultdict(list, grouped_file1)
for hour, names in grouped_file2.items():
    final_grouping[hour].extend(names)

# Вывод результата
for hour, names in sorted(final_grouping.items()):
    print(f"{hour}:00 - {', '.join(names)}")
