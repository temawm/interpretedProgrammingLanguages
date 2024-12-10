import csv
import re


def read_csv(file_path):
    with open(file_path, encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data


# Конвертация времени в секунды
def convert_time(time_str):
    match_hours = re.match(r"(\d+) ч. (\d+) мин.", time_str)
    if match_hours:
        hours = int(match_hours[1])
        minutes = int(match_hours[2])
        return hours * 3600 + minutes * 60

    match_minutes = re.match(r"(\d+) мин. (\d+) сек.", time_str)
    if match_minutes:
        minutes = int(match_minutes[1])
        seconds = int(match_minutes[2])
        return minutes * 60 + seconds

    return 0


# Преобразование времени из секунд в строку "мин:сек"
def format_time(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes} мин. {seconds} сек."


def parse_score(score_str):
    return float(score_str.replace(",", "."))


def analyze_data(data, required_score):
    filtered_data = []

    for row in data:
        score = parse_score(row["Оценка/100,00"])
        time_spent = row["Затраченное время"]
        time_in_seconds = convert_time(time_spent)

        if score == required_score:
            filtered_data.append((row["Фамилия"], row["Имя"], time_in_seconds))

    filtered_data.sort(key=lambda x: (x[2], x[0]))

    for last_name, first_name, time in filtered_data:
        formatted_time = format_time(time)
        print(f"{last_name} {first_name}: {formatted_time}")


file_path = "12 - 2.csv"
required_score = 90.00  # Заданный балл
data = read_csv(file_path)
analyze_data(data, required_score)
