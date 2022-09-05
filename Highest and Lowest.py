def high_and_low(numbers):
    number = [int(x) for x in numbers.split(' ')]
    return f"{max(number)} {min(number)}"
