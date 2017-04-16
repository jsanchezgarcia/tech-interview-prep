def edit_distance_recursive(s1, s2, n, m):
	if n == 0:
		return m

	if m == 0:
		return n

	if s1[n-1] == s2[m-1]:
		return edit_distance_recursive(s1,s2,n-1,m-1)
	else:
		# Try the 3 options
		return 1 + min(edit_distance_recursive(s1,s2,n-1,m-1),	#replace
					edit_distance_recursive(s1,s2,n,m-1),			#add
					edit_distance_recursive(s1,s2,n-1, m))		# remove

def edit_distance_dp(s1,s2):
	m = len(s1)	# cols
	n = len(s2) # rows

	dp = [[0 for x in range(m+1)] for y in range(n+1)]

	for i in range(n+1):
		for j in range(m+1):
			if i == 0:
				dp[i][j] = j
			if j == 0:
				dp[i][j] = i
			if s1[j-1] == s2[i-1]:
				dp[i][j] = dp[i-1][j-1]
			else:
				dp[i][j] = 1 + min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])

	return dp[-1][-1]

s1 = 'barco'
s2 = 'arca'

print edit_distance_recursive(s1, s2, len(s1), len(s2))
print edit_distance_dp(s1, s2)