from collections import defaultdict

def findAnagrams(s,p):
    # bruteforce approach
    # TLE ERROR
    # use 2 loops and for each window check whether 2 strings are anagram of each other or not
    # using a dictionary
    
    # ans = []
    # l1 = len(s)
    # l2 = len(p)
    # for i in range(l1-l2+1):
    #     d = defaultdict(int)
    #     f = 1
    #     for j in range(0,l2):
    #         d[p[j]] += 1
    #     for k in range(i,i+l2):
    #         if s[k] not in d:
    #             f = 0
    #             break
    #         else:
    #             d[s[k]] -= 1
    #     if f == 0:
    #         continue
    #     for v in d.values():
    #         if v != 0:
    #             break
    #     else:
    #         ans.append(i)
    # return ans









    # optimized approach
    # use slinding window to avoid repetition of work
    # we have to traverse the whole dictionary in every iteration to check that all the values 
    # are zero or not for dat window


    # ans = []
    # l1 = len(s)
    # l2 = len(p)
    # d = {}
    # for x in p:
    #     d[x] = d.get(x,0) + 1
    # i = 0
    # j = 0
    # while j < l1:
    #     if j - i != l2:
    #         if s[j] in d:
    #             d[s[j]] -= 1
    #         j += 1

    #     else:
    #         for value in d.values():
    #             if value != 0:
    #                 break
    #         else:
    #             ans.append(i)
    #         if s[i] in d:
    #             d[s[i]] += 1
    #         if s[j] in d:
    #             d[s[j]] -= 1
    #         i += 1
    #         j += 1
    # for value in d.values():
    #     if value != 0:
    #         break
    # else:
    #     ans.append(i)   
    # return ans





    # optimized approach 
    # take a counter variable which can be used to check for every window string instead of 
    #  traversing the whole dictionary to check that current window string is anagram or not

    d = defaultdict(int)
    i , j = 0,0
    ans = []
    k = len(p)
    n = len(s)
    for x in p:
        d[x] += 1
    count = len(d)
    while j < n:
        if s[j] in d:
            d[s[j]] -= 1
            if d[s[j]] == 0:
                count -= 1
        
        # increment j till the window size is reached 
        if j - i + 1 != k:
            j += 1

        # once the window size is reached calculate the ans for every window and 
        # maintain the window
        else:
            if count == 0:
                ans.append(i)
            if s[i] in d:
                d[s[i]] += 1
                if d[s[i]] == 1:
                    count += 1
            i += 1
            j += 1
    return ans
 
s = "foxofffoxroff"
p = "ffo"
print(findAnagrams(s,p))

