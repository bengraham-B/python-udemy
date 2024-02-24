# Calculate all the even numbers from 1 to a specified number

target = int(input())
accum = 0
for num in range(1, target+1):
    if num % 2 == 0:
        accum += num

print(accum)
