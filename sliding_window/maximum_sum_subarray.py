# MAXIMUM SUM SUBARRAY OF SIZE K




# bruteforce tc = O(N * K) sc = O(1)
# def sliding_window(arr,k):
#     max_sum = float('-inf')
#     n = len(arr)
#     if n<k:
#         return "invalid input"
#     for i in range(0, n -k+1):
#         sum = 0
#         for j in range(i,i+k):
#             sum = sum + arr[j]
#         if sum > max_sum:
#             max_sum = sum 
#     return max_sum

# k = int(input())
# arr = [int(x)for x in input().split()]
# print(sliding_window(arr,k))





# silding window tc = O(N)
def sliding_window(arr,k):

    n = len(arr)
    if n<k:
        return "invalid input"
    window_sum = 0
    
    for i in range(0,k):
        window_sum += arr[i]
    max_sum = window_sum
    for i in range(1,n-k+1):
        window_sum = window_sum - arr[i-1] + arr[i+k-1]
        if window_sum > max_sum:
            max_sum = window_sum
    return max_sum

k = int(input())
arr = [int(x)for x in input().split()]
print(sliding_window(arr,k))

