# LeetCode-Practice-from-Scratch
This repo is created to record my process of practicing LeetCode coding problems. 
> update 2024.4.8:
> After a long silence, I'd like to pick up the problems and start from the beginning.

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
    3. [reverse-linked-list](#reverse-linked-list) </br>
    4. [swap-nodes-in-pairs](#swap-nodes-in-pairs) </br>
    5. [remove-nth-node-from-end-of-list](#remove-nth-node-from-end-of-list) </br>
    6. [intersection-of-two-linked-lists-lcci](#intersection-of-two-linked-lists) </br>
    7. [Linked List Cycle-ii](#linked-list-cycle-ii) </br>
> **Hash Table**: </br>
    1. [valid-anagram](#valid-anagram) </br>
    2. [intersection-of-two-arrays](#intersection-of-two-arrays) </br>
    3. [happy-number](#happy-number) </br>
    4. [two-sum](#two-sum) </br>
    5. [four-sum-ii](#four-sum-ii) </br>
    6. [3sum](#3sum) </br>
    7. [4sum](#4sum) </br>
> **String**: </br>
    1. [reverse-string](#reverse-string) </br>
    2. [reverse-string-ii](#reverse-string-ii) </br>
    3. [replace-whitespace](#replace-whitespace) </br>
    4. [reverse-words-in-a-string](#reverse-words-in-a-string) </br>
    5. [zuo-xuan-zhuan-zi-fu-chuan-lcof](#zuo-xuan-zhuan-zi-fu-chuan-lcof) </br>
    6. [KMP / find-the-index-of-the-first-occurrence-in-a-string](#kmp-algo--find-the-index-of-the-first-occurrence-in-a-string) </br>
    7. [repeated-substring-pattern](#repeated-substring-pattern) </br>
> **Stack and Queue**: </br>
    1. [implement-queue-using-stacks](#implement-queue-using-stacks) </br>
    2. [implement-stack-using-queues](#implement-stack-using-queues) </br>
    3. [remove-all-adjacent-duplicates-in-string](#remove-all-adjacent-duplicates-in-string) </br>
    4. [valid-parentheses](#valid-parentheses) </br>
    5. [evaluate-reverse-polish-notation](#evaluate-reverse-polish-notation) </br>
    6. [sliding-window-maximum](#sliding-window-maximum) </br>
    7. [top-k-frequent-elements](#top-k-frequent-elements) </br>
> **Binary Tree**: </br>
    1. [binary-tree-preorder-traversal](#binary-tree-preorder-traversal) </br>
    2. [binary-tree-inorder-traversal](#binary-tree-inorder-traversal) </br>
    3. [binary-tree-postorder-traversal](#binary-tree-postorder-traversal) </br>
    4. [binary-tree-level-order-traversal](#binary-tree-level-order-traversal) </br>
    5. [invert-binary-tree](#invert-binary-tree) </br>
    6. [symmetric-tree](#symmetric-tree) </br>
    7. [maximum-depth-of-binary-tree](#maximum-depth-of-binary-tree) </br>
    8. [minimum-depth-of-binary-tree](#minimum-depth-of-binary-tree) </br>
    9. [count-complete-tree-nodes](#count-complete-tree-nodes) </br>
    10. [balanced-binary-tree](#balanced-binary-tree) </br>
    11. [binary-tree-paths](#binary-tree-paths) </br>
    12. [sum-of-left-leaves](#sum-of-left-leaves) </br>
    13. [find-bottom-left-tree-value](#find-bottom-left-tree-value) </br>
    14. [Path Sum](#path-sum) </br>
    15. [Path Sum ii](#path-sum-ii) </br>
    16. [construct-binary-tree-from-inorder-and-postorder-traversal](#construct-binary-tree-from-inorder-and-postorder-traversal) </br>
    17. [construct-binary-tree-from-preorder-and-postorder-traversal](#construct-binary-tree-from-preorder-and-postorder-traversal) </br>
    18. [maximum-binary-tree](#maximum-binary-tree) </br>
    19. [merge-two-binary-trees](#merge-two-binary-trees) </br>
    20. [search-in-a-binary-search-tree](#search-in-a-binary-search-tree) </br>
    21. [validate-binary-search-tree](#validate-binary-search-tree) </br>
    22. [minimum-absolute-difference-in-bst](#minimum-absolute-difference-in-bst) </br>
    23. [find-mode-in-binary-search-tree](#find-mode-in-binary-search-tree) </br>
    24. [lowest-common-ancestor-of-a-binary-tree](#lowest-common-ancestor-of-a-binary-tree) </br>
    25. [lowest-common-ancestor-of-a-binary-search-tree](#lowest-common-ancestor-of-a-binary-search-tree) </br>
    26. [insert-into-a-binary-search-tree](#insert-into-a-binary-search-tree) </br>
    27. [delete-node-in-a-bst](#delete-node-in-a-bst) </br>
    28. [trim-a-binary-search-tree](#trim-a-binary-search-tree) </br>
    29. [convert-sorted-array-to-binary-search-tree](#convert-sorted-array-to-binary-search-tree) </br>
    30. [convert-bst-to-greater-tree](#convert-bst-to-greater-tree) </br>
>   **Backtracking**: </br>
    1. [combinations](#combinations) </br>
    2. [combination-sum-iii](#combination-sum-iii) </br>
    3. [letter-combinations-of-a-phone-number](#letter-combinations-of-a-phone-number) </br>
    4. [combination-sum](#combination-sum) </br>
    5. [combination-sum-ii](#combination-sum-ii)
    6. [restore-ip-addresses](#restore-ip-addresses) </br>
    7. [subsets](#subsets) </br>
    8. [subsets-ii](#subsets-ii) </br>
    9. [non-decreasing-subsequences](#non-decreasing-subsequences) </br>
    10. [permutations](#permutations) </br>
    11. [permutations-ii](#permutations-ii) </br>
    12. [reconstruct-itinerary](#reconstruct-itinerary) </br>
    13. [N-Queens](#n-queens) </br>
    14. [sudoku-solver](#sudoku-solver) </br>
>   **Greeding**: </br>
    1. [wiggle-subsequence](#wiggle-subsequence) <br>
    2. [maximum-subarray](#maximum-subarray) </br>
    3. [best-time-to-buy-and-sell-stock-ii](#best-time-to-buy-and-sell-stock-ii) </br>
    4. [jump-game](#jump-game) </br>
    5. [jump-game-ii](#jump-game-ii) </br>
    6. [maximize-sum-of-array-after-k-negations](#maximize-sum-of-array-after-k-negations) </br>
    7. [assign-cookies]

# Array
## Binary Search
> My first version: [Binary Search](Array/binary_search/binary_search.py) </br>
> 2024-4-8: [Binary Search](Array/binary_search/binary_search_240408.py) </br>
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
    > 2024-4-8: [Search Insert Position](Array/binary_search/search-insert-position-240408.py) </br>
    > Problem Link: [Chinese Version](https://leetcode-cn.com/problems/search-insert-position/), [English Version](https://leetcode.com/problems/search-insert-position/)

    **Why Using Binary Search:**
    1. The array is sorted.
    2. The array is non-repetitive.

    **Key**: Classify the different situations of the target number and consider the corner cases.

#### Any followup?
1. I wonder if there is any problem considering the case where the array is sorted but the element is not unique? And the problem asks us to return the first element. 

## Remove Element
> My first version: [Remove Elements](Array/remove_element/remove-element.cpp) </br>
> 2024-04-08: [Remove Elements](Array/remove_element/remove-element-240408.py) </br>
> 2024-06-24: [Remove Elements](Array/remove_element/remove-element-240624.py) </br>
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
    > 2024-04-08: [Remove Duplicates from Sorted Array](Array/remove_element/remove-duplicates-from-sorted-array-240408.py) </br>
    > 2024-06-24: [Remove Duplicates from Sorted Array](Array/remove_element/remove-duplicates-240624.py) </br> 
    > Problem Link: [Chinese Version](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/), [English Version](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
    
    **Why Using Two Pointers Method:**: the array is sorted in **non-descending order**. So the duplicated elements are adjacent to each other. </br>
    **Think about when the array is not sorted:** the array is not sorted in **non-descending order**. So the duplicated elements are not adjacent to each other. In this case, we can use **Hash Table** to solve the problem. But the time complexity is O(n) and the space complexity is O(n).

2. **Move Zeroes**
    > 2024-06-24: [Move Zeroes](Array/remove_element/move-zeroes-240624.py) </br>
    **key:** the same as removing elements (and the val = 0) in the array.

3. **Backspace String Compare**
    > 2024-06-24: [Backspace String Compare](Array/remove_element/backspace-string-compare-240624.py) </br>
    **key:** from the *end to the start*, and use two pointers to compare the two strings.

## Squares of a Sorted Array
> My first version: [Squares of a Sorted Array](Array/squares_of_a_sorted_array/squares_of_a_sorted_array.cpp) </br>
> Second version: [Squares of a Sorted Array2](Array/squares_of_a_sorted_array/squares_of_a_sorted_array2.cpp) </br>
> 2024-04-08: [Squares of a Sorted Array](Array/squares_of_a_sorted_array/squares_of_a_sorted_array_240408.py) </br>
> 2024-06-25: [Squares of a Sorted Array](Array/squares_of_a_sorted_array/squares_of_a_sorted_array_240625.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/squares-of-a-sorted-array/), [English Version](https://leetcode.com/problems/squares-of-a-sorted-array/)

#### Keys: (Two Pointers Method)
1. In my **first version**, I stuck to the thinking that **I have to sort the result array from left to right in an ascending order**. So, I first use binary search to find the decision boundary of positive and negative numbers, and then use two pointers to merge the two sorted arrays. However, this method is not efficient enough.
2. In my **second version**, not implementing the sorting, I just use two pointers to merge the two sorted arrays in descending order and return the result array from the end of the array to the start. </br>

## Miminum Size Subarray Sum
> My first version: [Minimum Size Subarray Sum](Array/minimum_size_subarray_sum/minimum_size_subarray_sum.cpp) *This first version cannot pass the unit tests provided by LeetCode.* </br>
> Second version: [Minimum Size Subarray Sum2](Array/minimum_size_subarray_sum/minimum_size_subarray_sum2.cpp) </br>
> 2024-04-08: [Minimum Size Subarray Sum](Array/minimum_size_subarray_sum/minimum_size_subarray_sum_240408.py) </br>
> 2024-06-25: [Minimum Size Subarray Sum](Array/minimum_size_subarray_sum/minimum_size_subarray_sum_240625.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/minimum-size-subarray-sum/), [English Version](https://leetcode.com/problems/minimum-size-subarray-sum/)

#### Keys: Sliding Window (Still Two Pointers Method)
1. In my **first version**, I used two pointers, one from the start and the other from the end of the array, to move towards the middle, and find a subarray that cannot be reduced anymore. Nevertheless, this method has an obvious fallacy that it **only considers the partial optimized solution, without a general optimized solution, which is quite like greedy algorithm**. There are many cases this method cannot handle.</br>
2. The second version is about **Sliding Window**, which is a kind of **two pointers method**. It includes all situations and heuristically prevents certain combinations that are not optimal. </br> Actually, there are two kinds of sliding window: **iterate the starting pointer** and **iterate the ending pointer**. In this version, we iterate the start pointer. </br>

#### Applications:
1. **fruit into baskets**:
   > My first version: [fruit into baskets](Array/fruit-into-baskets/fruit-into-baskets.cpp) *This version cannot pass all the tests due to the time limit exceediing.* </br>
   > Second version: [fruit into baskets2](Array/fruit-into-baskets/fruit-into-baskets2.cpp) </br>
   > 2024-04-09: [fruit into baskets](Array/fruit-into-baskets/fruit-into-baskets_240409.py) </br>
   > Problem Link: [Chinese Version](https://leetcode-cn.com/problems/fruit-into-baskets/), [English Version](https://leetcode.com/problems/fruit-into-baskets/)

   **Keys**:
   1. In my **first version**, the thought is simple: for every start point, there is only one situation for the number of fruits, so I just need to **iterate all the start points**, i.e. from start to the end, to find the most fruits I can get. But obviously, this can lead to O($n^2$) time complexity.
   2. Applying the thought of **sliding window**, I modify my first version into the second version. The essence is very similar to the previous problem. But this question chooses **iterating the end pointer rather than the start pointer**. Actually, I find that it is more convenient to iterate the end pointer in **sliding window**.</br>

2. **minimum-window-substring**:
    > 2024-06-25: [minimum-window-substring](Array/minimum-window-substring/minimum-window-substring_240625.py) </br>

## Spiral Matrix
> My first version: [Spiral Matrix](Array/spiral-matrix-ii/spiral-matrix-ii.cpp) </br>
> 2024-04-09: [Spiral Matrix](Array/spiral-matrix-ii/spiral-matrix-ii_240409.py) </br>
> 2024-06-26: [Spiral Matrix](Array/spiral-matrix-ii/spiral-matrix-ii_240626.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/spiral-matrix-ii/), [English Version](https://leetcode.com/problems/spiral-matrix-ii/)
> Another: [Chinese Version](https://leetcode-cn.com/problems/spiral-matrix/), [English Version](https://leetcode.com/problems/spiral-matrix/)
> 2024-06-25: [Spiral Matrix](Array/spiral-matrix-ii/spiral-matrix_240626.py) </br>

#### Keys:
   1. **Iterate the matrix layer by layer**. </br>
   2. Pay attention to how to **iterate the matrix layer by layer**. Find the things that ***don't change in every loop and keep consistent*** when judging the loop conditions (***whether the interval is close, open, left-close-right-open or left-open-right-close?***)</br>
   3. This is a very good example to show the manipulation of the loop and the index. </br>



# List
## Remove Linked List Elements
> My first version: [Remove Linked List Elements](List/remove-linked-list-elements/remove-linked-list-elements.cpp) *This version cannot pass the test.* (太菜了┭┮﹏┭┮)</br>
> My second version: [Remove Linked List Elements2](List/remove-linked-list-elements/remove-linked-list-elements2.cpp) </br>
> 2024-06-26: [Remove Linked List Elements](List/remove-linked-list-elements/remove-linked-list-elements_240626.py) </br>
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
> 2024-06-26: [Design Linked List](List/design-linked-list/design-linked-list_240626.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/design-linked-list/), [English Version](https://leetcode.com/problems/design-linked-list/)

#### Keys
1. My first version can pass all the tests. But it is obvious that the code is **not well organized**. There are **too many corner cases judgement**. The core problem is that **A dummy head node and an attribute to record the internal size are missing.**</br>
2. [Second version](List/design-linked-list/design-linked-list2.cpp) is the **optimized version**. </br>

## Reverse Linked List
> My first version: [Reverse Linked List](List/reverse-linked-list/reverse-linked-list.cpp) </br>
> 2024-06-26: [Reverse Linked List](List/reverse-linked-list/reverse-linked-list_240626.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/reverse-linked-list/), [English Version](https://leetcode.com/problems/reverse-linked-list/)

#### Keys
1. The key is to **use three pointers' updation to iterate the whole linked list**. Pay attention to the **loop condition, that is when the loop is over, which pointer is the division boundary, is there any NULL pointer reference?** Drawing a graph and simulating the process can solve the problem.</br>

## Swap Nodes in Pairs
> My first version: [Swap Nodes in Pairs](List/swap-nodes-in-pairs/swap-nodes-in-pairs.cpp) </br>
> 2024-06-27: [Swap Nodes in Pairs](List/swap-nodes-in-pairs/swap-nodes-in-pairs_240627.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/swap-nodes-in-pairs/), [English Version](https://leetcode.com/problems/swap-nodes-in-pairs/)

#### Keys
1. Just simulate the process of swapping nodes. </br>
2. Pay attention to the **null pointer reference**. (今天终于一直有注意这个情况了！)</br>


## Remove Nth Node From End of List
> My first version: [Remove Nth Node From End of List](List/remove-nth-node-from-end-of-list/remove-nth-node-from-end-of-list.cpp) </br>
> 2024-06-27: [Remove Nth Node From End of List](List/remove-nth-node-from-end-of-list/remove-nth-node-from-end-of-list_240627.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/), [English Version](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

#### Keys
1. **"Two Pointers Method" 双指针法**. </br>
2. Corner case judgement. </br>

## Intersection of Two Linked Lists
> My first version: except for the brutal force method or the hashmap method, no idea </br>
> 2024-06-27: [Intersection of Two Linked Lists](List/intersection-of-two-linked-lists-lcci/intersection-of-two-linked-lists-lcci_240627.py) </br>
> Answer: [Intersection of Two Linked Lists](List/intersection-of-two-linked-lists-lcci/intersection-of-two-linked-lists-lcci.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/intersection-of-two-linked-lists-lcci/), [English Version](https://leetcode.com/problems/intersection-of-two-linked-lists-lcci/)

#### Keys:
1. The reason why I cannot figure out the **$O(n)$** time method is that I do not utilize the condition that **all nodes after the intersection pointer will be the same**. So, two pointers method can dominate.

## Linked List Cycle-ii
> My first version: [Linked List Cycle-ii](List/linked-list-cycle-ii/linked-list-cycle-ii.cpp) </br>
> 2024-06-27: [Linked List Cycle-ii](List/linked-list-cycle-ii/linked-list-cycle-ii_240627.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/linked-list-cycle-ii/), [English Version](https://leetcode.com/problems/linked-list-cycle-ii/)

#### Keys
1. **"Two Pointers Method" 双指针法. Once you meet with this problem, this method will pop up when encountering it again（xuasong:典型的套路题）**. </br>
2. Simulate the process of two pointers and find the internal mathmatical relationship between the two pointers. </br>

## Summary of Linked List
1. Most of the time, using a **dummy head node** can simplify the problem since it can avoid the **head node corner case**. </br>
2. Two pointers method is a **very common method** to solve the linked list problem. </br>
3. Pay attention to the **null pointer reference**. </br>

# Hash Table
## Valid Anagram
> My first version: [Valid Anagram](Hash-Table/valid-anagram/valid-anagram.cpp) </br>
> 2024-06-28: [Valid Anagram](Hash-Table/valid-anagram/valid-anagram_240628.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/valid-anagram/), [English Version](https://leetcode.com/problems/valid-anagram/)

#### Keys:
1. Array is a kind of hash table. The index is the key, and the value is the value. </br>

## intersection-of-two-arrays
> No idea other than brutal force method </br>
> Answer: [intersection-of-two-arrays](Hash-Table/intersection-of-two-arrays/intersection-of-two-arrays.cpp) </br>
> Since the answer uses the ```unordered_set``` container, I have to learn it. Answer link: https://www.programmercarl.com/0349.%E4%B8%A4%E4%B8%AA%E6%95%B0%E7%BB%84%E7%9A%84%E4%BA%A4%E9%9B%86.html#%E6%80%9D%E8%B7%AF</br>
> 2024-06-28: [intersection-of-two-arrays](Hash-Table/intersection-of-two-arrays/intersection-of-two-arrays_240628.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/intersection-of-two-arrays/), [English Version](https://leetcode.com/problems/intersection-of-two-arrays/)

## Happy Number
> My first version: [Happy Number](Hash-Table/happy-number/happy-number.cpp) </br>
> 2024-06-28: [Happy Number](Hash-Table/happy-number/happy-number_240628.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/happy-number/), [English Version](https://leetcode.com/problems/happy-number/)

#### Keys:
1. About the **loop or cycle** detection, if you have to search for the value in the loop, you can use the **set**. Since the set can guarantee the non-repetitiveness.</br>

## Two-sum
> My first version: [Two-sum](Hash-Table/two-sum/two-sum.cpp) </br>
> 2024-06-28: [Two-sum](Hash-Table/two-sum/two-sum_240628.py) </br>
> Porblem Link: [Chinese Version](https://leetcode-cn.com/problems/two-sum/), [English Version](https://leetcode.com/problems/two-sum/)

#### Keys:
1. why using hash map? I have to store the already searched **element and its corresponding index**, which is easy to connect to the "key-value pairs" concept in hash map.

## Four-sum-ii
> My first version: [Four-sum-ii](Hash-Table/four-sum-ii/four-sum-ii.cpp) </br>
> 2024-06-29: [Four-sum-ii](Hash-Table/four-sum-ii/four-sum-ii_240629.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/four-sum-ii/), [English Version](https://leetcode.com/problems/four-sum-ii/)

#### Keys:
1. The brutal force method takes $O(n^4)$ time, which is not acceptable. </br>
2. Similar to the two-sum problem, we can use the hash map to store the sum of two elements and the corresponding number of pairs. </br>

## 3sum
> No idea except hash map. But the de repetition process is trivious and easily bring bugs. It cannot pass. [3sum](Hash-Table/3sum/3sum.cpp) </br>
> 2024-06-29: [3sum](Hash-Table/3sum/3sum_240629.py) </br>
> answer: [3sum](Hash-Table/3sum/3sum2.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/3sum/), [English Version](https://leetcode.com/problems/3sum/)

#### Keys:
1. 首先看懂题目意思。。。说的是元组包含nums中的哪三个数的和为0，而不是这三个数索引的元组。
2. The hardest part is how to avoid repetition. If using **hash method** like [four sum](#four-sum-ii), it is very difficult because of a large number of corner cases.
3. Using **two pointers method**. Firstly sorting the array in order can give the pointers movement a hint. Then the repetition avoidance is easy to accomplish.

## 4sum
> My first version: [4sum](Hash-Table/4sum/4sum.cpp) </br>
> 2024-06-29: [4sum](Hash-Table/4sum/4sum_240629.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/4sum/), [English Version](https://leetcode.com/problems/4sum/)

#### Keys:
1. Very similar to the 3sum problem. Both problems utilize the **two pointers method**.
2. Remember the **overflow problem** and **cutting the branch problem**. Overflow can be caused by the **sum of two numbers**. Cutting the branch can reduce the time.

# String
## Reverse String
> My first version: [Reverse String](String/reverse-string/reverse-string.cpp) </br>
> 2024-07-02: [Reverse String](String/reverse-string/reverse-string_240702.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/reverse-string/), [English Version](https://leetcode.com/problems/reverse-string/)

#### Keys:
1. Very basic problem, use the **two pointers method** to solve it. </br>

## Reverse String-ii
> My first version: [Reverse String-ii](String/reverse-string-ii/reverse-string-ii.cpp) </br>
> 2024-07-02: [Reverse String-ii](String/reverse-string-ii/reverse-string-ii_240702.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/reverse-string-ii/), [English Version](https://leetcode.com/problems/reverse-string-ii/)

#### Keys:
1. Actually, my **first version** is much more complex. The logic is tedious since the **for loop** of the string reversal repeats a lot. Define an additional function to handle this.</br>

## Replace whitespace
> My first version: [Replace white space](String/replace-whitespace/replace-whitespace.cpp) </br>
> 2024-07-02: [Replace white space](String/replace-whitespace/replace-whitespace_240702.py) </br>
> Problem link: [Chinese Version](https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/), [English Version](https://leetcode.com/problems/ti-huan-kong-ge-lcof/)

#### Keys:
1. understand that the string is actually the same as **character array**. So pay attention to the space allocation.
2. Think of **moving pointer from the backward** about the reallocation problem.
3. **Allocate the needed space in advance.**

## Reverse words in a string
> My first version: At first, I have no clear idea. </br>
> After exposure to the answer's thought, the second version: [Reverse words in a string](String/reverse-words-in-a-string/reverse-words-in-a-string.cpp) </br>
> 2024-07-02: [Reverse words in a string](String/reverse-words-in-a-string/reverse-words-in-a-string_240702.py) </br>
> Problem link: [Chinese Version](https://leetcode.cn/problems/reverse-words-in-a-string/submissions/), [English Version](https://leetcode.com/problems/reverse-words-in-a-string/)

#### Keys:
1. Two key points:
2. **How to eliminate the unwanted whitespaces?**: two pointers method. 
3. **How to reverse the order of words, but remain the order of characters in each word?**: reverse all the characters, then reverse each word sparated by white space.

## zuo-xuan-zhuan-zi-fu-chuan-lcof
> My first version: [zuo-xuan-zhuan-zi-fu-chuan-lcof](String/zuo-xuan-zhuan-zi-fu-chuan-lcof/zuo-xuan-zhuan-zi-fu-chuan-lcof.cpp) </br>
> Second version: [zuo-xuan-zhuan-zi-fu-chuan-lcof](String/zuo-xuan-zhuan-zi-fu-chuan-lcof/zuo-xuan-zhuan-zi-fu-chuan-lcof2.cpp) </br>
> 2024-07-08: [zuo-xuan-zhuan-zi-fu-chuan-lcof](String/zuo-xuan-zhuan-zi-fu-chuan-lcof/zuo-xuan-zhuan-zi-fu-chuan-lcof_240708.py) </br>
> Problem link: [Chinese Version](https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/), [English Version](https://leetcode.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/)

#### Keys:
1. In my first version, I consider that no extra space cannot be achieved. But concerning the reverse string operation, it is actually a **in-place operation**. So the extra space is not needed. </br>

## KMP algo / find-the-index-of-the-first-occurrence-in-a-string
> My first version: [find-the-index-of-the-first-occurrence-in-a-string, brutal force](String/find-the-index-of-the-first-occurrence-in-a-string/find-the-index-of-the-first-occurrence-in-a-string.cpp) </br>
> Second version:[KMP](String/find-the-index-of-the-first-occurrence-in-a-string/kmp.cpp) </br>
> 2024-07-08: [KMP](String/find-the-index-of-the-first-occurrence-in-a-string/kmp_240708.py) </br>
> Problem link: [Chinese Version](https://leetcode-cn.com/problems/find-the-index-of-the-first-occurrence-in-a-string/), [English Version](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

#### Keys:
1. **Brutal force method** can solve the problem with $O(n*m)$ time complexity. </br>
2. **KMP algorithm** can solve the problem with $O(n+m)$ time complexity. </br>
3. Understand the **KMP algorithm**: 
   1. how to optimize the **brutal force method**?: use some already known information to avoid some useless comparisons. -> partial match table
   2. how to get partial match table?:
   ```python
   def getNxt(x):
        for i in range(x, 0, -1):
            if p[0:i] == p[x-i+1:x+1]:
                return i
        return 0
    ```
    This will cause $O(m^2)$ time complexity. So we can further optimize it. </br>
    3. how to further optimize the **KMP algorithm**?:
    如何更好地理解和掌握 KMP 算法? - 阮行止的回答 - 知乎
    https://www.zhihu.com/question/21923021/answer/1032665486
    核心的一点是：j一直是当前最长前缀的下一个位置；如果nxt[j] != nxt[i],说明当前后缀不能再用j匹配了，j必须缩小，而如何缩小呢？

## repeated-substring-pattern
> My first version: brutal force, incurs $O(n^2)$ time complexity. </br>
> second version: [repeated-substring-pattern](String/repeated-substring-pattern/repeated-substring-pattern.cpp) </br>
> 2024-07-08: [repeated-substring-pattern](String/repeated-substring-pattern/repeated-substring-pattern_240708.py) </br>
> Problem link: [Chinese Version](https://leetcode-cn.com/problems/repeated-substring-pattern/), [English Version](https://leetcode.com/problems/repeated-substring-pattern/)

#### Keys:
1. The method is very delicate: concatenate the string with itself, then delete the first and the last character. If the string is in the concatenated string, then the string is a repeated substring pattern. </br>
2. It is apparent that this condition is sufficient. But how to prove that it is necessary? [answer](https://leetcode.cn/problems/repeated-substring-pattern/solution/zhong-fu-de-zi-zi-fu-chuan-by-leetcode-solution/)


# Stack and Queue
## implement-queue-using-stacks
> My first version: [implement-queue-using-stacks](Stack-and-Queue/implement-queue-using-stacks/implement-queue-using-stacks.cpp) </br>
> 2024-07-09: [implement-queue-using-stacks](Stack-and-Queue/implement-queue-using-stacks/implement-queue-using-stacks_240709.py) </br>
> Problem link: [Chinese Version](https://leetcode-cn.com/problems/implement-queue-using-stacks/), [English Version](https://leetcode.com/problems/implement-queue-using-stacks/)

#### Keys:
Very fundamental problem. Just pay attention to **when to update the out queue**. </br>

## implement-stack-using-queues
> My first version: [implement-stack-using-queues](Stack-and-Queue/implement-stack-using-queues/implement-stack-using-queues.cpp) </br>
> 2024-07-09: [implement-stack-using-queues](Stack-and-Queue/implement-stack-using-queues/implement-stack-using-queues_240709.py) </br>
> Problem link: [Chinese Version](https://leetcode-cn.com/problems/implement-stack-using-queues/), [English Version](https://leetcode.com/problems/implement-stack-using-queues/)
> Basic problem so no more explanation.

## remove-all-adjacent-duplicates-in-string
> My first version: [remove-all-adjacent-duplicates-in-string](Stack-and-Queue/remove-all-adjacent-duplicates-in-string/remove-all-adjacent-duplicates-in-string.cpp) </br>
> 2024-07-09: [remove-all-adjacent-duplicates-in-string](Stack-and-Queue/remove-all-adjacent-duplicates-in-string/remove-all-adjacent-duplicates-in-string_240709.py) </br>
> Problem link: [Chinese Version](https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string/), [English Version](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/)
> Basic problem so no more explanation.

## Valid Parentheses
> My first version: [Valid Parentheses](Stack-and-Queue/Valid-Parentheses/Valid-Parentheses.cpp) </br>
> 2024-07-09: [Valid Parentheses](Stack-and-Queue/Valid-Parentheses/Valid-Parentheses_240709.py) </br>
> Problem link: [Chinese Version](https://leetcode-cn.com/problems/valid-parentheses/), [English Version](https://leetcode.com/problems/valid-parentheses/)
> Basic problem so no more explanation.

## evaluate-reverse-polish-notation
> My first version: [evaluate-reverse-polish-notation](Stack-and-Queue/evaluate-reverse-polish-notation/evaluate-reverse-polish-notation.cpp) </br>
> 2024-07-09: [evaluate-reverse-polish-notation](Stack-and-Queue/evaluate-reverse-polish-notation/evaluate-reverse-polish-notation_240709.py) </br>
> Problem link: [Chinese Version](https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/), [English Version](https://leetcode.com/problems/evaluate-reverse-polish-notation/)
> Basic problem so no more explanation.

## sliding-window-maximum
> My first version: [sliding-window-maximum](Stack-and-Queue/sliding-window-maximum/sliding-window-maximum.cpp) *This version exceeds the time constraint*</br>
> Second version: [sliding-window-maximum](Stack-and-Queue/sliding-window-maximum/sliding-window-maximum2.cpp) </br>
> 2024-07-09: [sliding-window-maximum](Stack-and-Queue/sliding-window-maximum/sliding-window-maximum_240709.py) </br>
> Problem link: [Chinese Version](https://leetcode-cn.com/problems/sliding-window-maximum/), [English Version](https://leetcode.com/problems/sliding-window-maximum/)

#### Keys:
1. The first version is a **brutal force method wtih $O(n^2)$ time complexity** . It is easy to understand but it exceeds the time constraint. </br>
2. The second version is implementing a descending queue using **double-ended queue with $O(n)$ time complexity**. Another name of this special data structure is **monotonic queue**. The ***essence*** is that:
   1.  when iterating from the **small index to large index**, if a number with low index is smaller than the number with higehr index, it will be **impossible** to occur in the result. To understand this, we should consider that the sliding window is a range from a small index to a large index, the lower index number will quit the window first, so if it is large, it is possible to occur in the result, but if it is small, it will never occur in the result since the latter number will always be over it.</br>
   2. However, how do we know that the large number, the front of the queue, is still in the sliding window? :
      1. We can use the index to record the position of the number. </br>
      2. Or we can use the **pop_front()** function to delete the number that is out of the sliding window. But how do we know that the front of the queue is the number quiting the sliding window? Actually, **we only need to delete those quiting numbers equal to the front of queue.** That is :
      ```cpp
      if (!q.empty() && q.front() == nums[i-1]) q.pop_front();
      ```
        </br>
3. An interesting point when implementing the algorithm: when pushing new numbers, the numbers in the queue should be **descending**. So we need to delete the numbers that are smaller than the new number. But what about the numbers that are equal to the new number? Actually, we **should** keep them in the queue.
    ```cpp
        while (!q.empty() && q.back() < nums[i]){
            q.pop_back();
        }
    ```
    In this line of code, the **<** sign can not be **<=**. If it is **<=**, the numbers that are equal to the new number will be deleted, but when the input case is like: [-7,-8,7,5,7,1,6,0] and k = 4, the problem rises. Since we delete the repeated **7**, when it quits the queue, all the **7** quits and this is not we want. 
    </br>

## top-k-frequent-elements
> I have no idea how to implement $O(nlogn)$ time complexity algo in this problem. </br>
> 2024-07-09: [top-k-frequent-elements](Stack-and-Queue/top-k-frequent-elements/top-k-frequent-elements_240709.py) </br>
> Answer link: [top-k-frequent-elements](Stack-and-Queue/top-k-frequent-elements/top-k-frequent-elements.cpp) </br>
> The analysis is here (**much more deailed and clear than me and I need to reimplement this problem later**): https://leetcode.cn/problems/top-k-frequent-elements/solution/qian-k-ge-gao-pin-yuan-su-by-leetcode-solution/

# Binary Tree
## binary-tree-preorder-traversal
> **Recursive** version: [binary-tree-preorder-traversal](Binary-Tree/binary-tree-preorder-traversal/binary-tree-preorder-traversal.cpp) </br>
> **Iteration Version1**: [binary-tree-preorder-traversal2](Binary-Tree/binary-tree-preorder-traversal/binary-tree-preorder-traversal2.cpp)
> **Iteration Version2**: [binary-tree-preorder-traversal3](Binary-Tree/binary-tree-preorder-traversal/binary-tree-preorder-traversal3.cpp)
> 2024-07-10: [binary-tree-preorder-traversal](Binary-Tree/binary-tree-preorder-traversal/binary-tree-preorder-traversal_240710.py) </br>
> Problem Link: [Chinese Version](https://leetcode.cn/problems/binary-tree-preorder-traversal/), [English Version](https://leetcode.com/problems/binary-tree-preorder-traversal/)

## binary-tree-inorder-traversal
> **Recursive** version: [binary-tree-inorder-traversal](Binary-Tree/binary-tree-inorder-traversal/binary-tree-inorder-traversal.cpp) </br>
> **Iteration Version1**: [binary-tree-inorder-traversal2](Binary-Tree/binary-tree-inorder-traversal/binary-tree-inorder-traversal2.cpp)
> **Iteration Version2**: [binary-tree-inorder-traversal3](Binary-Tree/binary-tree-inorder-traversal/binary-tree-inorder-traversal3.cpp)
> 2024-07-10: [binary-tree-inorder-traversal](Binary-Tree/binary-tree-inorder-traversal/binary-tree-inorder-traversal_240710.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/), [English Version](https://leetcode.com/problems/binary-tree-inorder-traversal/)

## binary-tree-postorder-traversal
> **Recursive** version: [binary-tree-postorder-traversal](Binary-Tree/binary-tree-postorder-traversal/binary-tree-postorder-traversal.cpp) </br>
> **Iteration Version1**: [binary-tree-postorder-traversal2](Binary-Tree/binary-tree-postorder-traversal/binary-tree-postorder-traversal2.cpp)
> **Iteration Version2**: [binary-tree-postorder-traversal3](Binary-Tree/binary-tree-postorder-traversal/binary-tree-postorder-traversal3.cpp)
> 2024-07-10: [binary-tree-postorder-traversal](Binary-Tree/binary-tree-postorder-traversal/binary-tree-postorder-traversal_240710.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/binary-tree-postorder-traversal/), [English Version](https://leetcode.com/problems/binary-tree-postorder-traversal/)

### Keys:
1. The recursive version is easy to understand. The difference between three kinds of orders is jsut the order of recursion. </br>
2. The **gist is iteration method 1:**
   1. We use a **stack** to store the **already-traversed** nodes since this is **DFS** rather than **BFS**. But whether **pushing the nodes to the result** depends on the order of travsersal.</br>
   2. The **preorder** is **root-left-right**, so we should push the **right** node first and then the **left** node. And the root node can be directly pushed to the result since it is already handled.</br>
   3. The **inorder** is quite different. Since the order is **left-root-right**, we traverse to root but it cannot be added to the result, rather, the left should be added to result before root. So, we first traverse to the left-most node, then begin to add the node to the result. </br>
   4. The **postorder** is similar to preorder. </br>
   5. From above, we can see that the three different traversal orders bring different styles of code. </br>
   6. However, in ***Iteration Version2***, all three traversal orders have similar and consistent styles. Here, we use the **null pointer markinig** method. We add a null pointer before the already-traversed nodes so that they should be added to the result.</br>
> 迭代法的核心难点就在于，如何判断这个节点是否已经遍历过了。用空指针标记法就可以很好的统一代码结构。

## binary-tree-level-order-traversal
> **Recursive** version: [binary-tree-level-order-traversal](Binary-Tree/binary-tree-level-order-traversal/binary-tree-level-order-traversal.cpp) </br>
> **Iteration Version**: [binary-tree-level-order-traversal2](Binary-Tree/binary-tree-level-order-traversal/binary-tree-level-order-traversal2.cpp)
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/), [English Version](https://leetcode.com/problems/binary-tree-level-order-traversal/)
> 2024-07-10: [binary-tree-level-order-traversal](Binary-Tree/binary-tree-level-order-traversal/binary-tree-level-order-traversal_240710.py) </br>
> 2024-07-12: [binary-tree-level-order-traversal-ii](Binary-Tree/binary-tree-level-order-traversal/binary-tree-level-order-traversal-ii_240712.py) </br>
> Related Problems: 
> 1.  [binary-tree-right-side-view](https://leetcode.cn/problems/binary-tree-right-side-view/) and [my version](Binary-Tree/binary-tree-level-order-Traversal/binary-tree-right-side-view.cpp)
> 2024-07-12: [binary-tree-right-side-view](Binary-Tree/binary-tree-right-side-view/binary-tree-right-side-view_240712.py) </br>
> 2. [n-ary-tree-level-order-traversal](https://leetcode.cn/problems/n-ary-tree-level-order-traversal/) and [my version(using ***Null pointer mark method***)](Binary-Tree/binary-tree-level-order-Traversal/n-ary-tree-level-order-traversal.cpp)
> 3. [populating-next-right-pointers-in-each-node](https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/description/), 2024-07-12: [populating-next-right-pointers-in-each-node](Binary-Tree/binary-tree-level-order-Traversal/populating-next-right-pointers-in-each-node_240712.py) </br>
> 4. [populating-next-right-pointers-in-each-node-ii](https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii/description/), 2024-07-12: [populating-next-right-pointers-in-each-node-ii](Binary-Tree/binary-tree-level-order-Traversal/populating-next-right-pointers-in-each-node-ii_240712.py) 
> Very good problem combining linkedlist and binary tree. </br>

#### Keys:
1. Since levelorder traversal is **BFS**, we use **queue** to store the nodes traversed. </br>
2. In **recursive method**, we use an additional parameter **depth** to indicate the level of the node. </br>

## Invert Binary Tree
> My version: [invert-binary-tree](Binary-Tree/invert-binary-tree/invert-binary-tree.cpp) </br>
> 2024-07-12: [invert-binary-tree](Binary-Tree/invert-binary-tree/invert-binary-tree_240712.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/invert-binary-tree/), [English Version](https://leetcode.com/problems/invert-binary-tree/)

#### Keys:
1. Use **recursion** or **iteration** to solve this problem. </br>
2. When using **recursion**, we should use *preorder* or *postorder* traversal to invert the tree. **Inorder** is not applicable since after inverting left and right child (traverse the mid point), the right child will be the original left child. </br>

## Symmetric Tree
> My version: [symmetric-tree](Binary-Tree/symmetric-tree/symmetric-tree.cpp) </br>
> 2024-07-12: [symmetric-tree](Binary-Tree/symmetric-tree/symmetric-tree_240712.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/symmetric-tree/), [English Version](https://leetcode.com/problems/symmetric-tree/)

#### Keys:
1. I use the **level order traversal** method to solve this problem. </br>
2. Every level, the nodes should be symmetric. So we use a stack to check the symmetry.</br>


## Maximum Depth of Binary Tree
> My version: [maximum-depth-of-binary-tree](Binary-Tree/maximum-depth-of-binary-tree/maximum-depth-of-binary-tree.cpp) </br>
> 2024-07-12: [maximum-depth-of-binary-tree](Binary-Tree/maximum-depth-of-binary-tree/maximum-depth-of-binary-tree_240712.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/), [English Version](https://leetcode.com/problems/maximum-depth-of-binary-tree/)


## Minimum Depth of Binary Tree
> My version: [minimum-depth-of-binary-tree](Binary-Tree/minimum-depth-of-binary-tree/minimum-depth-of-binary-tree.cpp) </br>
> 2024-07-12: [minimum-depth-of-binary-tree](Binary-Tree/minimum-depth-of-binary-tree/minimum-depth-of-binary-tree_240712.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/), [English Version](https://leetcode.com/problems/minimum-depth-of-binary-tree/)

#### Keys:
1. The difference between **maximum depth** and **minimum depth** is illustrated in this graph. ![](Binary-Tree/minimum-depth-of-binary-tree/111.二叉树的最小深度.png) </br>

## Count Complete Tree Nodes
> My version: [count-complete-tree-nodes](Binary-Tree/count-complete-tree-nodes/count-complete-tree-nodes.cpp) </br>
> 2024-07-12: [count-complete-tree-nodes](Binary-Tree/count-complete-tree-nodes/count-complete-tree-nodes_240712.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/count-complete-tree-nodes/), [English Version](https://leetcode.com/problems/count-complete-tree-nodes/)

#### Keys:
1. If using normal **recursion or iteration** method, the time complexity is $O(n)$ and these methods also apply to any normal binary tree. </br>
2. Utilizing the condition that this is a **complete binary tree**, we can use its property that once we know the depth of the complete binary tree, we get its node number. And if not, just deepening the recursion is ok to get $O(log^2_n)$ time complexity. </br>

## Balanced Binary Tree
> My first version: [balanced-binary-tree](Binary-Tree/balanced-binary-tree/balanced-binary-tree.cpp) </br>
> My second version: [balanced-binary-tree2](Binary-Tree/balanced-binary-tree/balanced-binary-tree2.cpp) </br>
> 2024-07-13: [balanced-binary-tree](Binary-Tree/balanced-binary-tree/balanced-binary-tree_240713.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/balanced-binary-tree/), [English Version](https://leetcode.com/problems/balanced-binary-tree/)

#### Keys:
1. In my **first version**, the time complexity is $O(n^2)$ since I use **recursion** from the **top to down** to solve this problem. That is, for every node traversed, I will **first** calculate whether **this node** is balanced, then consider its **left and right children**. So all the height below this node are calculated, leading to computability waste. </br>
2. In my **second** version, the time complexity is only $O(n)$ since I use **recursion** from the **bottom to top** to solve this problem. </br>

## binary-tree-paths
> My version: [binary-tree-paths](Binary-Tree/binary-tree-paths/binary-tree-paths.cpp) </br>
> Second version: [binary-tree-paths2](Binary-Tree/binary-tree-paths/binary-tree-paths2.cpp) </br>
> 2024-07-13: [binary-tree-paths](Binary-Tree/binary-tree-paths/binary-tree-paths_240713.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/binary-tree-paths/), [English Version](https://leetcode.com/problems/binary-tree-paths/)

#### Keys:
1. How to manipulate and maintain the **already traversed path**? Use **pass by reference** or not? </br>
2. My version uses **pass a string vector by reference** and second version uses **pass a string by value**. But the essence is the same: leave the track with marks.</br>

## sum of left leaves
> My version: [sum-of-left-leaves](Binary-Tree/sum-of-left-leaves/sum-of-left-leaves.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/sum-of-left-leaves/), [English Version](https://leetcode.com/problems/sum-of-left-leaves/)

#### Keys:
1. The challenge lies on the definition of **left leaves**, which means this node is both a leaf and a left node of the parent.
2. Pay attention to the conditions of stopping the recursion: we know **this node's left child is a leaf**. So it is not the common case that the **null pointer** is stopping condition.

## Find Bottom Left Tree Value
> My version: [find-bottom-left-tree-value](Binary-Tree/find-bottom-left-tree-value/find-bottom-left-tree-value.cpp) </br>
> Version2: [find-bottom-left-tree-value2](Binary-Tree/find-bottom-left-tree-value/find-bottom-left-tree-value2.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/find-bottom-left-tree-value/), [English Version](https://leetcode.com/problems/find-bottom-left-tree-value/)

#### Keys:
1. The most intuitive way is to use **level order traversal** to find the leftmost node of the last level. And this is the version 1.</br>
2. The second version is to use **recursion**. The key point is to **record the depth** of the current node. If the depth is larger than the maximum depth, then update the maximum depth and the leftmost node value. </br>

## path-sum
> My version: [path-sum](Binary-Tree/path-sum/path-sum.cpp) </br>
> problem Link: [Chinese Version](https://leetcode-cn.com/problems/path-sum/), [English Version](https://leetcode.com/problems/path-sum/)

#### Keys:
1. typical recursion problem. </br>

## path-sum-ii
> My version: [path-sum-ii](Binary-Tree/path-sum-ii/path-sum-ii.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/path-sum-ii/), [English Version](https://leetcode.com/problems/path-sum-ii/)

#### Keys:
1. The difference between this problem and the previous one is that this problem requires to return all the paths that sum to a given value. So we have to search for the **whole tree**, which means the recursion function should have no return.</br>
2. Use **backtracking** to remove the last element in the path vector after the recursion. And **use pass by reference**.</br>

## construct-binary-tree-from-inorder-and-postorder-traversal
> My version: [construct-binary-tree-from-inorder-and-postorder-traversal](Binary-Tree/construct-binary-tree-from-inorder-and-postorder-traversal/construct-binary-tree-from-inorder-and-postorder-traversal.cpp) </br>
> Second version: [construct-binary-tree-from-inorder-and-postorder-traversal2](Binary-Tree/construct-binary-tree-from-inorder-and-postorder-traversal/construct-binary-tree-from-inorder-and-postorder-traversal2.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/), [English Version](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

#### Keys:
1. The key point is to find the **pivot node** in the **postorder traversal**. The pivot node in the **inorder** array can divide the array into left child tree and right child tree. </br>
2. My version does not use the **unordered_map** to store the index of the inorder array. So the searching process has time complexity $O(n)$. What's more, I define two new vectors every recursion which is costly. The optimized one is the second version. </br>
3. The second version defines a **map** to store the index of the inorder array. So the searching process has time complexity $O(1)$. And the recursion function uses the **range of the inorder and postorder reference** to avoid defining new vectors. </br>

## construct-binary-tree-from-preorder-and-postorder-traversal
> My version: [construct-binary-tree-from-preorder-and-postorder-traversal](Binary-Tree/construct-binary-tree-from-preorder-and-postorder-traversal/construct-binary-tree-from-preorder-and-postorder-traversal.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/), [English Version](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/)

#### Keys:
1. From these two problems above, we can get the key to these constructing problems: **find the pivot node**, which means finding the decision boundary of left and right child tree. </br>

## maximum-binary-tree
> My version: [maximum-binary-tree](Binary-Tree/maximum-binary-tree/maximum-binary-tree.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/maximum-binary-tree/), [English Version](https://leetcode.com/problems/maximum-binary-tree/)

#### Keys:
1. Similar to the construction of binary tree above, we can find the **pivot node** by finding the **maximum value** in the array. </br>

## merge-two-binary-trees
> My version: [merge-two-binary-trees](Binary-Tree/merge-two-binary-trees/merge-two-binary-trees.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/merge-two-binary-trees/), [English Version](https://leetcode.com/problems/merge-two-binary-trees/)

#### Keys:
1. How to handle two trees at the same time? No difference. Just need to process two roots in one recursion. </br>

## search-in-a-binary-search-tree
> My version: [search-in-a-binary-search-tree](Binary-Tree/search-in-a-binary-search-tree/search-in-a-binary-search-tree.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/search-in-a-binary-search-tree/), [English Version](https://leetcode.com/problems/search-in-a-binary-search-tree/)

#### Keys:
1. This is the most basic problem to get familiar with the characteristics of binary search tree. </br> 

## validate-binary-search-tree
> My version: [validate-binary-search-tree](Binary-Tree/validate-binary-search-tree/validate-binary-search-tree.cpp) </br>
> second version: [validate-binary-search-tree2](Binary-Tree/validate-binary-search-tree/validate-binary-search-tree2.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/validate-binary-search-tree/), [English Version](https://leetcode.com/problems/validate-binary-search-tree/)

#### Keys:
1. In my first version, I use **from bottom to top** to check the validity of the tree. If the **left and right children are both valid**, then I use the **BST property** to check whether the **left child's max node is smaller than the current**, and so as the right child. So, this is **postorder** traversal. But this induces **some repetition** when finding the max and min node. </br>
2. Version two handles the reprtition problem. It checks whether the current node's value is in the boundary, and then goes to the left and right child by narrowing the boundary. This is **preorder** traversal.</br>

## minimum-absolute-difference-in-bst
> My version: [minimum-absolute-difference-in-bst](Binary-Tree/minimum-absolute-difference-in-bst/minimum-absolute-difference-in-bst.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/), [English Version](https://leetcode.com/problems/minimum-absolute-difference-in-bst/)

#### Keys:
1. The naive and my first version is to use **inorder traversal** to get the sorted array, and then calculate the minimum difference. </br>
2. The second version maintains a **previous node value** to calculate the minimum difference. So there is no need to allocate another $O(n)$ vector to record all the nodes. </br>

## find-mode-in-binary-search-tree
> My version: [find-mode-in-binary-search-tree](Binary-Tree/find-mode-in-binary-search-tree/find-mode-in-binary-search-tree.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/find-mode-in-binary-search-tree/), [English Version](https://leetcode.com/problems/find-mode-in-binary-search-tree/)

#### Keys:
1. Use **inorder traversal** to get the sorted array, and then store a global maximum frequency to help get the mode during the traversal process. </br>

## lowest-common-ancestor-of-a-binary-tree
> My version: [lowest-common-ancestor-of-a-binary-tree](Binary-Tree/lowest-common-ancestor-of-a-binary-tree/lowest-common-ancestor-of-a-binary-tree.cpp) </br>
> Second version: [lowest-common-ancestor-of-a-binary-tree2](Binary-Tree/lowest-common-ancestor-of-a-binary-tree/lowest-common-ancestor-of-a-binary-tree2.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/), [English Version](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

#### Keys:
1. The two versions are actually the same, but the second version is more concise. </br>
2. Both use the thought of **from the bottom to the top**. If the current node is the **lowest common ancestor**, then it must satisfy that **the left and right child are both marked by the program**. </br>

## lowest-common-ancestor-of-a-binary-search-tree
> My version: [lowest-common-ancestor-of-a-binary-search-tree](Binary-Tree/lowest-common-ancestor-of-a-binary-search-tree/lowest-common-ancestor-of-a-binary-search-tree.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/), [English Version](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

#### Keys:
1. The thought is the same as the previous problem. But this time, we can use the **BST property** to help us find the lowest common ancestor. </br>

## insert-into-a-binary-search-tree
> My version: [insert-into-a-binary-search-tree](Binary-Tree/insert-into-a-binary-search-tree/insert-into-a-binary-search-tree.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/insert-into-a-binary-search-tree/), [English Version](https://leetcode.com/problems/insert-into-a-binary-search-tree/)

#### Keys:
1. This problem is just simulating the process of searching the node in the BST. If the node is not found, then we can insert the node at the leaf. </br>

## delete-node-in-a-bst
> My version: [delete-node-in-a-bst](Binary-Tree/delete-node-in-a-bst/delete-node-in-a-bst.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/delete-node-in-a-bst/), [English Version](https://leetcode.com/problems/delete-node-in-a-bst/)

#### Keys:
1. This problem requires us to consider different cases. But the thought is naive. So, taking every case into consideration is ok. </br>

## trim-a-binary-search-tree
> My version: [trim-a-binary-search-tree](Binary-Tree/trim-a-binary-search-tree/trim-a-binary-search-tree.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/trim-a-binary-search-tree/), [English Version](https://leetcode.com/problems/trim-a-binary-search-tree/)

#### Keys:
1. To solve this problem, you have to understand the **recursion function with TreeNode as the return value**. This thought also applies to the [delete BST](#delete-node-in-a-bst) and [insert BST](#insert-into-a-binary-search-tree), where I use the iteration method instead.</br>

## convert-sorted-array-to-binary-search-tree
> My version: [convert-sorted-array-to-binary-search-tree](Binary-Tree/convert-sorted-array-to-binary-search-tree/convert-sorted-array-to-binary-search-tree.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/), [English Version](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)

#### Keys:
1. With the keys in [trim BST](#trim-a-binary-search-tree), we can solve this problem. </br>

## convert-bst-to-greater-tree
> My version: [convert-bst-to-greater-tree](Binary-Tree/convert-bst-to-greater-tree/convert-bst-to-greater-tree.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/convert-bst-to-greater-tree/), [English Version](https://leetcode.com/problems/convert-bst-to-greater-tree/)

#### Keys:
1. Use **reverse inorder traversal** to solve this problem. </br>

# Backtracking
## Combinations
> My version: [Combinations](Backtracking/Combinations/Combinations.cpp) </br>
> Second version: [Combinations2](Backtracking/Combinations/Combinations2.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/combinations/), [English Version](https://leetcode.com/problems/combinations/)

#### Keys:
1. The intuitive way is to use iteration for k times. But k is a parameter. Use backtracing (recursion) to solve it. </br>
2. To optimize it, the second version can avoid the cases that **the whole searching space is less than the required size**.

## combination-sum-iii
> My version: [combination-sum-iii](Backtracking/combination-sum-iii/combination-sum-iii.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/combination-sum-iii/), [English Version](https://leetcode.com/problems/combination-sum-iii/)

#### Keys:
1. This problem is very similar to the previous one. No need more talking.

## letter-combinations-of-a-phone-number
> My version: [letter-combinations-of-a-phone-number](Backtracking/letter-combinations-of-a-phone-number/letter-combinations-of-a-phone-number.cpp) </br>
> Second version: [letter-combinations-of-a-phone-number2](Backtracking/letter-combinations-of-a-phone-number/letter-combinations-of-a-phone-number2.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/), [English Version](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

#### Keys:
1. My first version is very long because I use **switch** to handle the different cases. </br>
2. The second version is more concise. It uses **map** to store the corresponding letters. But the core idea is the same. </br>

## combination-sum
> My version: [combination-sum](Backtracking/combination-sum/combination-sum.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/combination-sum/), [English Version](https://leetcode.com/problems/combination-sum/)

#### Keys:
1. This problem is a little bit different from above combination sum. Since the elements in combinations can be repeated. </br>

## combination-sum-ii
> My version: [combination-sum-ii](Backtracking/combination-sum-ii/combination-sum-ii.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/combination-sum-ii/), [English Version](https://leetcode.com/problems/combination-sum-ii/)

#### Keys:
1. The difficult point lies in that the candidates include **repetitive elements**, while the answer should **not include repetitive elemetns**. </br>
2. The answer has a very similar idea with [4sum](#4sum): see here
    ```cpp
    if ( j > i+1 && nums[j] == nums[j-1]) continue;
    ```
    and
    ```cpp
    if (i > start && candidates[i] == candidates[i-1]) continue;
    ```
    almost the same! </br>
3. **The [answer](https://www.programmercarl.com/0040.%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8CII.html#%E5%9B%9E%E6%BA%AF%E4%B8%89%E9%83%A8%E6%9B%B2) here has a great explanation of how to avoid repitition.** </br>

## palindrome-partitioning
> My version: [palindrome-partitioning](Backtracking/palindrome-partitioning/palindrome-partitioning.cpp) </br>
> Second version: [palindrome-partitioning2](Backtracking/palindrome-partitioning/palindrome-partitioning2.cpp) </br>
> Third version: [palindrome-partitioning3](Backtracking/palindrome-partitioning/palindrome-partitioning3.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/palindrome-partitioning/), [English Version](https://leetcode.com/problems/palindrome-partitioning/)

#### Keys:
1. In my first version, my thought is that: every time I meet with a new letter, I will decide whether this place can be divided according to the judgement of Palindrome. If it is, then it can be divided. This incurs two paths, one is division and the other is to continue. </br>
2. The second version is more concise. It uses the template **similar to all the backtracking problems above**. The thought is different as well: **the path division lies on where the cutting point is, rather than at each point it is cut or not.** The code difference lies on the backtracking part. </br>
3. The third version is the same as the second version, but it uses **dynamic programming** to preprocess the palindrome information. </br>

## restore-ip-addresses
> My version: [restore-ip-addresses](Backtracking/restore-ip-addresses/restore-ip-addresses.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/restore-ip-addresses/), [English Version](https://leetcode.com/problems/restore-ip-addresses/)

#### Keys:
1. still the same thought as above. But pay attention to **string modification**. </br>

## subsets
> My version: [subsets](Backtracking/subsets/subsets.cpp) </br>
> Second version: [subsets2](Backtracking/subsets/subsets2.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/subsets/), [English Version](https://leetcode.com/problems/subsets/)

#### Keys:
1. this problem is different from above. Here, I have to collect **all the nodes in the traversal tree**, rather than **only the leaf nodes** like the problems above. The answer link has a clear demonstration: https://www.programmercarl.com/0078.%E5%AD%90%E9%9B%86.html#%E5%9B%9E%E6%BA%AF%E4%B8%89%E9%83%A8%E6%9B%B2
   
## subsets-ii
> My version: [subsets-ii](Backtracking/subsets-ii/subsets-ii.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/subsets-ii/), [English Version](https://leetcode.com/problems/subsets-ii/)

#### Keys:
1. apply the thought of [subsets](#subsets) and [repetition avoidance](#combination-sum-ii) to solve this problem. </br>

## non-decreasing-subsequences
> My version: [non-decreasing-subsequences](Backtracking/non-decreasing-subsequences/non-decreasing-subsequences.cpp) </br> ==this version cannot pass==
> Second version: [non-decreasing-subsequences2](Backtracking/non-decreasing-subsequences/non-decreasing-subsequences2.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/increasing-subsequences/), [English Version](https://leetcode.com/problems/increasing-subsequences/)

#### Keys:
1. My first version cannot pass, since this version still uses the same **avoidance of repetition** method:
```cpp
if (i > start && candidates[i] == candidates[i-1]) continue;
```
as above. But this method has an **assumption: the array is in order**. But this problem does not have this assumption. So, we have to record an array **bit_vec** to avoid repetition in this tree depth. </br>

## permutations
> My version: [permutations](Backtracking/permutations/permutations.cpp) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/permutations/), [English Version](https://leetcode.com/problems/permutations/)

#### Keys:
1. This problem is similar to [subsets](#subsets). But the difference is that the **order** of the elements in the array matters. So, we have to use **visited array** to record the elements that have been visited. </br>

## permutations-ii
> My version: [permutations-ii](Backtracking/permutations-ii/permutations-ii.js) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/permutations-ii/), [English Version](https://leetcode.com/problems/permutations-ii/)

#### Keys:
1. Maintain a global variable to record the used **index**. Then, in every depth of the backtrack, maintain a local variable to record the used **element**. Pay attention that in every depth, the specific number should not overlap. </br>

## reconstruct-itinerary
> First version: [reconstruct-itinerary](Backtracking/reconstruct-itinerary/reconstruct-itinerary1.js) </br>
> Second version: [reconstruct-itinerary2](Backtracking/reconstruct-itinerary/reconstruct-itinerary2.js) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/reconstruct-itinerary/), [English Version](https://leetcode.com/problems/reconstruct-itinerary/)

#### Keys:
1. In fact, this problem can also be solved by backtracking. But if adding all available path and finally sort them the memory limit will be exceeded like first version. So, we have to search for those destinations with smaller dictionary order to solve this problem. </br>
2. In the second version, for every depth of backtracking, the **available path** is sorted. So, the first path is the one with the smallest dictionary order. And search those one by one then return as long as find one valid path.</br>

## N-Queens
> My version: [N-Queens](Backtracking/N-Queens/N-Queens.js) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/n-queens/), [English Version](https://leetcode.com/problems/n-queens/)

#### Keys:
1. easy problem. </br>

## sudoku-solver
> My version: [sudoku-solver](Backtracking/sudoku-solver/sudoku-solver.js) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/sudoku-solver/), [English Version](https://leetcode.com/problems/sudoku-solver/)

#### Keys:
1. easy problem. just simulate the process. </br>


# Greeding
## Wiggle subsequence
> My version: [wiggle-subsequence](Greeding/wiggle-subsequence/wiggle-subsequence.js) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/wiggle-subsequence/), [English Version](https://leetcode.com/problems/wiggle-subsequence/)

#### Keys:
1. consider the equality condition.
2. consider the series is monotonic in one direction. In this case you cannot instantly update the maximum length. You have to wait until the series changes its direction. </br>

## maximum-subarray
> My version: [maximum-subarray](Greeding/maximum-subarray/maximum-subarray.js) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/maximum-subarray/), [English Version](https://leetcode.com/problems/maximum-subarray/)

#### keys:
1. The key point is to find the **maximum subarray ending with the current element**. </br>


## Best Time to Buy and Sell Stock ii
> My version: [Best Time to Buy and Sell Stock ii](Greeding/Best-Time-to-Buy-and-Sell-Stock-ii/Best-Time-to-Buy-and-Sell-Stock-ii.js) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/), [English Version](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)

#### Keys:
1. The most profitable way is to buy at the lowest price and sell at the highest price. **But the easy way to do so is to buy the stock as long as the next day's price is higher. Then at the next day we can sell it.** （因为同一天可以卖了又买） Local optimization brings global maximization. </br>

## Jump Game
> My version: [Jump Game](Greeding/Jump-Game/Jump-Game.js) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/jump-game/), [English Version](https://leetcode.com/problems/jump-game/)

#### keys:
nothing to say... only way to solve greeding problem is by thinking greedingly but properly. </br>

## Jump Game ii
> My version: [Jump Game ii](Greeding/Jump-Game-ii/Jump-Game-ii.js) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/jump-game-ii/), [English Version](https://leetcode.com/problems/jump-game-ii/)

#### Keys:
1. 走一步之前，看走一步之后能走到的最远距离。找到可能走到最远的那一步就可以。 </br>

## maximize-sum-of-array-after-k-negations
> My version: [maximize-sum-of-array-after-k-negations](Greeding/maximize-sum-of-array-after-k-negations/maximize-sum-of-array-after-k-negations.js) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/maximize-sum-of-array-after-k-negations/), [English Version](https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/)

#### Keys:
1. greedy: always choose the negative element with largest absolute value to negate. Then choose the smallest positive number to negate.</br>

# Dynamic Programming
## 509. Fibonacci Number
> 2024-07-13: [Fibonacci Number](Dynamic-Programming/Fibonacci-Number/Fibonacci-Number.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/fibonacci-number/), [English Version](https://leetcode.com/problems/fibonacci-number/)

## 70. Climbing Stairs
> 2024-07-13: [Climbing Stairs](Dynamic-Programming/Climbing-Stairs/Climbing-Stairs.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/climbing-stairs/), [English Version](https://leetcode.com/problems/climbing-stairs/)

## 746. Min Cost Climbing Stairs
> 2024-07-13: [Min Cost Climbing Stairs](Dynamic-Programming/Min-Cost-Climbing-Stairs/Min-Cost-Climbing-Stairs.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/min-cost-climbing-stairs/), [English Version](https://leetcode.com/problems/min-cost-climbing-stairs/)

## 62. Unique Paths
> 2024-07-13: [Unique Paths](Dynamic-Programming/Unique-Paths/Unique-Paths.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/unique-paths/), [English Version](https://leetcode.com/problems/unique-paths/)

## 63. Unique Paths II
> 2024-07-13: [Unique Paths II](Dynamic-Programming/Unique-Paths-II/Unique-Paths-II.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/unique-paths-ii/), [English Version](https://leetcode.com/problems/unique-paths-ii/)

## 343. Integer Break
> 2024-07-13: [Integer Break](Dynamic-Programming/Integer-Break/Integer-Break.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/integer-break/), [English Version](https://leetcode.com/problems/integer-break/)

## 96. Unique Binary Search Trees
> 2024-07-13: [Unique Binary Search Trees](Dynamic-Programming/Unique-Binary-Search-Trees/Unique-Binary-Search-Trees.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/unique-binary-search-trees/), [English Version](https://leetcode.com/problems/unique-binary-search-trees/)

## 416. Partition Equal Subset Sum
> 2024-07-15: [Partition Equal Subset Sum](Dynamic-Programming/Partition-Equal-Subset-Sum/Partition-Equal-Subset-Sum.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/partition-equal-subset-sum/), [English Version](https://leetcode.com/problems/partition-equal-subset-sum/)

## 1049. Last Stone Weight II
> 2024-07-15: [Last Stone Weight II](Dynamic-Programming/Last-Stone-Weight-II/Last-Stone-Weight-II.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/last-stone-weight-ii/), [English Version](https://leetcode.com/problems/last-stone-weight-ii/)

## 494. Target Sum
> 2024-07-15: [Target Sum](Dynamic-Programming/Target-Sum/Target-Sum.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/target-sum/), [English Version](https://leetcode.com/problems/target-sum/)

## 474. Ones and Zeroes
> 2024-07-17: [Ones and Zeroes](Dynamic-Programming/Ones-and-Zeroes/Ones-and-Zeroes.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/ones-and-zeroes/), [English Version](https://leetcode.com/problems/ones-and-zeroes/)

## 518. Coin Change II
> 2024-07-17: [Coin Change II](Dynamic-Programming/Coin-Change-II/Coin-Change-II.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/coin-change-ii/), [English Version](https://leetcode.com/problems/coin-change-ii/)

## 377. Combination Sum IV
> 2024-07-18: [Combination Sum IV](Dynamic-Programming/Combination-Sum-IV/Combination-Sum-IV.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/combination-sum-iv/), [English Version](https://leetcode.com/problems/combination-sum-iv/)
> This problem is a **permutation** of the [Coin Change II](#518-coin-change-ii) problem. The complete package problem is a combination problem. Here we should pay attention that **iteration order** determines whether it is combination or permutation. If we iterate every item for the same volume, we are actully considering permutation (the order of each item matters)! If we iterate every volume for the same item, we consider combination (the amount of each item matters). </br>

## 322. Coin Change
> 2024-07-18: [Coin Change](Dynamic-Programming/Coin-Change/Coin-Change.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/coin-change/), [English Version](https://leetcode.com/problems/coin-change/)

## 279. Perfect Squares
> 2024-07-18: [Perfect Squares](Dynamic-Programming/Perfect-Squares/Perfect-Squares.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/perfect-squares/), [English Version](https://leetcode.com/problems/perfect-squares/)

## 139. Word Break
> 2024-07-18: [Word Break](Dynamic-Programming/Word-Break/Word-Break.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/word-break/), [English Version](https://leetcode.com/problems/word-break/)

## 198. House Robber
> 2024-07-18: [House Robber](Dynamic-Programming/House-Robber/House-Robber.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/house-robber/), [English Version](https://leetcode.com/problems/house-robber/)

## 213. House Robber II
> 2024-07-19: [House Robber II](Dynamic-Programming/House-Robber-II/House-Robber-II.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/house-robber-ii/), [English Version](https://leetcode.com/problems/house-robber-ii/)

## 337. House Robber III
> 2024-07-19: [House Robber III](Dynamic-Programming/House-Robber-III/House-Robber-III.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/house-robber-iii/), [English Version](https://leetcode.com/problems/house-robber-iii/)

## 121. Best Time to Buy and Sell Stock
> 2024-07-19: [Best Time to Buy and Sell Stock](Dynamic-Programming/Best-Time-to-Buy-and-Sell-Stock/Best-Time-to-Buy-and-Sell-Stock.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/), [English Version](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

## 122. Best Time to Buy and Sell Stock II
> 2024-07-19: [Best Time to Buy and Sell Stock II](Dynamic-Programming/Best-Time-to-Buy-and-Sell-Stock-II/Best-Time-to-Buy-and-Sell-Stock-II.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/), [English Version](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)

## 123. Best Time to Buy and Sell Stock III
> 2024-07-19: [Best Time to Buy and Sell Stock III](Dynamic-Programming/Best-Time-to-Buy-and-Sell-Stock-III/Best-Time-to-Buy-and-Sell-Stock-III.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/), [English Version](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)

## 188. Best Time to Buy and Sell Stock IV
> 2024-07-20: [Best Time to Buy and Sell Stock IV](Dynamic-Programming/Best-Time-to-Buy-and-Sell-Stock-IV/Best-Time-to-Buy-and-Sell-Stock-IV.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/), [English Version](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)

## 309. Best Time to Buy and Sell Stock with Cooldown
> 2024-07-20: [Best Time to Buy and Sell Stock with Cooldown](Dynamic-Programming/Best-Time-to-Buy-and-Sell-Stock-with-Cooldown/Best-Time-to-Buy-and-Sell-Stock-with-Cooldown.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/), [English Version](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)

## 714. Best Time to Buy and Sell Stock with Transaction Fee
> 2024-07-20: [Best Time to Buy and Sell Stock with Transaction Fee](Dynamic-Programming/Best-Time-to-Buy-and-Sell-Stock-with-Transaction-Fee/Best-Time-to-Buy-and-Sell-Stock-with-Transaction-Fee.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/), [English Version](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)

## 300. Longest Increasing Subsequence
> 2024-07-20: [Longest Increasing Subsequence](Dynamic-Programming/Longest-Increasing-Subsequence/Longest-Increasing-Subsequence.py) </br>
> Problem Link: [Chinese Version](https://leetcode-cn.com/problems/longest-increasing-subsequence/), [English Version](https://leetcode.com/problems/longest-increasing-subsequence/)
> Key: how to understand the `tail` variable is the key to decrease the time complexity. </br>