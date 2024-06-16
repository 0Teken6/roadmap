m = map(lambda x: x**2, [1, 2, 4, 5])
for i in m:
    print(i)

def my_map(func, lst):
    res = []
    for item in lst:
        res.append(func(item))
    return res

print(my_map(lambda x: x**3, [2, 4, 1]))

add = lambda x, y: x + y
print(add(1, 4))

my_filter = lambda lst: [[i for i in lst if i % 2 == 0], [j for j in lst if j % 2 != 0]]
print(my_filter([1, 2, 4, 6, 5, 6, 4, 7, 8, 9]))



