# ========FIRST NEGATIVE NUMBER IN EVERY WINDOW OF SIZE K=========


from collections import deque

def printFirstNegativeInteger( arr,n,k):
    # bruteforce TC = O(n * k)


    # ans = []
    # for i in range(0,n-k+1):
    #     for j in range(i , i + k):
    #         if arr[j] < 0:
    #             ans.append(arr[j])
    #             break
    #     else:
    #         ans.append(0)
    # return ans    



        
     
    
    # optimied using sliding window but sc = o(k) 
    # tc = o(N)   SC = O(k)
    # ans = []   
    # q = deque()
    # i,j = 0,0
    # while j < n:
    #     # keep track of all negative elements
    #     if arr[j] < 0:
    #         q.append(arr[j])
        
    #     # first reach the window size
    #     if j - i + 1 < k:  
    #         j += 1
        
    #     # once the window size is hit maintain it and add
    #     # negative element for each window
    #     elif j - i + 1 == k:
    #         if not q:
    #             ans.append(0)
    #         else:
    #             ans.append(q[0])
    #             if arr[i] < 0:
    #                 q.popleft()
    #         i += 1
    #         j += 1
    # return ans
                
                
                
                
                
                
    
    # CONSTANT SPACE
    # tc = O(N) AND SC = O(1) 
    last_checked_index = -1
    last_negative_value_index = -1
    ans = []
    for i in range(0,n-k+1):
        if last_negative_value_index < i:
            for j in range(last_checked_index+1,i+k):
                last_checked_index += 1
                if arr[j] < 0:
                    last_negative_value_index = j
                    ans.append(arr[j])
                    break
            else:
                ans.append(0)
        else:
            ans.append(ans[-1])
    return ans
        
arr = [1,2,3,-1,2,-6,78,5,7]
n = 9
k = 3
print(printFirstNegativeInteger( arr,n,k))