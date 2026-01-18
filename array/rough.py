arr = [1, 1, 2, 2, 2, 3, 3]
set_arr = set(arr)
print(list(set_arr))

for a in set_arr:
	print(a)

for i, a in enumerate(set_arr):
	print(i, a)