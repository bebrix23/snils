def is_valid_snils(snils):
    snils = snils.replace("-", "").replace(" ", "")
    if not snils.isdigit() or len(snils) != 11:
        return False

    check_digit = int(snils[-2:])
    snils_numbers = [int(digit) for digit in snils[:-2]]

    calculated_check_digit = 0
    for i in range(9):
        calculated_check_digit += snils_numbers[i] * (9 - i)

    if calculated_check_digit < 100:
        return check_digit == calculated_check_digit
    elif calculated_check_digit == 100 or calculated_check_digit == 101:
        return check_digit == 0
    else:
        return check_digit == calculated_check_digit % 101

input_snils = input("Введите  СНИЛС: ")
if is_valid_snils(input_snils):  # Проверяем введенный СНИЛС на валидность
    print("СНИЛС введен верно")
else:
    print("СНИЛС введен неверно")