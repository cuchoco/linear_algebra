def calc(n):
    sum = 0
    for i in range(0, n):
        sum += int(input())
    return sum

print("Input the numver of values to be added => ")
count = int(input())


while count <= 0:
    count = int(input())

print("Sum =", calc(count))
