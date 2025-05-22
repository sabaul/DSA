def findLCS(n: int, m: int, s: str, t: str) -> str:
    dp = [[0 for i in range(m+1)] for j in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    res = []
    i, j = n, m
    # lcs = dp[-1][-1]
    for row in dp:
    	print(row)

    while i > 0 and j > 0:
        if s[i-1] == t[j-1]:
            res.append(s[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    return ''.join(res[::-1])

n=5
m=6
s='ababa'
t='cbbcad'

print(findLCS(n, m, s, t))