# Binary Search 二分搜索算法

- ## binary search 的三个重要部分：
    - 1. 二分搜索的序列是要排序的，如果没有排序，需要先将序列排序
    - 2. 使用递归或非递归的方式寻找元素
    - 3. 判断是否在候选区域
- ## 时空间复杂度：
    - 对于下面三种不同类型的binary search template, 时空间复杂度都是一样的：
        - Time complexity: O(logN)
        - Space complexity: O(1)
    - why `logN` ?
        - So every time you a call the subroutine ( or complete one iteration ) the size reduced to half of the existing part.
        - First N become N/2, then it become N/4 and go on till it find the element or size become 1.
        - The maximum no of iterations is log N (base 2).
    - why `O(1)` ?
        - Although, Binary Search does require keeping track of 3 indicies, the iterative solution does not typically require any other additional space and can be applied directly on the collection itself, therefore warrants O(1) or constant space. 
## Binary Search Python Template I:
    - it is used to search for an element or condition which can be determined by accessing a single index in the array.
```python
def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # determine whether exists nums
    if len(nums) == 0:
        return -1
        
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else: 
            right = mid - 1
    
    # END condition: left > right
    return -1
```
- ### 重点 key attributes:
    - 不需要post-processing，只需要找到特定的元素
    - 初始条件: `left = 0, right = lenght -1`
    - 终止条件: `left > right`
    - 向左搜索：`right = mid - 1`
    - 向右搜索：`left = mid + 1`
## Binary Search Python Template II:
    - It is used to search for an element or condition which requires accessing the current index and its immediate right neighbor's index in the array.
```python
def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1
    
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    # Post-processing:
    # End Condition: left == right
    if left != len(nums) and nums[left] == target:
        return left
    return -1
```
- ### 重点 key attributes:
    - 搜索条件需要访问元素的直接右邻居
    - 使用元素的右邻居来确定是否满足条件并决定是向左还是向右
    - 保证搜索空间的每一步至少有2个
    - 需要进行后处理。当你剩下1个元素时，循环/递归结束。需要评估剩余元素是否符合条件。

- ### 区别点：
    - 初始条件: left = 0, right = length
    - 终止条件: left == right
    - 向左搜索: right = mid
    - 向右搜索: left = mid+1 

- ## Binary Search Python Template III:
    - It is used to search for an element or condition which requires accessing the current index and its immediate left and right neighbor's index in the array.
```python
def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1
    
    left, right = 0, len(nums)
    
    while left + 1 < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid
        else:
            right = mid
        
    # Post-processing:
    # End Condition: left + 1 == right
    if nums[left] == target: return left
    if nums[right] == target: return right
    return -1
```
- ### 重点 key attributes:
    - 实现二进制搜索的另一种方法
    - 搜索条件需要访问元素的直接左右邻居
    - 使用元素的邻居来确定是否满足条件并决定是向左还是向右
    - 保证搜索空间每个步骤至少有3个
    - 需要进行后处理。当剩下2个元素时，循环/递归结束。需要评估其余元素是否符合条件。
- ### 区别点：
    - 初始条件: left = 0, right = length-1
    - 终止条件: left + 1 == right
    - 向左搜索: right = mid
    - 向右搜索: left = mid 

- ## 三种模版的比较：
    - 不同点主要在三个部分：
        - 左中右的初始化 left, mid, right index assignments
        - 循环/递归的停止条件 loop or recursive termination condition
        - necessity of post-processing 