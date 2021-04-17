"""Сложите цифры целого числа."""

def print_hi():
    num = 123456789
    nums = str(num)
    result = 0
    for i in nums:
        result += int(i)
    print(result)


if __name__ == '__main__':
    print_hi()
