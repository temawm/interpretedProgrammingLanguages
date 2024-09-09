# Функция для нахождения количества непростых делителей числа
def sum_non_prime_divisors(number):
    sum = 0
    for i in range(2, number):
        if number % i == 0 and i != 1 and i != number:
            sum += i
    return sum

# Функция для нахождения количества цифр числа, меньших 3
def count_digits_less_than_3(number):
    count = 0
    for digit in str(number):
        if int(digit) < 3:
            count += 1
    return count

# Главная функция, вызывающая две другие функции
def main():
    number = 100

    print(f"Сумма непростых делителей числа {number}: {sum_non_prime_divisors(number)}")
    print(f"Количество цифр числа {number}, меньших 3: {count_digits_less_than_3(number)}")

if __name__ == "__main__":
    main()
