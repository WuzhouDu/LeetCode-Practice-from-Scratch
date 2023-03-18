# LeetCode-Practice-from-Scratch
This repo is created to record my process of practicing LeetCode coding problems.

# Acknowledgement
Thanks to [代码随想录](https://www.programmercarl.com) for giving a detailed instruction on **how to choose the problems** and in what **order** to solve them. I am following this guide to practice LeetCode problems.

# Catalogue
> **Array**: </br>
    1. [Binary Search](#binary-search) and [related problems](#applications) </br>
    2. [Remove Element](#remove-element) and [related problems](#applications-1) </br>
    3. [squares-of-a-sorted-array](#squares-of-a-sorted-array) </br>
    4. [minimum-size-subarray-sum](#miminum-size-subarray-sum) and [related problems](#applications-2) </br>
    5. [Spiral Matrix](#spiral-matrix) </br>
> **List**: </br>
    1. [remove-linked-list-elements](#remove-linked-list-elements) </br>
    2. [design-linked-list](#design-linked-list) </br>


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
1. referring to [solution](https://www.programmercarl.com/0704.%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE.html#%E6%80%9D%E8%B7%AF), remember to define whether the target is in the range of [left, right] or [left, right). Though in my version I consider the middle as a decision boundary.

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

#### Applications:
1. **fruit into baskets**:
   > My first version: [fruit into baskets](Array/fruit-into-baskets/fruit-into-baskets.cpp) *This version cannot pass all the tests due to the time limit exceediing.* </br>
   > Second version: [fruit into baskets2](Array/fruit-into-baskets/fruit-into-baskets2.cpp) </br>
   > Problem Link: [Chinese Version](https://leetcode-cn.com/problems/fruit-into-baskets/), [English Version](https://leetcode.com/problems/fruit-into-baskets/)

   **Keys**:
   1. In my **first version**, the thought is simple: for every start point, there is only one situation for the number of fruits, so I just need to **iterate all the start points**, i.e. from start to the end, to find the most fruits I can get. But obviously, this can lead to O($n^2$) time complexity.
   2. Applying the thought of **sliding window**, I modify my first version into the second version. The essence is very similar to the previous problem. But this question chooses **iterating the end pointer rather than the start pointer**. Actually, I find that it is more convenient to iterate the end pointer in **sliding window**.</br>

## Spiral Matrix
> My first version: [Spiral Matrix](Array/spiral-matrix-ii/spiral-matrix-ii.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/spiral-matrix-ii/), [English Version](https://leetcode.com/problems/spiral-matrix-ii/)

#### Keys:
   1. **Iterate the matrix layer by layer**. </br>
   2. Pay attention to how to **iterate the matrix layer by layer**. Find the things that ***don't change in every loop and keep consistent*** when judging the loop conditions (***whether the interval is close, open, left-close-right-open or left-open-right-close?***)</br>
   3. This is a very good example to show the manipulation of the loop and the index. </br>



# List
## Remove Linked List Elements
> My first version: [Remove Linked List Elements](List/remove-linked-list-elements/remove-linked-list-elements.cpp) *This version cannot pass the test.* (太菜了┭┮﹏┭┮)</br>
> My second version: [Remove Linked List Elements2](List/remove-linked-list-elements/remove-linked-list-elements2.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/remove-linked-list-elements/), [English Version](https://leetcode.com/problems/remove-linked-list-elements/)

#### Keys
1. In my **first version**, I used a **dummy node** to solve the problem. But my implementation has an error, which is during each while loop, the **current pointer** updation is not correct. There are 2 problems: 
   ```cpp
        while (current->next != NULL){
            if (current->next->val == val){
                if (current->next == head){
                    head = head->next;
                }
                current->next = current->next->next;
            }
            current = current->next;
        }
    ```
   1. My logic is: whether the next node should be deleted or not, **I always move the current pointer to the next in one while loop** (so the current updation is outside of the ```if```). The problem is that, if I remove the last element of the list, the current will become NULL pointer. A test case showing this bug is [1, 2, 3, 5, 6] and remove target is 6. When removing the last element, the current will be a ```NULL``` pointer, leading to a bug.</br>
   2. The second problem is about the updation of ```head```. This is a sub-problem caused by previous problem. An example showing the ```head``` updation bug is [7, 7, 7, 7]. When removing the first element, the ```head``` will be updated to the second ```7```, but the current pointer also points to the second ```7```, missing the removal of the second ```7```. </br>
   3. The core of the above problem is that, **when removing the current's next node, the current pointer should not move to the next in this while loop. Because I don't have the information of the current's next' next**. </br>
   4. After modifying the code, the **[second version](List/remove-linked-list-elements/remove-linked-list-elements2.cpp)** can pass all the tests. </br>

## Design Linked List
> My first version: [Design Linked List](List/design-linked-list/design-linked-list.cpp) </br>
> Second version: [Design Linked List2](List/design-linked-list/design-linked-list2.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/design-linked-list/), [English Version](https://leetcode.com/problems/design-linked-list/)

#### Keys
1. My first version can pass all the tests. But it is obvious that the code is **not well organized**. There are **too many corner cases judgement**. The core problem is that **A dummy head node and an attribute to record the internal size are missing.**</br>
2. [Second version](List/design-linked-list/design-linked-list2.cpp) is the **optimized version**. </br>