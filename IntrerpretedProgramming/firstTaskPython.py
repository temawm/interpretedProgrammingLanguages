import math

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

# Функция для нахождения суммы простых цифр числа
def sum_of_prime_digits(number):
    prime_digits = [2, 3, 5, 7]
    sum_primes = 0
    for digit in str(number):
        if int(digit) in prime_digits:
            sum_primes += int(digit)
    return sum_primes

# Функция для проверки, являются ли два числа взаимно простыми
def are_coprime(a, b):
    return math.gcd(a, b) == 1

# Функция для нахождения количества чисел, которые:
# 1. Не являются делителями исходного числа
# 2. Не взаимно просты с исходным числом
# 3. Взаимно просты с суммой простых цифр исходного числа
def count_special_numbers(number):
    prime_sum = sum_of_prime_digits(number)
    count = 0
    for i in range(1, number + 1):
        if number % i != 0 and not are_coprime(i, number) and are_coprime(i, prime_sum):
            count += 1
    return count


# Главная функция, вызывающая две другие функции
def main():
    number = 100000

    print(f"Сумма непростых делителей числа {number}: {sum_non_prime_divisors(number)}")
    print(f"Количество цифр числа {number}, меньших 3: {count_digits_less_than_3(number)}")
    print(f"Количество специальных чисел для {number}: {count_special_numbers(number)}")


if __name__ == "__main__":
    main()