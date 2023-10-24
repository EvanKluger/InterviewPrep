'''
Given two sequences, find the length of the longest subsequence present in both of them. 
A subsequence is a sequence that appears in the same relative order but not necessarily contiguous 
(i.e., not a substring).
'''

def lcs(sq1,sq2):
    m = len(sq1)
    n = len(sq2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if sq1[i-1] == sq2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]
    

s1 = "ABCBDAB"
s2 = "BDCAB"
print(lcs(s1, s2))