# -*- coding: utf-8 -*-

def triangles(max):
	n, result = 0, [1]
	while n < max:
		yield result
		if len(result) >= 2:
			result = [result[x] + result[x+1] for x in range(len(result) - 1)]
			result.insert(0, 1)
		result.append(1)
		n = n + 1

	return "done"

scale = input("input scale: ")
while scale.isdigit() == False:
	scale = input("input scale: ")


g = triangles(int(scale))
for n in g:
	print(n) 




