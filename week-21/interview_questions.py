# PLUS ONE: Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
# [1, 2, 3] -> [1, 2, 4]
# [9, 9, 9] -> [1, 0, 0, 0]
def plus_one_verbose(lst):
    # s = ''
    # for item in lst:
    #     s += str(item)
    num_str = ''.join([str(item) for item in lst])          # list -> str
    # plus_one_int = int(s) + 1                             # str -> (int + 1)
    # plus_one_str = str(plus_one_int)                      # (int + 1) -> str
    # plus_one_list = [int(item) for item in plus_one_str]  # str -> list
    return [int(item) for item in str(int(num_str) + 1)]

def plus_one(nums):
    return [int(item) for item in str(int(''.join([str(item) for item in nums])) + 1)]

# def plus_one2(digits):
#     num = 0
#     for i in range(len(digits)):
#         num += digits[i] * pow(10, (len(digits)-1-i))
#     return [int(i) for i in str(num+1)]

def plus_one2(nums):
    """Raise error on bad input"""
    if not isinstance(nums, (list, tuple)):
        raise Exception('Input "nums" must be a list')
    return [int(item) for item in str(int(''.join([str(item) for item in nums])) + 1)]

# print(plus_one([1, 2, 3]))  # [1, 2, 4]
# print(plus_one([7, 8, 9]))  # [7, 9, 0]
# print(plus_one([9, 9, 9]))  # [1, 0, 0, 0]




# ROTATE ARRAY: Given an array, rotate the array to the right by k steps, where k is non-negative.
# [1, 2, 3, 4, 5], k=2 -> [4, 5, 1, 2, 3]
# [1, 2, 3, 4, 5], k=3 -> [3, 4, 5, 1, 2]
def rotate_array1(nums, k):
    for _ in range(k):
        end_value = nums.pop(-1)
        nums.insert(0, end_value)
    return nums

# # removing items from list
# lst = ['a', 'b', 'c']
# lst.remove('b')     # remove first matching value
# del lst[1]          # remove item by index
# value = lst.pop(1)  # remove item by index AND return it

def rotate_array2(nums, k):
    length = len(nums)
    end_segment = nums[(length - k):]
    start_segment = nums[:(length - k)]
    return end_segment + start_segment

def rotate_array3(nums, k):
    """Inplace"""
    for _ in range(k):
        end_value = nums.pop(-1)
        nums.insert(0, end_value)

def rotate_array4(nums, k):
    """Inplace"""
    length = len(nums)
    end_segment = nums[(length - k):]
    start_segment = nums[:(length - k)]
    nums[:] = end_segment + start_segment  # edits items in OG list

def rotate_array5(nums, k):
    """Inplace and raise error on bad k"""
    if k < 0 or k > len(nums):
        raise Exception('Invalid rotate value "k"')
    for _ in range(k):
        end_value = nums.pop(6)
        nums.insert(0, end_value)

# print(rotate_array1([1, 2, 3, 4, 5], 2))  # [4, 5, 1, 2, 3]
# print(rotate_array1([1, 2, 3, 4, 5], 3))  # [3, 4, 5, 1, 2]

# inplace
nums = [1, 2, 3, 4, 5]
# rotate_array4(nums, 2)
rotate_array5(nums, -1)
print(nums)



# Perfect number
# 6: 1, 2, 3
# 28: 1, 2, 4, 7, 14
def is_perfect_number(num):
    if num > 0:
        factors = []
        for i in range(num + 1):
            if sum(factors) > num:
                return False
            for j in range(num + 1):
                if i * j == num and i != num:
                    factors.append(i)
        # print(factors)
        if sum(factors) == num:
            return True
    return False

for n in range(8129):
    if is_perfect_number(n):
        print(n)




# Single Number: Given a non-empty array of integers, every element appears twice except for one. Find that single one.
def singleNumber1(nums):
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0) + 1
    for key, val in dic.items():
        if val == 1:
            return key


def singleNumber2(nums):
    """Return first single"""
    for num in nums:
        if nums.count(num) == 1:
            return num
    return num


def singleNumber3(nums):
    """Return last single"""
    last_single = None
    for num in nums:
        if nums.count(num) == 1:
            last_single = num
    return last_single

print(singleNumber2([1, 1, 1, 2, 2, 3]))  # 3
print(singleNumber3([1, 1, 1, 2, 2, 3, 4]))  # 4









# Implement strStr(): Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
def strStr(haystack, needle):
    for i in range(len(haystack) - len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1






# Merge Sorted Array
def merge(nums1, m, nums2, n):
    while m > 0 and n > 0:
        if nums1[m-1] >= nums2[n-1]:
            nums1[m+n-1] = nums1[m-1]
            m -= 1
        else:
            nums1[m+n-1] = nums2[n-1]
            n -= 1
    if n > 0:
        nums1[:n] = nums2[:n]





# Sums of two different squares for number
# 17: [1, 4]
# 25: [3, 4]
# 65: [1, 8, 4, 7]
# 85: [2, 9, 6, 7]
import math

def sum_of_squares(n):
    """Brute force"""
    result = []
    for i in range(1, n):
        i_sq = i**2
        if i_sq > n:
            continue
        for j in range(1, n):
            if i == j:
                continue
            j_sq = j**2
            if j_sq > n:
                continue
            if i_sq + j_sq == n:
                if i not in result:
                    result.append(i)
                if j not in result:
                    result.append(j)
    return result

def sum_of_squares2(n):
    """Compliments list while iterating"""
    result = []
    compliments = []
    for i in range(1, n):
        # print(f'i: {i}')
        squared = i**2
        # print(f'squared: {squared}')
        if squared > n:
            break
        compliment = math.sqrt(n - squared)
        # print(f'compliment: {compliment}')
        if i in compliments:
            if compliment not in result:
                result.append(int(compliment))
            if i not in result:
                result.append(i)
        if compliment.is_integer():
            compliments.append(int(compliment))
        # print(f'compliments: {compliments}')
        # print(f'result: {result}')
    return result

# print(sum_of_squares(85))
print(sum_of_squares2(85))
