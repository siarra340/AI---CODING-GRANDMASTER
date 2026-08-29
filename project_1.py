num = int(input("Write a Number! "))

str_num = str(num)
num_len = len(str_num)

total_amount = 0

for digit_char in str_num:

    digit = int(digit_char)

    total_amount += digit ** num_len

if total_amount == num:
    print(f"The number {num} is an Armstrong number")
else:
    print(f"The number {num} is not an Armstrong number")

    




