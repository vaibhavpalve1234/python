# problem given an arr find the max sum contineous subarray 
# [2, 5, -10, 7, 8]
# 12 => [2, 5, -10, 7, 8]
# 15 =>[7, 8]
# 5 =>[-10, 7, 8]

def solve(arr):
    max_sum =0
    for i in range(0,len(arr)):
        for j in range(i,len(arr)):
            sum1 = 0
            for k in range(i,j+1):
                sum1+=arr[k]
            max_sum = max(max_sum,sum1)
    print(max_sum)
    
# pre-compitution
def solve1(arr):
    max_sum =0
    presum = [0]*len(arr)
    for i in range(len(arr)):
        for j in range(0,i):
            presum[j] += arr[j]
    print(presum) 
    for i in range(0,len(arr)):
        for j in range(i,len(arr)):
            sum = presum[j] - presum[i-1]
            max_sum = max(max_sum,sum)
    print(max(presum))
    
def solve2(arr):
    curr_sum = arr[0]
    max_sum = arr[0]
    for i in range(1,len(arr)):
        curr_sum = max(curr_sum+arr[i],arr[i])
        max_sum = max(curr_sum,max_sum)
    print(max_sum)
if __name__ == "__main__":
    arr =[2,5,-10,7,8,5]
    solve2(arr)