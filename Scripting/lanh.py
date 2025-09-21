import random

num = [4]
for i in range(14):
    num.append(random.randint(0,9))

sum = 0

#Calculate the Lunh checksum
for i, digit in enumerate(num):
    if i % 2 == 0:
        if digit * 2 > 9:
            digit = digit * 2 - 9
        else:
            digit = digit * 2
    sum += digit
checkdigit = (10 - (sum % 10)) % 10

num.append(checkdigit)

print("Card number: ", " ".join("".join(map(str, num))[i : i + 4] for i in range(0, len(num), 4)))
