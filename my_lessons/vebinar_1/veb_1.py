from time import perf_counter

nums = [el for el in range(1, 10 ** 5 + 1)]
start = perf_counter()
print(sum(nums), perf_counter() - start)

start = perf_counter()
sum = 0
for el in range(len(nums)):
    sum += el
print(sum, perf_counter() - start)

start = perf_counter()
sum = 0
for i in range(len(nums)):
    sum += nums[i]
print(sum, perf_counter() - start)

start = perf_counter()
sum = 0
for el in nums:
    sum += el
print(sum, perf_counter() - start)

print(id(sum))  # Идентификатор в памяти

# map, filter, zip = итераторы
lt = ['dfdf', 'fgfggf', 'ghghh']
res = map(str.title, lt)  # экономично по памяти
print(res)
print(*res)  # * для распаковки
print(*res)  # Не напечатает, потому что итератор исчерпан

print(tuple(map(str.title, lt)))  # чуть менее затратно, поскольку не изменяемый тип данных
print(list(map(str.title, lt)))  # Очень затратно по памяти, поскольку создает список
