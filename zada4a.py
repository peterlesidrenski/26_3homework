
numbers = [96, 815, 402, 317, 368, 448, 841, 315, 630, 606, 388, 77, 552, 15, 375]
print(numbers)
print(numbers[6:10])
sorted_numbers = sorted(numbers)
print(sorted_numbers)
reversed_copy = list(reversed(numbers[:]))
numbers.extend(reversed_copy)
print(numbers)
count_379 = numbers.count(379)
numbers.insert(7, count_379)
print(numbers)
for num in numbers:
    if str(num)[-1] == '2':
        numbers.insert(4, num)
        break
print(numbers)
numbers.sort()
print(numbers)
print(numbers[::-1])
numbers[3] = 139310
print(numbers)
numbers[5], numbers[7] = numbers[7], numbers[5]
print(numbers)
if any(num % 10 == 3 for num in numbers):
    numbers.remove(next(num for num in numbers if num % 10 == 3))
print(numbers)
print(' '.join(map(str, numbers)))
