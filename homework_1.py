import math
print('Factorizer Pro (TM).')

number = int(input("Enter the number for factorization: "))
divisor = 2
ans = str(number) + " = "
limit = math.sqrt(number)

# Zbieram wszystkie nietrywialne dzielniki
while number > 1 and divisor <= limit:
    if number % divisor == 0:
        number = number // divisor
        ans += f"{divisor}*"
    else:
        divisor += 1

# Jeśli liczba była pierwsza, to dodaję ją do faktoryzacji
if number > 1:
    ans += str(number)

# Jeśli na końcu jest gwiazdka, to usuwam
if ans[-1] == '*':
    ans = ans[:-1]
print(ans)
