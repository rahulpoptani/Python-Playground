def decimalToBinary(number):
    if number <= 1:
        return str(number)
    else:
        return decimalToBinary(number//2) + decimalToBinary(number%2)


print(decimalToBinary(11))