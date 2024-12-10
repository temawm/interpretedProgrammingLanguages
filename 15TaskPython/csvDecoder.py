import csv


def read_csv(file_path):
    with open(file_path, encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

def time_to_seconds(time_spent):
    if "мин." in time_spent:
        parts = time_spent.split(" мин.")
        minutes = int(parts[0].split()[0])
        seconds = 0
        if "сек." in parts[1]:
            seconds = int(parts[1].split()[0].replace("сек.", ""))
        return minutes * 60 + seconds
    elif "ч." in time_spent:
        parts = time_spent.split(" ч.")
        hours = int(parts[0].split()[0])
        minutes = 0
        if "мин." in parts[1]:
            minutes = int(parts[1].split()[0].replace("мин.", ""))
        return hours * 3600 + minutes * 60
    else:
        return 0


def format_time(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes} мин. {seconds} сек."

def filter_and_sort(data, required_score):
    filtered_data = [
        row for row in data if float(row["Оценка/10,00"].replace(",", ".")) == required_score
    ]

    filtered_data.sort(key=lambda x: (time_to_seconds(x["Затраченное время"]), x["Фамилия"]))

    return filtered_data


# Анализ данных
def analyze_data(data, required_score):
    filtered_data = filter_and_sort(data, required_score)

    if not filtered_data:
        print(f"Нет участников с таким количеством баллов: {required_score}")
        return

    print(f"Участники с баллом {required_score} (отсортированы по времени):")
    for row in filtered_data:
        name = f"{row['Фамилия']} {row['Имя']}"
        score = row["Оценка/10,00"]
        time_spent = row["Затраченное время"]
        total_seconds = time_to_seconds(time_spent)
        print(f"{name} - Балл: {score}, Время: {format_time(total_seconds)}")


file_path = "12 - 1.csv"
required_score = 9.0  # Заданный балл для фильтрации
data = read_csv(file_path)
analyze_data(data, required_score)
