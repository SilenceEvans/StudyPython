i = 1
while i <= 5:
    print(i)
    i = i + 1

# 0——100求和
n = 0
result = 0
while n <= 100:
    result += n
    n += 1
print(result)

# 0 ——100中偶数求和
n = 0
result = 0
while n <= 100:
    if n % 2 == 0:
        result += n
    n += 1
print(result)

# break 与 continue
# break
n = 0
while n <= 10:
    print(n)
    if n == 5:
        break
    n += 1

# continue
n = 0
while n <= 10:
    n += 1
    if n == 5:
        continue
    print(n)
