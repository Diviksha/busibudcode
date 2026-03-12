def StringChallenge(s):
    ans = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                ans = max(ans, len(set(s[i+1:j])))
    return ans
