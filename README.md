# LeetCode-Practice-from-Scratch
This repo is created to record my process of practicing LeetCode coding problems.

# Acknowledgement
Thanks to [代码随想录](https://www.programmercarl.com) for giving a detailed instruction on **how to choose the problems** and in what **order** to solve them. I am following this guide to practice LeetCode problems.

# Catalogue
> **Array**: </br>
    1. [Binary Search](#binary-search) and [related problems](#applications) </br>
    2. [Remove Element](#remove-element) and [related problems](#applications-1) </br>
    3. [squares-of-a-sorted-array](#squares-of-a-sorted-array) </br>
    4. [minimum-size-subarray-sum](#miminum-size-subarray-sum) </br>

# Array
## Binary Search
> My first version: [Binary Search](Array/binary_search/binary_search.py) </br>
> Problem Link: [Chinese Version](https://leetcode.cn/problems/binary-search/), [English Version](https://leetcode.com/problems/binary-search/)
#### Missing Keys:
1. when calculating the 'middle', I did not consider **overflowing of the integer type**, using 
```python
middle = (left + right) // 2
```
instead of
```python
middle = left + (right - left) // 2
```
2. referring to [solution](https://www.programmercarl.com/0704.%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE.html#%E6%80%9D%E8%B7%AF), remember to define whether the target is in the range of [left, right] or [left, right). Though in my version I consider the middle as a decision boundary.

#### Others to Note:
The conditions using **binary search** are usually **sorted** and **non-repetitive elements**.

#### Applications: 
1. **Search Insert Position:**
    > My first version: [Search Insert Position](Array/binary_search/search-insert-position.cpp) </br>
    > Problem Link: [Chinese Version](https://leetcode-cn.com/problems/search-insert-position/), [English Version](https://leetcode.com/problems/search-insert-position/)

    **Why Using Binary Search:**
    1. The array is sorted.
    2. The array is non-repetitive.

    **Key**: Classify the different situations of the target number and consider the corner cases.

## Remove Element
> My first version: [Remove Elements](Array/remove_element/remove-element.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/remove-element/), [English Version](https://leetcode.com/problems/remove-element/)

#### Keys:
1. Use two pointers, one for the current element and the other for the position to be replaced. (**Two Pointers Method or 双指针法**)
2. Only using the original array and the length of the array, **no extra array is needed**.
3. The block:
    ```cpp
    temp[result] = nums[i];
    result++;
    ```
    can be replaced by:
    ```cpp
    nums[result++] = nums[i];
    ```
    Try to be familiar with it.

#### Applications:
1. **Remove Duplicates from Sorted Array**
    > My first version: [Remove Duplicates from Sorted Array](Array/remove_element/remove-duplicates-from-sorted-array.cpp) </br>
    > Problem Link: [Chinese Version](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/), [English Version](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
    
    **Why Using Two Pointers Method:**: the array is sorted in **non-descending order**. So the duplicated elements are adjacent to each other. </br>
    **Think about when the array is not sorted:** the array is not sorted in **non-descending order**. So the duplicated elements are not adjacent to each other. In this case, we can use **Hash Table** to solve the problem. But the time complexity is O(n) and the space complexity is O(n).

## Squares of a Sorted Array
> My first version: [Squares of a Sorted Array](Array/squares_of_a_sorted_array/squares_of_a_sorted_array.cpp) </br>
> Second version: [Squares of a Sorted Array2](Array/squares_of_a_sorted_array/squares_of_a_sorted_array2.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/squares-of-a-sorted-array/), [English Version](https://leetcode.com/problems/squares-of-a-sorted-array/)

#### Keys: (Two Pointers Method)
1. In my **first version**, I stuck to the thinking that **I have to sort the result array from left to right in an ascending order**. So, I first use binary search to find the decision boundary of positive and negative numbers, and then use two pointers to merge the two sorted arrays. However, this method is not efficient enough.
2. In my **second version**, not implementing the sorting, I just use two pointers to merge the two sorted arrays in descending order and return the result array from the end of the array to the start. </br>

## Miminum Size Subarray Sum
> My first version: [Minimum Size Subarray Sum](Array/minimum_size_subarray_sum/minimum_size_subarray_sum.cpp) *This first version cannot pass the unit tests provided by LeetCode.* </br>
> Second version: [Minimum Size Subarray Sum2](Array/minimum_size_subarray_sum/minimum_size_subarray_sum2.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/minimum-size-subarray-sum/), [English Version](https://leetcode.com/problems/minimum-size-subarray-sum/)

#### Keys: Sliding Window (Still Two Pointers Method)
1. In my **first version**, I used two pointers, one from the start and the other from the end of the array, to move towards the middle, and find a subarray that cannot be reduced anymore. Nevertheless, this method has an obvious fallacy that it **only considers the partial optimized solution, without a general optimized solution, which is quite like greedy algorithm**. There are many cases this method cannot handle.</br>
2. The second version is about **Sliding Window**, which is a kind of **two pointers method**. It includes all situations and heuristically prevents certain combinations that are not optimal. </br> Actually, there are two kinds of sliding window: **iterate the starting pointer** and **iterate the ending pointer**. In this version, we iterate the start pointer. </br>