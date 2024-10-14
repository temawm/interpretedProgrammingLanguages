def reverse_elements_between_min_max(arr):
    if len(arr) < 2:
        return arr

    min_index = arr.index(min(arr))
    max_index = arr.index(max(arr))

    start_index = min(min_index, max_index) + 1
    end_index = max(min_index, max_index)

    if start_index >= end_index:
        return arr

    arr[start_index:end_index] = arr[start_index:end_index][::-1]
    return arr

def find_two_largest(arr):
    if len(arr) < 2:
        return "Массив должен содержать как минимум два элемента"

    largest = max(arr[0], arr[1])
    second_largest = min(arr[0], arr[1])

    for i in range(2, len(arr)):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        elif arr[i] > second_largest:
            second_largest = arr[i]

    return largest, second_largest

def find_most_frequent_indices(nums):
    num_list = nums.split()
    num_counts = {}

    for i, num in enumerate(num_list):
        if num in num_counts:
            num_counts[num].append(i)
        else:
            num_counts[num] = [i]

    most_frequent_num = max(num_counts, key=lambda x: len(num_counts[x]))

    return num_counts[most_frequent_num]
def find_max_odd(arr):
    max_odd = None

    for num in arr:
        if num % 2 != 0:  # Проверяем, является ли число нечетным
            if max_odd is None or num > max_odd:
                max_odd = num

    return max_odd

def build_array(arr):
    result = []
    for i, num in enumerate(arr):
        if num / (i + 1) == 1:
            print(num)
            result.append(num)

    return result


while True:
    task_number = int(input("Введите номер задачи (1-5) или 0 для завершения: "))

    if task_number == 0:
        print("Программа завершена.")
        break
        print("Отсортированные строки по количеству зеркальных троек:")
        for string in sorted_strings:
            print(string)
    elif task_number == 1:
        arr = [3, 8, 2, 5, 7, 1, 6, 4]
        result = reverse_elements_between_min_max(arr)
        print(result)
    elif task_number == 2:
        arr = [3, 8, 2, 5, 7, 1, 6, 4]
        largest, second_largest = find_two_largest(arr)
        print("Наибольший элемент:", largest)
        print("Второй по величине элемент:", second_largest)
    elif task_number == 3:
        arr = [3, 8, 2, 5, 7, 1, 6, 4]
        max_odd = find_max_odd(arr)
        if max_odd is not None:
            print("Максимальный нечетный элемент:", max_odd)
        else:
            print("В массиве нет нечетных элементов")
    elif task_number == 4:
        numbers = "1 2 3 2 4 2 5 2"
        indices = find_most_frequent_indices(numbers)
        print("Индексы наиболее часто встречающегося элемента:", indices)
    elif task_number == 5:
        elements = [ 1, 8, 9, 4, 5, 4, 3, 2, 1]
        new_array = build_array(elements)
        print("Массив, удовлетворяющий условиям:", new_array)
    else:
        print("Задачи с таким номером не существует. Попробуйте еще раз.")
