def PrintSubsequence(arr,idx,curr_sub):
    if idx == len(arr):
        print(curr_sub)
        return
    curr_sub.append(arr[idx])
    PrintSubsequence(arr,idx+1,curr_sub)
    curr_sub.pop()
    PrintSubsequence(arr,idx+1,curr_sub)

def maxLenghtOfSubsequence(arr):
    dp = [1] * len(arr)

    for j in range(1,len(arr)):
        for i in range(0,j):
            if arr[j] > arr[i]:
                dp[j] = max(dp[j],dp[i]+1)
    print(dp)
    return max(dp)
if __name__ == "__main__":
    arr = [1, 2, 3, 6]
    # print(maxLenghtOfSubsequence(arr))
    print(PrintSubsequence(arr,0,[]))