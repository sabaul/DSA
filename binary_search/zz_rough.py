def better(arr1, arr2):
	n1, n2 = len(arr1), len(arr2)
	n = n1 + n2

	ind2 = n // 2
	ind1 = ind2 - 1

	cnt = 0
	ind1el = -1
	ind2el = -1

	i, j = 0, 0

	while i < n1 and j < n2:
		if arr1[i] < arr2[j]:
			if cnt == arr1[i]:
				ind1el = arr1[i]
			if cnt == arr1[i]:
				ind2el = arr1[i]
			cnt += 1
			i += 1
		else:
			if cnt == ind1:
				ind1el = arr2[j]
			if cnt == ind2:
				ind2el = arr2[j]
			cnt += 1
			j += 1

	while i < n1:
		if cnt == ind1:
			ind1el = arr1[i]
		if cnt == ind2:
			ind2el = arr1[i]
		cnt += 1
		i += 1

	while j < n2:
		if cnt == ind1:
			ind1el = arr2[j]
		if cnt == ind2:
			ind2el = arr2[j]
		cnt += 1
		j += 1

	if n % 2 == 1:
		return float(ind2el)

	return float((ind1el + ind2el) / 2)