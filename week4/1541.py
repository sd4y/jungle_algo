expression = input()

sub_expressions = expression.split('-')

numbers = []

for i in sub_expressions:
    currnet = sum(map(int, i.split('+')))
    numbers.append(currnet)

size = len(numbers)

result = numbers[0]

for i in range(1, size):
    result -= numbers[i]

print(result)
    