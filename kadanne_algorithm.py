# problem given an arra find the max sum contineous subarray 
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
    return
if __name__ == "__main__":
    arr =[2,5,-10,7,8,5]
    solve(arr)