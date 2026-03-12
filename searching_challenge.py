def SearchingChallenge(strArr):
    rows = len(strArr)
    cols = len(strArr[0])
    visited = set()
    holes = 0

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if strArr[r][c] != "0" or (r, c) in visited:
            return

        visited.add((r, c))

        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    for r in range(rows):
        for c in range(cols):
            if strArr[r][c] == "0" and (r, c) not in visited:
                holes += 1
                dfs(r, c)

    return holes
