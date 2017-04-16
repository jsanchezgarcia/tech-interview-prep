# http://www.geeksforgeeks.org/trapping-rain-water/

def trapped_water(heights):
	max_l, max_r = precompute_max(heights)
	print max_l, max_r
	total = 0
	for i in range(len(heights)):
		partial = min(max_l[i], max_r[i]) - heights[i]
		if partial > 0:
			total += partial
	return total

def precompute_max(heights):
	max_l = [heights[0]] * len(heights)
	max_r = [heights[-1]] * len(heights)

	for i in range(1, len(heights)):
		max_l[i] = max(max_l[i-1], heights[i])

	for i in range(len(heights)-2, -1, -1):
		max_r[i] = max(max_r[i+1], heights[i])

	return (max_l, max_r)


heights = [3, 0, 0, 2, 0, 4]
print(trapped_water(heights))