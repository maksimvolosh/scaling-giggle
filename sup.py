def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers_up_to(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def sum_of_primes(limit):
    primes = prime_numbers_up_to(limit)
    return sum(primes)

number = int(input("Введите число: "))
if is_prime(number):
    print(f"Число {number} является простым.")
else:
    print(f"Число {number} не является простым.")

print(f"Простые числа до {number}: {prime_numbers_up_to(number)}")
print(f"Сумма всех простых чисел до {number}: {sum_of_primes(number)}")
