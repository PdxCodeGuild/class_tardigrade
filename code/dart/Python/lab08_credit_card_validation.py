
card_number = list(input("Input your card number: ").strip())

check_digit = card_number.pop()

card_number.reverse()

doubled_digits = []

for index, digit in enumerate(card_number):
    if index % 2 == 0:
        doubled_digit = int(digit) * 2

        if doubled_digit > 9:
            doubled_digit -= 9

        doubled_digits.append(doubled_digit)
    else:
        doubled_digits.append(int(digit))

total = int(check_digit) + sum(doubled_digits)

[print("Valid!") if total % 10 == 0 else print("False!")]

# if total % 10 == 0:
#     print("Valid")
# else:
#     print("False")