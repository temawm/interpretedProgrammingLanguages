def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count_vowels = sum(1 for char in s if char in vowels)
    count_consonants = sum(1 for char in s if char in consonants)
    print(s, count_vowels, count_consonants,  count_vowels / count_consonants)
    return count_vowels, count_consonants

def sort_string_by_difference(input_string):
    words = input_string.split()
    sorted_words = sorted(words, key=lambda x: (abs(count_vowels_consonants(x)[0] / count_vowels_consonants(x)[1]))/ len(
        words))
    return ' '.join(sorted_words)

input_string = "Hello World Python Program abbbb aaaaaab"
sorted_string = sort_string_by_difference(input_string)
print(sorted_string)


def median_word_length(s):
    words = s.split()
    word_lengths = [len(word) for word in words]
    sorted_word_lengths = sorted(word_lengths)

    if len(sorted_word_lengths) % 2 == 0:
        median = (sorted_word_lengths[len(sorted_word_lengths) // 2 - 1] + sorted_word_lengths[
            len(sorted_word_lengths) // 2]) / 2
    else:
        median = sorted_word_lengths[len(sorted_word_lengths) // 2]

    return median


def sort_strings_by_median_length(strings):
    return sorted(strings, key=lambda x: median_word_length(x))


# Пример использования
strings = ["Я студент ФКТиПМ", "Что где мне я а и", "Программирование, эффективно, интерполяция"]
sorted_strings = sort_strings_by_median_length(strings)
print()
print("Отсортированные строки по медианному значению длины слов:")
for string in sorted_strings:
    print(string)



def quadratic_deviation(s):
    ascii_values = [ord(char) for char in s]
    max_ascii = max(ascii_values)
    mid = len(s) // 2
    deviations = [abs(ord(s[i]) - ord(s[len(s)-1-i])) for i in range(mid)]
    mean_deviation = sum(deviations) / len(deviations)
    quadratic_deviations = [(dev - mean_deviation) ** 2 for dev in deviations]
    return max_ascii, sum(quadratic_deviations), ascii_values

def sort_strings_by_quadratic_deviation(strings):
    return sorted(strings, key=lambda x: quadratic_deviation(x)[1])

# Пример использования
strings = ["abcde", "opxyz", "hello world", "programming", "xxxxxx"]
sorted_strings = sort_strings_by_quadratic_deviation(strings)
print()
print("Отсортированные строки по квадратичному отклонению:")
for string in sorted_strings:
    max_ascii, quadratic_deviation_val, ascii_values = quadratic_deviation(string)
    print(f"Строка: {string}, ASCII коды: {ascii_values}, Квадратичное отклонение: {quadratic_deviation_val}")


def count_mirror_triplets(s):
    count = 0
    for i in range(len(s) - 2):
        if s[i] == s[i + 2] and i + 2 < len(s):
            count += 1
    return count

def sort_strings_by_mirror_triplets(strings):
    return sorted(strings, key=lambda x: count_mirror_triplets(x), reverse=True)

# Пример использования
strings = ["ada", "bgb", "abcdeedcba", "ada","programming"]
sorted_strings = sort_strings_by_mirror_triplets(strings)
print()
print("Отсортированные строки по количеству зеркальных троек:")
for string in sorted_strings:
    print(string)
