
#1 (Easy) 
 
"""If two Arrays A1[] and A2[] of size m and n with distinct elements in each of the Arrays is given,
find all the pair of elements (one from A1 and other from A2) whose product should be a perfect square. 
Print -1 if no pairs can be formed."""

# from math import sqrt,floor
# A1 = [1,2,3,4,5,6,]
# A2 = [2,3,4,5,8]
# A3=[]


# for i in A1:
#     for j in A2:
#         value = i*j
#         sqrt_value =sqrt(value)
#         if sqrt_value - floor(sqrt_value)==0:
#             A3.append((i,j))
        

# if len(A3)!=0:
#     print(A3)
# else:
#     print(-1)



#2 (Medium)
 
"""Given a string STR, find the length of the longest substring without repeating characters.
·         For “ABDEFGABEF”, the longest substring are “BDEFGA” and “DEFGAB”, with length 6.
·         For “BBBB” the longest substring is “B”, with length 1."""

# string1= "ABDEFGABEF"
# string2=""
# for i in range(len(string1)):
#     if string1[i] not in lst:
#         lst+=string1[i]
#         break
#     print(string1[0,i])


def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    
    str_list = []
    max_length = 0
    
    for x in s:
        if x in str_list:
            # import pdb
            # pdb.set_trace()
            str_list = str_list[str_list.index(x)+1:]
            
        str_list.append(x)    
        max_length = max(max_length, len(str_list))
        
    return max_length


print(lengthOfLongestSubstring("sdfghyrqadgf"))


#3 (Hard)
 
"""A one dimensional array is given, that may contain both positive and negative integers. Find the sum of contiguous subarray of numbers which has the largest sum.

For example, if the given array is {-2, -5, 6, -2, -3, 1, 5, -6}, then the maximum subarray sum is 7 (see highlighted elements)."""

arr=[-2, -5, 6, -2, -3, 1, 5, -6]
max_sum = 0
sub_ary=[]

for i in range(len(arr)):
    for j in range(len(arr)):
        subarr_left =arr[i:-j]
        # subarr_right=arr[i:]
        print(subarr_left)
        # print(subarr_right)

    if sum(subarr_left)>sum(subarr_right) and max_sum > sum(subarr_left):
        max_sum=sum(subarr_left)
        sub_ary = subarr_left
    elif sum(subarr_left)< sum(subarr_right) and max_sum >sum(subarr_right):
        max_sum =sum(subarr_right)
        sub_ary = subarr_right
print(sub_ary)

# max_so_far=arr[0]
# current_max=arr[0]

# for i in range(1,len(arr)):
#     current_max =max(arr[i], current_max+arr[i])
#     max_so_far =max(max_so_far, current_max)
# print(max_so_far)


# Python program to print largest contiguous array sum 
  
# from sys import maxsize 
  
# # Function to find the maximum contiguous subarray 
# # and print its starting and end index 
# def maxSubArraySum(a,size): 
  
#     max_so_far = -maxsize - 1
#     print(max_so_far)
#     max_ending_here = 0
#     start = 0
#     end = 0
#     s = 0
  
#     for i in range(0,size): 
  
#         max_ending_here += a[i] 
  
#         if max_so_far < max_ending_here: 
#             max_so_far = max_ending_here 
#             start = s 
#             end = i 
  
#         if max_ending_here < 0: 
#             max_ending_here = 0
#             s = i+1
  
#     print ("Maximum contiguous sum is %d"%(max_so_far)) 
#     print ("Starting Index %d"%(start)) 
#     print ("Ending Index %d"%(end)) 


# # Driver program to test maxSubArraySum 
# a = [-2, -3, 4, -1, -2, 1, 5, -3] 
# maxSubArraySum(a,len(a)) 
 