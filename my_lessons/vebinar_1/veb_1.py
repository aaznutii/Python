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
