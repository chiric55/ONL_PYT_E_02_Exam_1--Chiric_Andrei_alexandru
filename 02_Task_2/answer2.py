import random

def get_random(number=3):
    if not isinstance(number, int) or number < 1:
        raise Exception("Invalid Data!")

    drawn_numbers = []

    while len(drawn_numbers) < number:
        num = random.randint(1, 100)
        if num not in drawn_numbers:
            drawn_numbers.append(num)

    return sorted(drawn_numbers)


try:
    result = get_random(5)
    print(result)
except Exception as e:
    print(e)