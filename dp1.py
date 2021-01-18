dp = [None for _ in range(100005)]
def solve( starting_position,n):
    if starting_position == n:
        return 1
    if starting_position > n:
        return 0
    left = solve(starting_position+1,n)
    right = solve(starting_position+2,n)
    dp[starting_position] = left + right
    return dp[starting_position]
if __name__ == "__main__":
    n = 5
    print(solve(0,n))