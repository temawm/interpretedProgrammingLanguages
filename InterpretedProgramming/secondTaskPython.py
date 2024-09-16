import random
def shuffle_inner_chars(text):
    def shuffle_word(word):
        if len(word) <= 3:
            return word
        first, middle, last = word[0], word[1:-1], word[-1]
        middle = list(middle)
        random.shuffle(middle)
        return first + ''.join(middle) + last

    words = text.split()
    shuffled_words = [shuffle_word(word) for word in words]
    return ' '.join(shuffled_words)




def rearrange_digits_and_letters(string):
    digits = []
    letters = []

    # Разделяем цифры и буквы
    for char in string:
        if char.isdigit():
            digits.append(char)
        elif char.isalpha():
            letters.append(char)

    # Объединяем цифры и буквы
    return ''.join(digits) + ''.join(letters)

def count_words_by_spaces(string):
    string = string.strip()
    if not string:
        return 0
    return string.count(' ') + 1


# Пример
input_text = "Пример строки для перемешивания символов"
result = shuffle_inner_chars(input_text)
print(f"Было: {input_text}, стало: {result}")


# Пример использования
input_string = "a1b2c3d4"
result = rearrange_digits_and_letters(input_string)
print(f"Было {input_string}, стало {result}")  # Ожидаемый результат: "1234abcd"


# Пример использования
input_string = "Пример строки для подсчёта слов"
result = count_words_by_spaces(input_string)
print(f"Количество слов: {result}")




